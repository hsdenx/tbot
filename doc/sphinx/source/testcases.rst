.. _Testcases_Documentation:

=======================
Testcases Documentation
=======================

Simply a documentation for all testcases, found in src/tc/

.. _Directory_:

---------
Directory 
---------

.. _Directory_board:

***************
Directory board
***************

.. _bbb:

Directory board/bbb
===================

.. _tc_board_bbb_after_linux_booted_py:

board/bbb/tc_board_bbb_after_linux_booted.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_bbb_after_linux_booted.py


nowadays after booting into linux there comes the message

"random: crng init done"


This pos in, and may disturb a current running test ...


so call this testcase after logging into linux

and wait until this string is read ...



------------------------------------------------

.. _tc_board_bbb_bootmode_py:

board/bbb/tc_board_bbb_bootmode.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_bbb_bootmode.py


switch bootmode for the bbb


- power off the board

- set bootmode

2 states:

normal: we use emmc

recovery: we boot from sd card



------------------------------------------------

.. _tc_board_bbb_bootmode_labdenx_py:

board/bbb/tc_board_bbb_bootmode_labdenx.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_bbb_bootmode_labdenx.py


switch bootmode for the bbb


- power off the board

- set bootmode

2 states:

normal: we use sd card

recovery: we boot from emmc



------------------------------------------------

.. _tc_board_bbb_restore_uboot_py:

board/bbb/tc_board_bbb_restore_uboot.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_bbb_restore_uboot.py

start with

tbot.py -s lab_denx -c beagleboneblack -t tc_demo_part1.py -l log/tbot_demo_part1.log -v


we boot from emmc, if it is broken, we boot

from sdcard and restore a known working uboot on

the emmc.


To switch between botmodes we can use the PIN P8_43

attached to GND -> boot from sd, floating -> boot

from emmc.


------------------------------------------------

.. _tc_board_deploy_beagleboneblack_py:

board/bbb/tc_board_deploy_beagleboneblack.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_deploy_beagleboneblack.py


Copy the binaries from the compile PC

to the tftp directory on the lab PC



------------------------------------------------

.. _tc_board_deploy_lx_beagleboneblack_py:

board/bbb/tc_board_deploy_lx_beagleboneblack.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_deploy_lx_beagleboneblack.py


Copy the linux binaries from the compile PC

to the tftp directory on the lab PC



------------------------------------------------

.. _tc_board_yocto_bbb_all_py:

board/bbb/tc_board_yocto_bbb_all.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_yocto_bbb_all.py


call testcases:

- tc_board_yocto_get_and_bake_py_

- tc_board_yocto_install_nfs_py_

- tc_board_yocto_boot_nfs_py_

- tc_board_yocto_boot_sdcard_py_



------------------------------------------------

.. _tc_board_yocto_boot_nfs_py:

board/bbb/tc_board_yocto_boot_nfs.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_yocto_boot_nfs.py


- set boot mode normal

- go into u-boot

- boot linux with "run net_nfs"

- call tc_board_yocto_install_sdcard_py_



------------------------------------------------

.. _tc_board_yocto_boot_sdcard_py:

board/bbb/tc_board_yocto_boot_sdcard.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_yocto_boot_sdcard.py


- set jumper to normal

- boot sd card image



------------------------------------------------

.. _tc_board_yocto_boot_sdcard_recovery_py:

board/bbb/tc_board_yocto_boot_sdcard_recovery.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_yocto_boot_sdcard_recovery.py


- set recovery mode

- boot with linux from tftp

- boot sd card image



------------------------------------------------

.. _tc_board_yocto_check_rootfs_py:

board/bbb/tc_board_yocto_check_rootfs.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_yocto_check_rootfs.py


check if in booted rootfs, the rootfs version is the

same as in tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version



------------------------------------------------

.. _tc_board_yocto_get_and_bake_py:

board/bbb/tc_board_yocto_get_and_bake.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_yocto_get_and_bake.py


- go to compile PC

- goto lab source dir

- get yocto sources with tc_workfd_get_yocto_source_py_

- bitbake it

- check if files we expect exist

- check tar content

- deploy files (copy to lab PC)

- get rootfs version



------------------------------------------------

.. _tc_board_yocto_install_nfs_py:

board/bbb/tc_board_yocto_install_nfs.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_yocto_install_nfs.py


- set workfd to c_ctrl

- call tc_yocto_install_rootfs_as_nfs_py_

- if tb.config.rootfs_sdcard_file != ''

copy sd card image into nfs

- restore old workfd



------------------------------------------------

.. _tc_board_yocto_install_sdcard_py:

board/bbb/tc_board_yocto_install_sdcard.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_yocto_install_sdcard.py


- install sd card image onto sd card



------------------------------------------------


.. _tc_board_aristainetos2_py:

board/tc_board_aristainetos2.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_aristainetos2.py

start with

tbot.py -s lab_denx -c aristainetos2 -t tc_board_aristainetos2.py

start all testcases for the aristainetos2 board

tc_board_aristainetos2_linux_tests_py_

tc_workfd_set_toolchain_py_


------------------------------------------------

.. _tc_board_aristainetos2_linux_py:

board/tc_board_aristainetos2_linux.py
=====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_aristainetos2_linux.py

start with

tbot.py -s lab_denx -c aristainetos2 -t tc_board_aristainetos2_linux.py

start all linux testcases for the aristainetos2 board


------------------------------------------------

.. _tc_board_aristainetos2_linux_bisect_py:

board/tc_board_aristainetos2_linux_bisect.py
============================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_aristainetos2_linux_bisect.py

start with

tbot.py -s lab_denx -c aristainetos2 -t tc_board_aristainetos2_linux_bisect.py

start a git bisect for the aristainetos2 board


------------------------------------------------

.. _tc_board_aristainetos2_linux_tests_py:

board/tc_board_aristainetos2_linux_tests.py
===========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_aristainetos2_linux_tests.py

start with

tbot.py -s lab_denx -c aristainetos2 -t tc_board_aristainetos2_linux_tests.py

start all linux testcases for the aristainetos2 board


------------------------------------------------

.. _tc_board_ccu1_tests_py:

board/tc_board_ccu1_tests.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_ccu1_tests.py

start with

tbot.py -s lab_denx -c ccu1 -t tc_board_ccu1_tests.py

start all testcases for the ccu1 board


------------------------------------------------

.. _tc_board_corvus_py:

board/tc_board_corvus.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_corvus.py

start with

tbot.py -s lab_denx -c corvus -t tc_board_corvus.py

start all testcases for the corvus board


------------------------------------------------

.. _tc_board_dxr2_py:

board/tc_board_dxr2.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_dxr2.py

start with

tbot.py -s lab_denx -c dxr2 -t tc_board_dxr2.py

start all testcases for the dxr2 board


------------------------------------------------

.. _tc_board_dxr2_linux_py:

board/tc_board_dxr2_linux.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_dxr2_linux.py

start with

tbot.py -s lab_denx -c dxr2 -t tc_board_dxr2_linux.py

start all linux testcases for the dxr2 board


------------------------------------------------

.. _tc_board_dxr2_lx_ubi_tests_py:

board/tc_board_dxr2_lx_ubi_tests.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_dxr2_lx_ubi_tests.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_board_dxr2_lx_ubi_tests.py

more dxr2 specific ubi tests, maybe make them common


------------------------------------------------

.. _tc_board_dxr2_ub_py:

board/tc_board_dxr2_ub.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_dxr2_ub.py

start with

tbot.py -s lab_denx -c dxr2 -t tc_board_dxr2_ub.py

start all u-boot testcases for the dxr2 board


------------------------------------------------

.. _tc_board_dxr2_ub_ubi_py:

board/tc_board_dxr2_ub_ubi.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_dxr2_ub_ubi.py

start with

tbot.py -s lab_denx -c dxr2 -t tc_board_dxr2_ub_ubi.py

start all ubi testcases for the dxr2 board


------------------------------------------------

.. _tc_board_dxr2_uboot_patchwork_py:

board/tc_board_dxr2_uboot_patchwork.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_dxr2_uboot_patchwork.py

start with

python2.7 src/common/tbot.py -c tbot_dxr2_uboot.cfg -t tc_board_dxr2_uboot_patchwork.py

dxr2 check all patches with patchworknumber > default_nr

in patchwork, if it is checkpatch clean and applies to

current mainline without errors


------------------------------------------------

.. _tc_board_fipad_py:

board/tc_board_fipad.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad.py

start with

tbot.py -s lab_denx -c fipad -t tc_board_fipad.py

start all U-Boot/linux testcases for the fipad board


------------------------------------------------

.. _tc_board_fipad_linux_py:

board/tc_board_fipad_linux.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad_linux.py

start with

tbot.py -s lab_denx -c fipad -t tc_board_fipad_linux.py

start all linux testcases for the fipad board


------------------------------------------------

.. _tc_board_fipad_ub_tests_py:

board/tc_board_fipad_ub_tests.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad_ub_tests.py

start with

tbot.py -s lab_denx -c fipad -t tc_board_fipad_ub_tests.py

start all U-Boot testcases for the fipad board


------------------------------------------------

.. _tc_board_fipad_ub_usb_py:

board/tc_board_fipad_ub_usb.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad_ub_usb.py

start with

python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_board_fipad_ub_usb.py


do some simple usb test

- usb start

- usb info (check some output)

- list root dir on the stick

(ext2 formatted stick)

- load test.bin from this partition with ext2load

- check if test.bin has the crc32 sum 0x2144df1c


used vars:

tb.config.tc_uboot_usb_info_expect = [

'Hub,  USB Revision 2.0',

'Mass Storage,  USB Revision 2.0',

'SMI Corporation USB DISK AA04012900007453',

'Vendor: 0x090c  Product 0x1000 Version 17.0'

]

tb.config.tc_board_fipad_uboot_ext2load_files = ['test.bin']

list of files which get load and crc32 tested


------------------------------------------------

.. _tc_board_fipad_upd_ub_py:

board/tc_board_fipad_upd_ub.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad_upd_ub.py

start with

tbot.py -s lab_denx -c fipad -t tc_board_fipad_upd_ub.py

update SPL and u-boot.img on the SPI NOR or the MMC0

card, and boot it ...


------------------------------------------------

.. _tc_board_fipad_upd_ub_mmc_py:

board/tc_board_fipad_upd_ub_mmc.py
==================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad_upd_ub_mmc.py

start with

tbot.py -s lab_denx -c fipad -t tc_board_fipad_upd_ub_mmc.py

update SPL and u-boot.img on the MMC0


------------------------------------------------

.. _tc_board_fipad_upd_ub_spi_py:

board/tc_board_fipad_upd_ub_spi.py
==================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad_upd_ub_spi.py

start with

tbot.py -s lab_denx -c fipad -t tc_board_fipad_upd_ub_spi.py

update SPL and u-boot.img on the SPI NOR


------------------------------------------------

.. _tc_board_flea3_py:

board/tc_board_flea3.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_flea3.py

start with

tbot.py -s lab_denx -c flea3 -t tc_board_flea3.py

start all testcases for the flea3 board

currently only test the nor unprotect with linux


------------------------------------------------

.. _tc_board_mcx_py:

board/tc_board_mcx.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_mcx.py

start with

tbot.py -s lab_denx -c mcx -t tc_board_mcx.py

start all testcases for the mcx board linux stable and linux-ml


------------------------------------------------

.. _tc_board_mcx_tests_py:

board/tc_board_mcx_tests.py
===========================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_mcx_tests.py

start with

tbot.py -s lab_denx -c mcx -t tc_board_mcx_tests.py

start all testcases for the mcx board


------------------------------------------------

.. _tc_board_shc_py:

board/tc_board_shc.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_shc.py

start with

tbot.py -s lab_denx -c shc -t tc_board_shc.py

start all testcases for the shc board linux and linux-stable


------------------------------------------------

.. _tc_board_shc_compile_ml_py:

board/tc_board_shc_compile_ml.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_shc_compile_ml.py

start with

tbot.py -s lab_denx -c shc -t tc_board_shc_compile_ml.py

compile ML linux kernel for the shc board


------------------------------------------------

.. _tc_board_shc_tests_py:

board/tc_board_shc_tests.py
===========================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_shc_tests.py

start with

tbot.py -s lab_denx -c shc -t tc_board_shc_tests.py

start all testcases for the shc board


------------------------------------------------

.. _tc_board_shc_ub_create_regdump_py:

board/tc_board_shc_ub_create_regdump.py
=======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_shc_ub_create_regdump.py

start with

tbot.py -s lab_denx -c shc -t tc_board_shc_ub_create_regdump.py

create a uboot regdump for all interesting registers

on the shc board


------------------------------------------------

.. _tc_board_shc_ub_tests_py:

board/tc_board_shc_ub_tests.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_shc_ub_tests.py

start with

tbot.py -s lab_denx -c shc -t tc_board_shc_ub_tests.py

start all U-Boot testcases for the shc board


------------------------------------------------

.. _tc_board_shc_upd_ub_py:

board/tc_board_shc_upd_ub.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_shc_upd_ub.py

start with

tbot.py -s lab_denx -c shc -t tc_board_shc_upd_ub.py

update MLO and u-boot.img on the SD card or the eMMC

card, and boot it ...


------------------------------------------------

.. _tc_board_sigmatek-nand_py:

board/tc_board_sigmatek-nand.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_sigmatek-nand.py

start with

tbot.py -s lab_denx -c sigmatek-nand -t tc_board_sigmatek-nand.py

On the sigmatek-nand board we have problems with a crash in U-boot

We do:

- wait until linux state is reached

- wait random seconds (3 -10)

- power off the board

- wait 3 seconds for powering really of the board

- loop this 50 times


------------------------------------------------

.. _tc_board_sirius_dds_py:

board/tc_board_sirius_dds.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_sirius_dds.py

start with

python2.7 src/common/tbot.py -c tbot_sirius_dds.cfg -t tc_board_sirius_dds.py

On the sirius board we have problems with ubifs

on nand flash and power cuts. So this is a special

testcase for this board. We do:

- go into statte u-boot

- start linux with ubifs as rootfs

- wait until Userspace APP SiriusApplicat is started

- wait random seconds (3 -10)

- power off the board

- wait 3 seconds for powering really of the board

- loop this 50 times

if we have an ubifs error, testcase ends with error


------------------------------------------------

.. _tc_board_smartweb_py:

board/tc_board_smartweb.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_smartweb.py

start with

tbot.py -s lab_denx -c smartweb -t tc_board_smartweb.py


remove, clone current mainline U-Boot, then

start tc_board_smartweb_test_ub_py_


------------------------------------------------

.. _tc_board_smartweb_test_ub_py:

board/tc_board_smartweb_test_ub.py
==================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_smartweb_test_ub.py

start with

tbot.py -s lab_denx -c smartweb -t tc_board_smartweb.py

start all ub testcases for the smartweb board


------------------------------------------------

.. _tc_board_taurus_py:

board/tc_board_taurus.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_taurus.py

start with

tbot.py -s lab_denx -c taurus -t tc_board_taurus.py

start all testcases for the taurus board


------------------------------------------------

.. _tc_board_thuban_py:

board/tc_board_thuban.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_thuban.py

start with


------------------------------------------------

.. _tc_board_thuban_test_uboot_py:

board/tc_board_thuban_test_uboot.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_thuban_test_uboot.py

start with


------------------------------------------------

.. _tc_board_tqm5200s_try_cur_ub_py:

board/tc_board_tqm5200s_try_cur_ub.py
=====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_tqm5200s_try_cur_ub.py

start with

tbot.py -s lab_denx -c tqm5200s -t tc_board_tqm5200s_try_cur_ub.py

remove current u-boot code on the lab PC

then call tc tc_board_tqm5200s_ub_comp_install_py_


------------------------------------------------

.. _tc_board_tqm5200s_ub_comp_install_py:

board/tc_board_tqm5200s_ub_comp_install.py
==========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_tqm5200s_ub_comp_install.py

start with

tbot.py -s lab_denx -c tqm5200s -t tc_board_tqm5200s_ub_comp_install.py

compile and install U-Boot for the tqm5200s board

install U-Boot with BDI


------------------------------------------------

.. _tc_linux_create_reg_file_am335x_py:

board/tc_linux_create_reg_file_am335x.py
========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_linux_create_reg_file_am335x.py

start with

tbot.py -s lab_denx -c boardname -t tc_linux_create_reg_file_am335x.py

create a regfile for am335x SoC registers


------------------------------------------------

.. _tc_linux_create_reg_file_at91sam9g15_py:

board/tc_linux_create_reg_file_at91sam9g15.py
=============================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_linux_create_reg_file_at91sam9g15.py

start with

python2.7 src/common/tbot.py -c tbot_wivue2.cfg -t tc_linux_create_reg_file_at91sam9g15.py

create a regfile for at91sam9g15 SoC registers


------------------------------------------------

.. _tc_linux_create_reg_file_imx6qdl_py:

board/tc_linux_create_reg_file_imx6qdl.py
=========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_linux_create_reg_file_imx6qdl.py

start with

tbot.py -s lab_denx -c aristainetos2 -t tc_linux_create_reg_file_imx6qdl.py

create a regfile for am335x SoC registers


------------------------------------------------


.. _Directory_debugger:

******************
Directory debugger
******************

.. _bdi:

Directory debugger/bdi
======================

.. _tc_lab_bdi_connect_py:

debugger/bdi/tc_lab_bdi_connect.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/debugger/bdi/tc_lab_bdi_connect.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_bdi_connect.py

connect to the BDI if tb.config.board_has_debugger != 0

- send to workfd tb.config.lab_bdi_upd_uboot_bdi_cmd

- set BDI prompt tb.config.lab_bdi_upd_uboot_bdi_prompt

- wait for BDI prompt


------------------------------------------------

.. _tc_lab_bdi_create_dump_py:

debugger/bdi/tc_lab_bdi_create_dump.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/debugger/bdi/tc_lab_bdi_create_dump.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_bdi_create_dump.py


check if we are on the BDI already, if not switch to it

with tc_lab_bdi_connect_py_


- send "halt"

- dump registers from tb.config.tc_lab_bdi_create_dump_start

to tb.config.tc_lab_bdi_create_dump_stop with mask

tb.config.tc_lab_bdi_create_dump_mask and stepsize

tb.config.tc_lab_bdi_create_dump_type into the file

tb.config.tc_lab_bdi_create_dump_filename


------------------------------------------------

.. _tc_lab_bdi_disconnect_py:

debugger/bdi/tc_lab_bdi_disconnect.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/debugger/bdi/tc_lab_bdi_disconnect.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_bdi_disconnect.py

disconnect from the BDI

- send bdi command "quit"

- set tb.config.linux_prompt


------------------------------------------------

.. _tc_lab_bdi_run_py:

debugger/bdi/tc_lab_bdi_run.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/debugger/bdi/tc_lab_bdi_run.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_bdi_upd_uboot.py

BDI run

- send "res halt" to workfd

- send BDI cmd tb.config.lab_bdi_upd_uboot_bdi_run


------------------------------------------------

.. _tc_lab_bdi_upd_uboot_py:

debugger/bdi/tc_lab_bdi_upd_uboot.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/debugger/bdi/tc_lab_bdi_upd_uboot.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_bdi_upd_uboot.py

update u-boot with BDI

- send BDI cmd: "res halt"

- send BDI cmd: "era"

- send BDI cmd:

tb.config.lab_bdi_upd_uboot_bdi_prog + ' ' + tb.config.lab_bdi_upd_uboot_bdi_file + ' BIN'

- send BDI cmd: tb.config.lab_bdi_upd_uboot_bdi_run


------------------------------------------------



.. _Directory_default:

*****************
Directory default
*****************

.. _tc_def_tbot_py:

default/tc_def_tbot.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/default/tc_def_tbot.py

start with

tbot.py -s lab_denx -c cfgfile -t tc_def_tbot.py

simple set default values for tbot


------------------------------------------------

.. _tc_def_ub_py:

default/tc_def_ub.py
====================

https://github.com/hsdenx/tbot/blob/master/src/tc/default/tc_def_ub.py

start with

tbot.py -s lab_denx -c cfgfile -t tc_def_ub.py

simple set default values for U-Boot testcases


------------------------------------------------


.. _Directory_demo:

**************
Directory demo
**************

.. _linux:

Directory demo/linux
====================

.. _tc_demo_compilepc_linux_compile_py:

demo/linux/tc_demo_compilepc_linux_compile.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/linux/tc_demo_compilepc_linux_compile.py


- switch to compile PC (call tc_connect_to_compilepc_py_)

- call tc_demo_linux_compile_py_


!! changes tb.workfd !!



------------------------------------------------

.. _tc_demo_compilepc_linux_test_py:

demo/linux/tc_demo_compilepc_linux_test.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/linux/tc_demo_compilepc_linux_test.py

start with

- switch to compile PC

- call tc_demo_linux_test_py_



------------------------------------------------

.. _tc_demo_linux_compile_py:

demo/linux/tc_demo_linux_compile.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/linux/tc_demo_linux_compile.py


- goto linux code

- compile it

- deploy it



------------------------------------------------

.. _tc_demo_linux_test_py:

demo/linux/tc_demo_linux_test.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/linux/tc_demo_linux_test.py


- if tb.config.tc_board_bootmode_tc is defined

call tc tb.config.tc_board_bootmode_tc

(set bootmode for the board)

- call tc_workfd_rm_linux_code_py_

- call tc_workfd_get_linux_source_py_

- call tc_workfd_goto_linux_code_py_

- call tc_demo_linux_compile_py_

- tc_demo_linux_testcases_py_



------------------------------------------------

.. _tc_demo_linux_testcases_py:

demo/linux/tc_demo_linux_testcases.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/linux/tc_demo_linux_testcases.py

start with

tbot.py -s lab_denx -c beagleboneblack -t tc_demo_linux_testcases.py


- if tb.config.tc_board_bootmode_tc is set, call

tb.config.tc_board_bootmode_tc

- boot a linux kernel if tb.config.tc_demo_linux_tc_boot_lx

is set to 'yes' 

- get booted linux version

- grep through dmesg and check if strings in

tb.config.tc_demo_linux_test_dmesg exist

- check with devmem2 if the register values defined

in the register files tb.config.tc_demo_linux_test_reg_files

are identical with the values defined in the files

- start cmd defined in tb.config.tc_demo_linux_test_basic_cmd

and check the returning strings.

- call testcase names defined in list tb.config.tc_demo_linux_tc_list



------------------------------------------------


.. _u-boot:

Directory demo/u-boot
=====================

.. _tc_demo_compile_install_test_py:

demo/u-boot/tc_demo_compile_install_test.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/u-boot/tc_demo_compile_install_test.py

start with

tbot.py -c -s lab_denx -c demo -t tc_demo_compile_install_test.py

start tc:

- if tb.config.tc_board_bootmode_tc is defined

call tc tb.config.tc_board_bootmode_tc

(set bootmode for the board)

- go to uboot code with tc_workfd_goto_uboot_code_py_

- set toolchain with tc_workfd_set_toolchain_py_

- compile source tree with tc_workfd_compile_uboot_py_

- if tb.config.tc_demo_uboot_test_deploy != ''

call tb.config.tc_demo_uboot_test_deploy

else

copy files in list tb.config.tc_demo_compile_install_test_files

tb.config.tc_demo_compile_install_test_files contains a list of files,

which are copied to tftp directory

tb.config.tftpdir + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir

- get u-boot version from binary with tc_ub_get_version_py_

- if tb.config.tc_demo_uboot_test_update != '':

call tb.config.tc_demo_uboot_test_update

else:

call tc_ub_upd_uboot_py_

call tc_ub_upd_spl_py_

- if tb.config.tc_demo_compile_install_test_spl_vers_file and/or

tc_tb.config.demo_compile_install_test_ub_vers_file != ''

check if the new installed version is the same

as in the binary files, defined in

tb.config.tc_demo_compile_install_test_ub_vers_file or

tb.config.tc_demo_compile_install_test_spl_vers_file

- call tb.config.tc_demo_compile_install_test_name

which should contain a testcase, which tests the new

installed u-boot

- if tb.config.tc_demo_compile_install_test_poweroff == 'yes':

power off board at the end.


------------------------------------------------

.. _tc_demo_compilepc_compile_install_test_py:

demo/u-boot/tc_demo_compilepc_compile_install_test.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/u-boot/tc_demo_compilepc_compile_install_test.py


call testcases

tc_connect_to_compilepc_py_

tc_demo_compile_install_test_py_



------------------------------------------------

.. _tc_demo_compilepc_uboot_test_py:

demo/u-boot/tc_demo_compilepc_uboot_test.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/u-boot/tc_demo_compilepc_uboot_test.py


- switch to compile PC (call tc_connect_to_compilepc_py_)

- call tc_demo_uboot_test_py_


!! changes tb.workfd !!



------------------------------------------------

.. _tc_demo_get_ub_code_py:

demo/u-boot/tc_demo_get_ub_code.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/u-boot/tc_demo_get_ub_code.py

start with

python2.7 src/common/tbot.py -c tbot_board.cfg -t tc_demo_get_ub_code.py

start tc:

- rm old u-boot tree (if there is one)

- tc_lab_get_uboot_source_py_

- 


------------------------------------------------

.. _tc_demo_uboot_test_py:

demo/u-boot/tc_demo_uboot_test.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/u-boot/tc_demo_uboot_test.py


call testcases

tc_demo_get_ub_code_py_

tc_demo_compile_install_test_py_



------------------------------------------------

.. _tc_demo_uboot_tests_py:

demo/u-boot/tc_demo_uboot_tests.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/u-boot/tc_demo_uboot_tests.py

start with

tbot.py -s lab_denx -c smartweb -t tc_demo_uboot_tests.py


start all "standard" u-boot testcases


- if tb.config.tc_demo_uboot_test_reg_files contains

a list of files, check for each file with testcase

tc_ub_check_reg_file_py_ if the registersettings are

correct.


- start cmd defined in tb.config.tc_demo_uboot_test_basic_cmd

and check the returning strings.


- tb.eof_call_tc("uboot/duts/tc_ub_start_all_duts_py_")


- tb.eof_call_tc("tc_ub_test_py_py_")


- call a list of testcases defined in

tb.config.tc_demo_uboot_tc_list



------------------------------------------------


.. _tc_demo_can_part1_py:

demo/tc_demo_can_part1.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/tc_demo_can_part1.py

start with

python2.7 src/common/tbot.py -c tbot_board.cfg -t tc_demo_can_part1.py

start tc:

starts a can demo

For this demo the fipad board in the denx lab is used.

To test the CAN bus we have in the DENX lab installed a PC, called

CANPC to which a PEAK CAN adapter is attached, which then is connected

to the CAN bus the fipad board is also connected.


We use tc_workfd_can_py_ for testing


We open a new connection to the LabPC, called canm and then we ssh

to the CANPC, from where we then start candump, while on the console

connection a cansend was started. So we can read from the canm

connection, the bytes we send with cansend on the console connection.


If we got the same bytes as we send -> TC True

else the TC returns False


Only one cansend call is tested ... room for more.


------------------------------------------------

.. _tc_demo_part1_py:

demo/tc_demo_part1.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/tc_demo_part1.py

start with

tbot.py -s lab_denx -c smartweb -t tc_demo_part1.py

start tc:


- set workfd to c_ctrl

- call tc_demo_uboot_test_py_



------------------------------------------------

.. _tc_demo_part2_py:

demo/tc_demo_part2.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/tc_demo_part2.py

start with

tbot.py -s lab_denx -c smartweb -t tc_demo_part2.py

start tc:

- call tc_demo_get_ub_code_py_

- call tc_demo_compile_install_test_py_


------------------------------------------------

.. _tc_demo_part3_py:

demo/tc_demo_part3.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/tc_demo_part3.py

start with

tbot.py -s lab_denx -c smartweb -t tc_demo_part3.py

start tc:


------------------------------------------------


.. _Directory_lab:

*************
Directory lab
*************

.. _denx:

Directory lab/denx
==================

.. _tc_lab_denx_connect_to_board_py:

lab/denx/tc_lab_denx_connect_to_board.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_denx_connect_to_board.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_denx_connect_to_board.py

connect to board with connect


------------------------------------------------

.. _tc_lab_denx_disconnect_from_board_py:

lab/denx/tc_lab_denx_disconnect_from_board.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_denx_disconnect_from_board.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_denx_disconnect_from_board.py

disconnect from board in denx vlab


------------------------------------------------

.. _tc_lab_denx_get_power_state_py:

lab/denx/tc_lab_denx_get_power_state.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_denx_get_power_state.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_denx_get_power_state.py

get the power state of the board, and save it in

tb.power_state


------------------------------------------------

.. _tc_lab_denx_power_py:

lab/denx/tc_lab_denx_power.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_denx_power.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_denx_power.py

power on/off the board 


------------------------------------------------

.. _tc_lab_interactive_get_power_state_py:

lab/denx/tc_lab_interactive_get_power_state.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_interactive_get_power_state.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_denx_get_power_state.py

get the power state of the board through user input,

and save it in tb.power_state


------------------------------------------------

.. _tc_lab_interactive_power_py:

lab/denx/tc_lab_interactive_power.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_interactive_power.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_denx_power.py

power on/off the board from hand


------------------------------------------------


.. _tc_lab_power_onoff_gpio_py:

lab/tc_lab_power_onoff_gpio.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_power_onoff_gpio.py


Switch on/off boardpower through a GPIO pin

from the lab PC


define the gpio for powering on/off in your board config

file with for example:

gpio_power_on = gpo(21)  gpio number of gpio used to controll power of board



------------------------------------------------

.. _tc_lab_prepare_py:

lab/tc_lab_prepare.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_prepare.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_prepare.py


when logging into a lab, do some basic setup

- go into workdir

- if tb.config.tc_lab_prepare_tc_name != 'none' then call

testcase which name is defined in tb.config.tc_lab_prepare_tc_name


In this testcase, you can do lab specific setup you need

and set the variable tb.config.tc_lab_prepare_tc_name

with the name you give your testcase for lab specific setup.



------------------------------------------------

.. _tc_lab_prepare_laptop_hs_py:

lab/tc_lab_prepare_laptop_hs.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_prepare_laptop_hs.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_prepare_laptop_hs.py


do setup needed for the laptop from hs, when used as

lapPC



------------------------------------------------

.. _tc_lab_prepare_tbot2go_py:

lab/tc_lab_prepare_tbot2go.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_prepare_tbot2go.py

start with


do setup needed for the pi in tbot2go mode, when used as

lapPC



------------------------------------------------

.. _tc_lab_sispmctl_get_power_state_py:

lab/tc_lab_sispmctl_get_power_state.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_sispmctl_get_power_state.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_sispmctl_get_power_state.py

get the power state of the board through sispmctl

and save it in tb.power_state

find more information for the Gembird Silver Shield PM power controller:

http://sispmctl.sourceforge.net/


use testcase "tc_lab_sispmctl_get_variables_py_" for setting

the serial and the index you need for the specific board.


This file is an example for a setup, you need to adapt

this to your needs.



------------------------------------------------

.. _tc_lab_sispmctl_get_variables_py:

lab/tc_lab_sispmctl_get_variables.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_sispmctl_get_variables.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_sispmctl_get_variables.py

get serial and index for tb.config.boardlabpowername for

controlling the Gembird Silver Shield PM power controller

and save it in tb.config.gembird_serial and tb.config.gembird_index



------------------------------------------------

.. _tc_lab_sispmctl_set_power_state_py:

lab/tc_lab_sispmctl_set_power_state.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_sispmctl_set_power_state.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_sispmctl_set_power_state.py

power on/off the board


get the power state of the board through sispmctl

and save it in tb.power_state

find more information for the Gembird Silver Shield PM power controller:

http://sispmctl.sourceforge.net/


use testcase "tc_lab_sispmctl_get_variables_py_" for setting

the serial and the index you need for the specific board.


This file is an example for a setup, you need to adapt

this to your needs.



------------------------------------------------

.. _tc_lab_usb_relay_power_py:

lab/tc_lab_usb_relay_power.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_usb_relay_power.py

power on / off the board tb.config.boardlabpowername

with testcase tc_linux_relay_simple_set_py_


simple util must be installed, source see

src/files/relay/simple.c


adapt dependend on tb.config.boardlabpowername

which port you use..


If you have more than one USB relay from sainsmart

adapt simple.c to work with the serial ID, and adapt

also tb.config.tc_linux_relay_simple_set_cmd



------------------------------------------------


.. _Directory_linux:

***************
Directory linux
***************

.. _relay:

Directory linux/relay
=====================

.. _tc_linux_relay_get_config_py:

linux/relay/tc_linux_relay_get_config.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/relay/tc_linux_relay_get_config.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_linux_relay_get_config.py

get relay tbot configuration


input:

tb.config.tc_linux_relay_set_port

tb.config.tc_linux_relay_set_state


output:

tb.config.tc_linux_relay_set_tc

testcase which gets called for setting relay port  with state state

also set the config variables for tb.config.tc_linux_relay_set_tc

accordingly.


------------------------------------------------

.. _tc_linux_relay_set_py:

linux/relay/tc_linux_relay_set.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/relay/tc_linux_relay_set.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_linux_relay_set.py

set relay port tb.config.tc_linux_relay_set_port to state

tb.config.tc_linux_relay_set_state.


you need to adapt tc_linux_relay_get_config_py_, which does

the mapping from port/state to your specific lab settings.



------------------------------------------------

.. _tc_linux_relay_simple_set_py:

linux/relay/tc_linux_relay_simple_set.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/relay/tc_linux_relay_simple_set.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_linux_relay_set.py

set relay port with the simple cmd to state

find the c source code for the simple cmd in src/files/relay/simple.c


tb.config.tc_linux_relay_simple_set_sudo if 'yes' "sudo" is perpended to

tb.config.tc_linux_relay_simple_set_cmd and if password is needed, password

is searched in password_py_ with board = tb.config.ip and user = tb.config.user + '_sudo'



------------------------------------------------


.. _ubi:

Directory linux/ubi
===================

.. _tc_lx_ubi_attach_py:

linux/ubi/tc_lx_ubi_attach.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/ubi/tc_lx_ubi_attach.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_ubi_attach.py


------------------------------------------------

.. _tc_lx_ubi_detach_py:

linux/ubi/tc_lx_ubi_detach.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/ubi/tc_lx_ubi_detach.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_ubi_detach.py

detach ubi device tb.config.tc_ubi_mtd_dev


------------------------------------------------

.. _tc_lx_ubi_format_py:

linux/ubi/tc_lx_ubi_format.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/ubi/tc_lx_ubi_format.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_ubi_format.py

ubiformat tb.config.tc_ubi_mtd_dev with tb.config.tc_lx_ubi_format_filename


------------------------------------------------

.. _tc_lx_ubi_info_py:

linux/ubi/tc_lx_ubi_info.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/ubi/tc_lx_ubi_info.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_ubi_info.py

ubinfo tb.config.tc_ubi_ubi_dev


------------------------------------------------

.. _tc_lx_ubi_tests_py:

linux/ubi/tc_lx_ubi_tests.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/ubi/tc_lx_ubi_tests.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_ubi_tests.py

- install mtd utils if needed with tc_lx_mtdutils_install_py_

- attach ubi device with tc_lx_ubi_attach_py_

- get info with tc_lx_ubi_info_py_

- get parameters with tc_lx_get_ubi_parameters_py_


------------------------------------------------


.. _xenomai:

Directory linux/xenomai
=======================

.. _tc_xenomai_common_py:

linux/xenomai/tc_xenomai_common.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/xenomai/tc_xenomai_common.py


basic xenomai tests


- simply call "cat /proc/xenomai/\*"


ToDo: call xeno-test



------------------------------------------------

.. _tc_xenomai_latency_py:

linux/xenomai/tc_xenomai_latency.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/xenomai/tc_xenomai_latency.py


start latency command tb.config.tc_xenomai_latency_lcmd from the xenomai

tools. Use paramter -g for creating histogram to file

tb.config.tc_xenomai_latency_tmpfile in gnuplot format.

Save this file into tb.config.tc_xenomai_latency_datfile2

on the lab PC.


While latency test is running, extract the content of the

line starting with "RTD" into the file

tb.config.tc_xenomai_latency_datfile


This testcase runs the latency tool until tb.config.tc_xenomai_latency_count

lines are read. While running it checks if the value

of the column "lat max" is lower than tb.config.tc_xenomai_latency_max

Than this testcase ends with True, else Testcase ends with False.


At the end of this tetscase, it creates the png images

of the files tb.config.tc_xenomai_latency_datfile

and tb.config.tc_xenomai_latency_datfile2 on the host PC

using gnuplot tool.


Therefore the files

src/files/balkenplot_lat_tbot.sem

src/files/balkenplot_latency.sem

are used.



------------------------------------------------


.. _tb_workfd_check_if_process_run_py:

linux/tb_workfd_check_if_process_run.py
=======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tb_workfd_check_if_process_run.py

check if process with name

tb.config.tc_workfd_check_if_process_run_name

runs



------------------------------------------------

.. _tc_connect_to_compilepc_py:

linux/tc_connect_to_compilepc.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_connect_to_compilepc.py


This testcase creates a third connection handle to the lab and uses

ssh to create a connection to a compile pc.

The third connection can then be used with tb.workfd and tb.c_cpc

to outsource resource hungry tasks like compiling.


! workfd is set after calling this testcase to the new connection !


The vars tb.config.compile_pc_ip, tb.config.compile_pc_user

tb.config.connect_to_compilepc_ssh_opt, tb.config.connect_to_compilepc_ssh_cmd_prompt

could also be a list of strings.



------------------------------------------------

.. _tc_git_get_branch_commit_py:

linux/tc_git_get_branch_commit.py
=================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_git_get_branch_commit.py

start with

python2.7 src/common/tbot.py -c tbot.cfg -t tc_git_get_branch_commit.py

get current branch, commit from git tree in directory

tb.config.tc_git_get_branch_commit_tree


save values in

tb.config.tc_git_get_branch_commit_dirty

tb.config.tc_git_get_branch_commit_branch

tb.config.tc_git_get_branch_commit_commit



------------------------------------------------

.. _tc_linux_top_py:

linux/tc_linux_top.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_linux_top.py


This testcase starts the linux "top" command

with the top cmdline arguments tb.config.tc_linux_top_count

and tb.config.tc_linux_top_sec


amd analyses the output and write them into the file

tb.config.tc_linux_top_filename in a gnuplot format.


used config vars.

tb.config.tc_linux_top_count top count argument

default: '10'

tb.config.tc_linux_top_sec top seconds argument

default: '2'

tb.config.tc_linux_top_filename filename where the results are stored

default: 'top-stat.dat'


create the images with gnuplot:


gnuplot src/files/top_plot_mem.sem

result image

top-mem-output.jpg

gnuplot src/files/top_plot_cpu.sem

result image

top-cpu-output.jpg

gnuplot src/files/top_plot_load.sem

result image

top-load-output.jpg


!! may you need to adapt path in src/files/top_plot\*.sem files

ToDo: pass paramter workdir to gnuplot


While at it, include a demo for adding it to the dashboard

backend and create a demo documentation.


If you use this testcase in conjunction with other testcases

you should remove the line

tb.config.create_documentation_auto = 'linux_top'



------------------------------------------------

.. _tc_lx_bonnie_py:

linux/tc_lx_bonnie.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_bonnie.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_bonnie.py

run a bonnie test, if timer tc_workfd_check_tc_time_py_ timed out

- try to install bonnie if not is installed tc_lx_bonnie_install_py_

- start bonnie on device tb.config.tc_lx_bonnie_dev with

size tb.config.tc_lx_bonnie_sz


------------------------------------------------

.. _tc_lx_bonnie_install_py:

linux/tc_lx_bonnie_install.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_bonnie_install.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_bonnie_install.py

get bonnie source and install it


------------------------------------------------

.. _tc_lx_check_reg_file_py:

linux/tc_lx_check_reg_file.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_check_reg_file.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_check_reg_file.py

checks if the default values in reg file tb.config.tc_lx_create_reg_file_name

on the tbot host in tb.workdir have the same values, as the

registers on the board. Needs devmem2 installed.

format of the regfile:

regaddr mask type defval


If you have to call devmem2 with a "header"

set it through tb.config.devmem2_pre

so on the bbb with original rootfs -> no devmem2 installed

so to use tc which use devmem2 you have to copy devmem2

bin to the rootfs, and start it with 'sudo ...'


ToDo: use the file from the lab host, not the tbot host


------------------------------------------------

.. _tc_lx_check_usb_authorized_py:

linux/tc_lx_check_usb_authorized.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_check_usb_authorized.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_check_usb_authorized.py

check if usb device tb.config.tc_lx_check_usb_authorized needs authorizing


------------------------------------------------

.. _tc_lx_cmd_and_grep_py:

linux/tc_lx_cmd_and_grep.py
===========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_cmd_and_grep.py


loop over the list of strings in the tb.config.tc_lx_cmd_and_grep

"cmds" key.

for each command save the output in a temporary file, and

search that all strings in key="cmd" are in the temporary file.


example tb.config.tc_lx_cmd_and_grep

tc_lx_cmd_and_grep = {"cmds" : ["cat /proc/partitions",

"cat /proc/mounts"],

"cat /proc/partitions" :

[

"mmcblk0p1",

"mmcblk0p2",

]

,

"cat /proc/mounts" : [

"/ squashfs ro,noatime 0 0",

"tmp /tmp tmpfs rw,relatime 0 0",

]}


This will do:

- "cat /proc/partitions > gnlmpf"

- search if gnlmpf contains the strings "mmcblk0p1" and "mmcblk0p2"

- "cat /proc/mounts > gnlmpf"

- search if gnlmpf contains the strings

"/ squashfs ro,noatime 0 0"

"tmp /tmp tmpfs rw,relatime 0 0"



------------------------------------------------

.. _tc_lx_cpufreq_py:

linux/tc_lx_cpufreq.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_cpufreq.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_cpufreq.py

check if frequencies in tb.config.tc_lx_cpufreq_frequences

are possible to set with cpufreq-info


------------------------------------------------

.. _tc_lx_create_dummy_file_py:

linux/tc_lx_create_dummy_file.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_create_dummy_file.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_create_dummy_file.py

create a random dummy file tb.tc_lx_dummy_file_tempfile in linux

on tb.c_con with bs = tb.tc_lx_dummy_file_bs and

count = tb.tc_lx_dummy_file_count


------------------------------------------------

.. _tc_lx_create_reg_file_py:

linux/tc_lx_create_reg_file.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_create_reg_file.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_create_reg_file.py

creates a reg file tb.config.tc_lx_create_reg_file_name on the tbot host

in tb.workdir

read from tb.config.tc_lx_create_reg_file_start to tb.config.tc_lx_create_reg_file_stop

and writes the results in the regfile

format of the regfile:

regaddr mask type defval

This reg file can be used as a default file, how the

registers must be setup, check it with testcase

tc_lx_check_reg_file_py_


If you have to call devmem2 with a "header"

set it through tb.config.devmem2_pre

so on the bbb with original rootfs -> no devmem2 installed

so to use tc which use devmem2 you have to copy devmem2

bin to the rootfs, and start it with 'sudo ...'


ToDo: use the file from the lab host, not the tbot host


------------------------------------------------

.. _tc_lx_devmem2_install_py:

linux/tc_lx_devmem2_install.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_devmem2_install.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_devmem2_install.py

get devmem2 source from www.lartmaker.nl/lartware/port/devmem2.c

and install it


------------------------------------------------

.. _tc_lx_dmesg_grep_py:

linux/tc_lx_dmesg_grep.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_dmesg_grep.py


check if string tb.config.tc_lx_dmesg_grep_name is in dmesg output.

make the grep options configurable through tb.config.tc_lx_dmesg_grep_options



------------------------------------------------

.. _tc_lx_eeprom_py:

linux/tc_lx_eeprom.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_eeprom.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_eeprom.py

Test an eeprom:

- read the content from eeprom @ tb.config.tc_lx_eeprom_tmp_dir

with "cat" into tmpfile

- check tb.config.tc_lx_eeprom_wp_gpio != 'none'

if WP pin works

- generate random file with tb.config.tc_lx_eeprom_wp_sz size

- write it into eeprom

- reread it

- compare it with original

- restore original eeprom content at end


------------------------------------------------

.. _tc_lx_get_ubi_parameters_py:

linux/tc_lx_get_ubi_parameters.py
=================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_get_ubi_parameters.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_get_ubi_parameters.py

get ubi parameters of ubi device tb.config.tc_ubi_mtd_dev

save them into:

- tb.config.tc_ubi_max_leb_cnt

- tb.config.tc_ubi_min_io_size

- tb.config.tc_ubi_leb_size


------------------------------------------------

.. _tc_lx_get_version_py:

linux/tc_lx_get_version.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_get_version.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_get_version.py

get the linux version and create event LINUX_VERSION

save the linux version in tb.config.tc_return


------------------------------------------------

.. _tc_lx_gpio_py:

linux/tc_lx_gpio.py
===================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_gpio.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_gpio.py

set in linux gpio tb.config.tc_lx_gpio_nr to direction tb.config.tc_lx_gpio_dir

and value tb.config.tc_lx_gpio_val


------------------------------------------------

.. _tc_lx_mount_py:

linux/tc_lx_mount.py
====================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_mount.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_mount.py

mount device tb.config.tc_lx_mount_dev with fs type tb.config.tc_lx_mount_fs_type

to tb.config.tc_lx_mount_dir


------------------------------------------------

.. _tc_lx_mtdutils_install_py:

linux/tc_lx_mtdutils_install.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_mtdutils_install.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_mtdutils_install.py

check if mtdutils are installed. If not, clone the code with

git clone git://git.infradead.org/mtd-utils.git mtd-utils

and install it


------------------------------------------------

.. _tc_lx_partition_check_py:

linux/tc_lx_partition_check.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_partition_check.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_partition_check.py

cp a dummy file into a partiton umount/mount it and

compare it.

- Mount tb.config.tc_lx_mount_dir with tc_lx_mount_py_


------------------------------------------------

.. _tc_lx_partitions_grep_py:

linux/tc_lx_partitions_grep.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_partitions_grep.py


check, if all strings in tb.config.tc_lx_ps_partitions are

in "cat /proc/partitions" output.



------------------------------------------------

.. _tc_lx_printenv_py:

linux/tc_lx_printenv.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_printenv.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_printenv.py

simple printenv linux command


------------------------------------------------

.. _tc_lx_ps_grep_py:

linux/tc_lx_ps_grep.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_ps_grep.py


check, if all strings in tb.config.tc_lx_ps_grep are

in ps output.



------------------------------------------------

.. _tc_lx_regulator_py:

linux/tc_lx_regulator.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_regulator.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_regulator.py

check if regulators in tb.config.tc_lx_regulator_nrs exist, and have

the correct microvolts settings.


------------------------------------------------

.. _tc_lx_trigger_wdt_py:

linux/tc_lx_trigger_wdt.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_trigger_wdt.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_trigger_wdt.py

simple trigger wdt with command tb.config.tc_lx_trigger_wdt_cmd


------------------------------------------------

.. _tc_lx_uname_py:

linux/tc_lx_uname.py
====================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_uname.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_uname.py

simple linux "uname -a" command


------------------------------------------------

.. _tc_workfd_apply_local_patches_py:

linux/tc_workfd_apply_local_patches.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_apply_local_patches.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_apply_local_patches.py

apply patches from directory tb.config.tc_workfd_apply_local_patches_dir

with 'git am -3' to the source in current directory.

if tb.config.tc_workfd_apply_local_patches_checkpatch_cmd != 'none'

check the patches with the checkpatch cmd tb.config.tc_workfd_apply_local_patches_checkpatch_cmd

before applying.


------------------------------------------------

.. _tc_workfd_apply_patchwork_patches_py:

linux/tc_workfd_apply_patchwork_patches.py
==========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_apply_patchwork_patches.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_apply_patchwork_patches.py

apply patchworkpatches from list:

tb.config.tc_workfd_apply_patchwork_patches_list:

to source in current directory.

creates event:

- PW_NR: which patchwork number used

- PW_CLEAN: is it checkpatch clean

- PW_AA: already applied

- PW_APPLY: apply it clean to source


------------------------------------------------

.. _tc_workfd_can_py:

linux/tc_workfd_can.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_can.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_can.py


minimal can test:

starts a new connection named tb_canm. This connection runs

on board/PC which has a can conncetion to the board tbot

tests, named CAN PC.

If necessary (tb.config.tc_workfd_can_ssh != 'no'), tc connects first

to ssh (if the CAN PC is not the lab PC). Also if necessary

(tb.config.tc_workfd_can_su != 'no', switch to superuser on the CAN PC.


Set on the CAN PC, with the "ip" command the bitrate

tb.config.tc_workfd_can_bitrate for the can device tb.config.tc_workfd_can_dev

and activate the interface.


Now on the board, go into tb.config.tc_workfd_can_iproute_dir

(which contains the "ip" command ...

Set the bitrate with it and activate the can interface.

Goto into tb.config.tc_workfd_can_util_dir which contains canutils

Send '123DEADBEEF' with cansend


check if the CAN PC gets this string.

End True if this is the case, False else


ToDo:

- get rid of tb.config.tc_workfd_can_iproute_dir and tb.config.tc_workfd_can_util_dir

(add the commands to rootfs ...)

- support different can devices on the CAN PC and board


------------------------------------------------

.. _tc_workfd_cd_to_dir_py:

linux/tc_workfd_cd_to_dir.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_cd_to_dir.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_cd_to_dir.py

simple cd into directory tb.config.tc_workfd_cd_name


------------------------------------------------

.. _tc_workfd_check_cmd_success_py:

linux/tc_workfd_check_cmd_success.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_cmd_success.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_check_cmd_success.py

simple check if previous shell command was succesful


------------------------------------------------

.. _tc_workfd_check_if_cmd_exist_py:

linux/tc_workfd_check_if_cmd_exist.py
=====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_if_cmd_exist.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_check_if_cmd_exist.py

check if a command exists


------------------------------------------------

.. _tc_workfd_check_if_device_exist_py:

linux/tc_workfd_check_if_device_exist.py
========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_if_device_exist.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_check_if_device_exist.py

check if a device tb.config.tc_workfd_check_if_device_exists_name exist

this tc returns always true, but sets

tb.config.tc_return True or False, because we may not

want to end testcase failed, if device not exists.


------------------------------------------------

.. _tc_workfd_check_if_dir_exist_py:

linux/tc_workfd_check_if_dir_exist.py
=====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_if_dir_exist.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_check_if_dir_exist.py

check if a dir in tbot workdir exist

this tc returns always true, but sets

tb.config.tc_return True or False, because we may not

want to end testcase failed, if dir not exists.


if tb.config.tc_workfd_check_if_dir_exists_create != 'no'

create the directory.



------------------------------------------------

.. _tc_workfd_check_if_file_exist_py:

linux/tc_workfd_check_if_file_exist.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_if_file_exist.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_check_if_file_exist.py

check if a file in tbot workdir exist


------------------------------------------------

.. _tc_workfd_check_tar_content_py:

linux/tc_workfd_check_tar_content.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_tar_content.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_check_tar_content.py

check if the strings in the tb.config.tc_workfd_check_tar_content_elements

list are in the tar file tb.config.tc_workfd_check_tar_content_path


tb.config.tc_workfd_check_tar_content_path path and file name

tb.config.tc_workfd_check_tar_content_elements list of elements in the tar file

tb.config.tc_workfd_check_tar_content_endtc_onerror end TC when element is not found


------------------------------------------------

.. _tc_workfd_check_tc_time_py:

linux/tc_workfd_check_tc_time.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_tc_time.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_check_tc_time.py

check if time for a special testcase is expired.

some testcases (like writting in a flash) are not good for

execute them every day, so give them a timeout. This testcase

checks, if the testcases is ready for a new run.

False means time is not expired

True means time is expired


------------------------------------------------

.. _tc_workfd_compile_linux_py:

linux/tc_workfd_compile_linux.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_compile_linux.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_compile_linux.py

compile linux:

- set toolchain with tc_lab_set_toolchain_py_

- if tb.config.tc_workfd_compile_linux_clean == 'yes'

call "make mrproper"

- tb.config.tc_workfd_compile_linux_load_addr != 'no'

add LOAD_ADDR=tb.config.tc_workfd_compile_linux_load_addr to make

- make tb.config.tc_workfd_compile_linux_boardname defconfig

- make tb.config.tc_workfd_compile_linux_makeoptions tb.config.tc_workfd_compile_linux_make_target

- if tb.config.tc_workfd_compile_linux_modules != 'none'

compile modules

- if tb.config.tc_workfd_compile_linux_dt_name != 'none'

compile DTB from list tb.config.tc_workfd_compile_linux_dt_name

- if tb.config.tc_workfd_compile_linux_fit_its_file != 'no'

create FIT image

mkimage path: tb.config.tc_workfd_compile_linux_mkimage

fit description file: tb.config.tc_workfd_compile_linux_fit_its_file

tb.config.tc_workfd_compile_linux_fit_file

- if tb.config.tc_workfd_compile_linux_append_dt != 'no'

append dtb to kernel image

tb.config.tc_workfd_compile_linux_boardname _defconfig


------------------------------------------------

.. _tc_workfd_connect_with_conmux_py:

linux/tc_workfd_connect_with_conmux.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_connect_with_conmux.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_connect_with_conmux.py

connect to console with conmux

Never tested !!!


------------------------------------------------

.. _tc_workfd_connect_with_kermit_py:

linux/tc_workfd_connect_with_kermit.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_connect_with_kermit.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_connect_with_kermit.py

connect with kermit to serials board console

- if tb.config.tc_workfd_connect_with_kermit_ssh != 'none'

connect first with ssh to another PC (where kermit is started)

- start kermit

- if tb.config.tc_workfd_connect_with_kermit_rlogin == 'none'

set line tb.config.kermit_line and speed tb.config.kermit_speed and

kermit parameter list tb.config.tc_workfd_connect_with_kermit_settings

than connect to serial line.

else

connect with command in tb.config.tc_workfd_connect_with_kermit_rlogin

- if you need sudo rights set tb.config.tc_workfd_connect_with_kermit_sudo = 'yes'

and a sudo is preceded to kermit.

the sudo password is searched with

user:  tb.config.user + '_kermit'

board: tb.config.boardname



------------------------------------------------

.. _tc_workfd_connect_with_ssh_py:

linux/tc_workfd_connect_with_ssh.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_connect_with_ssh.py


connect wit ssh to board, and use it as console



------------------------------------------------

.. _tc_workfd_cp_file_py:

linux/tc_workfd_cp_file.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_cp_file.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_cp_file.py

simple copy file from tb.tc_workfd_cp_file_a to tb.tc_workfd_cp_file_b


------------------------------------------------

.. _tc_workfd_create_ubi_rootfs_py:

linux/tc_workfd_create_ubi_rootfs.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_create_ubi_rootfs.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_create_ubi_rootfs.py

create a ubifs rootfs

ubi rootfs path: tb.config.tc_workfd_create_ubi_rootfs_path

ubi parameters:

tb.config.tc_ubi_min_io_size tb.config.tc_ubi_leb_size tb.config.tc_ubi_max_leb_cnt

output path: tb.config.tc_workfd_create_ubi_rootfs_target


------------------------------------------------

.. _tc_workfd_date_py:

linux/tc_workfd_date.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_date.py


just as a demo for the tbot workshop

simply show, how to send a cmd (in our case "date") to the

linux console on the DUT

(2 different possibilities)


Then send again "date" and search for the string

"Mon" in the output of the date command, and end Testcase

with True, if found, else end TC with False.


This testcase is a good starting point for writting

own testcases.


You also can use this testcase for a fast tbot

test after tbot is installed.

See config/tbot_test_py_ for more info



------------------------------------------------

.. _tc_workfd_disconnect_with_kermit_py:

linux/tc_workfd_disconnect_with_kermit.py
=========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_disconnect_with_kermit.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_connect_with_kermit.py

disconnect from a kermit connection


------------------------------------------------

.. _tc_workfd_generate_random_file_py:

linux/tc_workfd_generate_random_file.py
=======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_generate_random_file.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_generate_random_file.py

simple create a random file tb.tc_workfd_generate_random_file_name

with tb.tc_workfd_generate_random_file_length length.


------------------------------------------------

.. _tc_workfd_get_linux_source_py:

linux/tc_workfd_get_linux_source.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_get_linux_source.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_get_linux_source.py

get Linux source tb.config.tc_lab_get_linux_source_git_repo with "git clone"

and go into the source tree.

check out branch tc_lab_get_linux_source_git_branch if tc_lab_get_linux_source_git_commit_id == 'none'

else checkout commit tc_lab_get_linux_source_git_commit_id

Apply patches if needed with:

tc_lab_apply_patches_py_ and tc_workfd_apply_local_patches_py_


------------------------------------------------

.. _tc_workfd_get_list_of_files_in_dir_py:

linux/tc_workfd_get_list_of_files_in_dir.py
===========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_get_list_of_files_in_dir.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_get_list_of_files_in_dir.py

get a list of files from directory tb.tc_workfd_get_list_of_files_dir

tb.config.tc_workfd_get_list_of_files_mask


------------------------------------------------

.. _tc_workfd_get_patchwork_number_list_py:

linux/tc_workfd_get_patchwork_number_list.py
============================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_get_patchwork_number_list.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_get_patchwork_number_list.py

get a list of patchworknumbers

which are delegated to specific user

tb.config.workfd_get_patchwork_number_user

currently, this testcase reads "http://patchwork.ozlabs.org/project/uboot/list/"

and filters out the patches, which are for

tb.config.workfd_get_patchwork_number_user

It would be better to login and look for the users

ToDo list, but I did not find out, how to login ...

ignore patches on blacklist:

tb.config.tc_workfd_apply_patchwork_patches_blacklist

also you can set the patch order with:

tb.config.tc_workfd_get_patchwork_number_list_order


------------------------------------------------

.. _tc_workfd_get_uboot_config_hex_py:

linux/tc_workfd_get_uboot_config_hex.py
=======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_get_uboot_config_hex.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_get_uboot_config_hex.py

get a hex parameter from U-Boot configuration

Input:

tb.config.uboot_get_parameter_file_list: list of files, where TC searches

for the define

tb.uboot_config_option: config option which get searched


return value:

TC ends True, if hex value found, else False

tb.config_result: founded hex value, else 'undef'


------------------------------------------------

.. _tc_workfd_get_uboot_config_string_py:

linux/tc_workfd_get_uboot_config_string.py
==========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_get_uboot_config_string.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_get_uboot_config_string.py

get a string parameter from U-Boot configuration

Input:

tb.config.uboot_get_parameter_file_list: list of files, where TC searches

for the define

tb.uboot_config_option: config option which get searched


return value:

TC ends True, if string value found, else False

tb.config_result: founded string value, else 'undef'


------------------------------------------------

.. _tc_workfd_get_uboot_config_vars_py:

linux/tc_workfd_get_uboot_config_vars.py
========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_get_uboot_config_vars.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_get_uboot_config_vars.py


try to get some configuration variables from the U-Boot

source code, and save them in config variables.


'CONFIG_SYS_SDRAM_BASE' saved in tb.config.tc_ub_memory_ram_ws_base

tb.config.tc_ub_memory_ram_ws_base_alt = tc_ub_memory_ram_ws_base + 0x100000

tb.config.tc_ub_memory_ram_big depended on CONFIG_SYS_ARCH

if CONFIG_SYS_ARCH == powerpc than yes else no



------------------------------------------------

.. _tc_workfd_git_rebase_py:

linux/tc_workfd_git_rebase.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_git_rebase.py


go into git source tree tb.config.tc_workfd_git_rebase_git_src_path

checkout branch tb.config.tc_workfd_git_rebase_git_base_branch

call "git fetch" and "git pull"

checkout branch tb.config.tc_workfd_git_rebase_git_work_branch

and rebase tb.config.tc_workfd_git_rebase_git_work_branch with

tb.config.tc_workfd_git_rebase_git_base_branch



------------------------------------------------

.. _tc_workfd_goto_lab_source_dir_py:

linux/tc_workfd_goto_lab_source_dir.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_goto_lab_source_dir.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_goto_lab_source_dir.py

switch into lab PC source directory tb.config.tc_lab_source_dir

set TBOT_BASEDIR to tb.config.tc_lab_source_dir


------------------------------------------------

.. _tc_workfd_goto_linux_code_py:

linux/tc_workfd_goto_linux_code.py
==================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_goto_linux_code.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_goto_linux_code.py

switch into linux source tb.config.tc_lab_source_dir + "/linux-" + tb.config.boardlabname

set tb.config.linux_name to "linux-" + tb.config.boardlabname

and tb.config.linux_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.linux_name

and set $TBOT_BASEDIR_LINUX to tb.config.linux_fulldir_name


------------------------------------------------

.. _tc_workfd_goto_tbot_workdir_py:

linux/tc_workfd_goto_tbot_workdir.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_goto_tbot_workdir.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_goto_tbot_workdir.py

go into the tbot work dir tb.config.tc_workfd_work_dir

if not exist, create it


------------------------------------------------

.. _tc_workfd_goto_uboot_code_py:

linux/tc_workfd_goto_uboot_code.py
==================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_goto_uboot_code.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_goto_uboot_code.py

switch into U-Boot source tb.config.tc_lab_source_dir + "/u-boot-" + tb.config.boardlabname

set tb.config.uboot_name to "u-boot-" + tb.config.boardlabname

and tb.config.uboot_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.uboot_name

and set $TBOT_BASEDIR_UBOOT to tb.config.uboot_fulldir_name



------------------------------------------------

.. _tc_workfd_grep_py:

linux/tc_workfd_grep.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_grep.py


search string tb.tc_workfd_grep_string in file tb.tc_workfd_grep_file

grep options configurable through tb.config.tc_workfd_grep_option

default '--color=never'



------------------------------------------------

.. _tc_workfd_hdparm_py:

linux/tc_workfd_hdparm.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_hdparm.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_hdparm.py

make a minimal hdparm check

call hdparm -t tb.config.tc_workfd_hdparm_dev

and check if read speed is greater than tb.config.tc_workfd_hdparm_min

It is possible to add a PATH tb.config.tc_workfd_hdparm_path

where hdparm is installed

Testcase fails if readen speed is <= tb.config.tc_workfd_hdparm_min


------------------------------------------------

.. _tc_workfd_insmod_py:

linux/tc_workfd_insmod.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_insmod.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_insmod.py

insmod module tb.tc_workfd_insmod_module with

module path tb.tc_workfd_insmod_mpath and

tb.tc_workfd_insmod_module_path

check if the strings in list tb.tc_workfd_insmod_module_checks

come back when inserting the module.


------------------------------------------------

.. _tc_workfd_iperf_py:

linux/tc_workfd_iperf.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_iperf.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_iperf.py


make a minimal iperf check

starts an iperf server on tb.tc_workfd_c_sr connection

with ip addr tb.tc_workfd_iperf_sip

starts an iperf "slave" on tb.tc_workfd_c_sl

waiting for the first result of iperf measure and

check if the resulting speed is bigger then

tb.config.tc_workfd_iperf_minval


if you have not the iperf cmd instead iperf 3, you can

set

tb.config.tc_workfd_c_sr_vers or tb.config.tc_workfd_c_sl_vers

to '3'


------------------------------------------------

.. _tc_workfd_linux_get_ifconfig_py:

linux/tc_workfd_linux_get_ifconfig.py
=====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_linux_get_ifconfig.py

start with

tbot.py -s lab_denx -c boardname -t tc_workfd_linux_get_ifconfig.py

read from tb.config.linux_get_ifconfig_dev the current

ip addr and save it in tb.config.linux_get_ifconfig_ip

broadcast and save it in tb.config.linux_get_ifconfig_broadcast

mask and save it in tb.config.linux_get_ifconfig_mask


------------------------------------------------

.. _tc_workfd_linux_get_uboot_env_py:

linux/tc_workfd_linux_get_uboot_env.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_linux_get_uboot_env.py

start with

tbot.py -s lab_denx -c boardname -t tc_workfd_linux_get_uboot_env.py

read U-Boot Environment variable from tb.config.linux_get_uboot_env_name

from linux with fw_printenv, and save the value in tb.config.linux_get_uboot_env_value


------------------------------------------------

.. _tc_workfd_linux_mkdir_py:

linux/tc_workfd_linux_mkdir.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_linux_mkdir.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_linux_mkdir.py

check if the directory tb.config.tc_workfd_linux_mkdir_dir exists.

if not, create it


------------------------------------------------

.. _tc_workfd_lx_get_bc_py:

linux/tc_workfd_lx_get_bc.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_lx_get_bc.py

get in linux bootcount value

if not found testcases end with failure

value returned in var tb.lx_bc


------------------------------------------------

.. _tc_workfd_lx_set_bc_py:

linux/tc_workfd_lx_set_bc.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_lx_set_bc.py

set in linux bootcount value tb.lx_bc


------------------------------------------------

.. _tc_workfd_md5sum_py:

linux/tc_workfd_md5sum.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_md5sum.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_md5sum.py

calculate md5sum of file tb.tc_workfd_md5sum_name , and store it in

tb.tc_workfd_md5sum_sum


------------------------------------------------

.. _tc_workfd_rm_dir_py:

linux/tc_workfd_rm_dir.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_rm_dir.py


remove the path tb.config.tc_lab_rm_dir



------------------------------------------------

.. _tc_workfd_rm_file_py:

linux/tc_workfd_rm_file.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_rm_file.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_rm_file.py

simple rm directory tb.config.tc_workfd_rm_file_name on the lab


------------------------------------------------

.. _tc_workfd_rm_linux_code_py:

linux/tc_workfd_rm_linux_code.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_rm_linux_code.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_rm_linux_code.py

rm linux source tb.config.tc_lab_source_dir + '/linux-' + tb.config.boardlabname


------------------------------------------------

.. _tc_workfd_rm_uboot_code_py:

linux/tc_workfd_rm_uboot_code.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_rm_uboot_code.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_rm_uboot_code.py

rm U-Boot source tb.config.tc_lab_source_dir + '/u-boot-' + tb.config.boardlabname


------------------------------------------------

.. _tc_workfd_scp_py:

linux/tc_workfd_scp.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_scp.py

start with

python2.7 src/common/tbot.py -s lab_denx -c exceet -t tc_workfd_scp.py


start an scp transfer

tb.config.tc_workfd_scp_opt: scp options

tb.config.tc_workfd_scp_from: from where

tb.config.tc_workfd_scp_to: to where


If the scp command asks for  "password" the testcase extracts

the user and ip from scp output "user@ip's password:"

and writes the password it find in password_py_ with


tb.write_stream_passwd(tb.workfd, user, ip)


to the scp command ... if no user and or ip

is found ... scp command fails and so the testcase.


An errorneous scp command exits with an error code.

check this error code when scp command finished,

and return True, if no error, else False.



------------------------------------------------

.. _tc_workfd_set_gpio_py:

linux/tc_workfd_set_gpio.py
===========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_set_gpio.py

Sets a GPIO through sysfs gpio high/low


Call like this:

tb.eof_call_tc("tc_workfd_set_gpio_py_", highlow='high', gpio=gpioname)



------------------------------------------------

.. _tc_workfd_ssh_py:

linux/tc_workfd_ssh.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_ssh.py


login with ssh to tb.config.workfd_ssh_cmd and ssh options

tb.config.tc_workfd_ssh_opt.

This testcases expects

tb.config.workfd_ssh_cmd_prompt

as the prompt it get, after a succefull log in.

When logged in call

if tb.config.workfd_ssh_do_first == 'yes':

tb.do_first_settings_after_login(c)



------------------------------------------------

.. _tc_workfd_sudo_cp_file_py:

linux/tc_workfd_sudo_cp_file.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_sudo_cp_file.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_sudo_cp_file.py

simple copy file from tb.tc_workfd_cp_file_a to tb.tc_workfd_cp_file_b

with sudo rights


------------------------------------------------

.. _tc_workfd_switch_su_py:

linux/tc_workfd_switch_su.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_switch_su.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_switch_su.py

switch to superuser


------------------------------------------------


.. _Directory_uboot:

***************
Directory uboot
***************

.. _duts:

Directory uboot/duts
====================

.. _tc_ub_basic_py:

uboot/duts/tc_ub_basic.py
,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_basic.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_basic.py

convert duts tests from:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/02_UBootBasic.tc;h=5503cc6c716d2748732d30d63b0801e651fe1706;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_bdinfo_py:

uboot/duts/tc_ub_bdinfo.py
,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_bdinfo.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_bdinfo.py

convert duts tests from:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootBdinfo.tc;h=aa794a93ac5c8d2c3aea4aa5d02433ca2ee0f010;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_boot_py:

uboot/duts/tc_ub_boot.py
,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_boot.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_boot.py

convert duts tests from:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootBoot.tc;h=f679ff09cdb1e1393829c32dc5aa5cf299e9af07;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_coninfo_py:

uboot/duts/tc_ub_coninfo.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_coninfo.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_coninfo.py

convert duts tests from:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootConinfo.tc;h=2d028f74ba791343b8a70a97885eabe8b5944017;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_date_py:

uboot/duts/tc_ub_date.py
,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_date.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_date.py

convert duts tests from:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootDate.tc;h=03b7d53fd93bd61381db4095a4bff58b1d1efff7;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_download_py:

uboot/duts/tc_ub_download.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_download.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_download.py

convert duts tests from:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootCmdGroupDownload.tc;h=8e58d53add90b680ef7a1300894d2392f90d9824;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_dtt_py:

uboot/duts/tc_ub_dtt.py
,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_dtt.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_dtt.py

convert duts tests from:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootDtt.tc;h=e420c7b45cd73b00465d69f969039222868f4cc7;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_duts_fdt_py:

uboot/duts/tc_ub_duts_fdt.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_duts_fdt.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_duts_fdt.py


create logfiles used for DULG

http://www.denx.de/wiki/view/DULG/UBootCmdFDT



------------------------------------------------

.. _tc_ub_duts_go_py:

uboot/duts/tc_ub_duts_go.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_duts_go.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_duts_go.py

do the commands needed for:

http://www.denx.de/wiki/view/DULG/UBootCmdGroupExecSection_5.9.4.3.

U-Boots go command



------------------------------------------------

.. _tc_ub_duts_hush_py:

uboot/duts/tc_ub_duts_hush.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_duts_hush.py


create the logfiles needed for the U-Boot documentation

used in src/documentation/u-boot-script.rst


based on the DULG chapter:

http://www.denx.de/wiki/view/DULG/CommandLineParsing



------------------------------------------------

.. _tc_ub_duts_source_py:

uboot/duts/tc_ub_duts_source.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_duts_source.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_duts_source.py

do the commands needed for:

http://www.denx.de/wiki/view/DULG/UBootCmdGroupExecSection_5.9.4.1.

U-Boots source command



------------------------------------------------

.. _tc_ub_duts_version_py:

uboot/duts/tc_ub_duts_version.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_duts_version.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_duts_version.py


execute U-Boots "version" cmd, and create event

DUTS_UBOOT_VERSION

DUTS_SPL_VERSION

DUTS_BOARDNAME = tb.config.boardlabpowername



------------------------------------------------

.. _tc_ub_environment_py:

uboot/duts/tc_ub_environment.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_environment.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_environment.py

convert duts tests from:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootEnvironment.tc;h=18d235f427e3efe9e6a04f870a3c5426d719ec58;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_flinfo_py:

uboot/duts/tc_ub_flinfo.py
,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_flinfo.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_flinfo.py

convert duts tests from:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootFlinfo.tc;h=f5b728258250211d86dc9c6a9208639d8542b845;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_i2c_help_py:

uboot/duts/tc_ub_i2c_help.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_i2c_help.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_i2c_help.py

simple prints "help i2c" cmd


------------------------------------------------

.. _tc_ub_memory_py:

uboot/duts/tc_ub_memory.py
,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_memory.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_memory.py

convert duts tests from:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootMemory.tc;h=f5fb055499db17c322859215ab489cefb063ac47;hb=101ddd5dbd547d5046363358d560149d873b238a


disable "base" only command with

tb.config.tc_ub_memory_base = 'no'

default: 'yes'


------------------------------------------------

.. _tc_ub_run_py:

uboot/duts/tc_ub_run.py
,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_run.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_run.py

convert duts tests from:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootRun.tc;h=44f8a0a0de256afdd95b5ec20d1d4570373aeb7d;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_start_all_duts_py:

uboot/duts/tc_ub_start_all_duts.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_start_all_duts.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_start_all_duts.py

start all DUTS tests


only start the DUTS testcases, if tb.config.tc_ub_start_all_duts_start

is set to True (default)



------------------------------------------------


.. _tc_ub_aristainetos2_ubi_py:

uboot/tc_ub_aristainetos2_ubi.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_aristainetos2_ubi.py

start with

tbot.py -s lab_denx -c aristainetos2 -t tc_ub_aristainetos2_ubi.py

ubi testcases for the aristainetos2 board


------------------------------------------------

.. _tc_ub_check_reg_file_py:

uboot/tc_ub_check_reg_file.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_check_reg_file.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_check_reg_file.py

checks if the default values in reg file tb.config.tc_ub_create_reg_file_name

on the tbot host in tb.workdir have the same values, as the

registers on the board

format of the regfile:

regaddr mask type defval

ToDo: use the file from the lab host, not the tbot host


------------------------------------------------

.. _tc_ub_check_version_py:

uboot/tc_ub_check_version.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_check_version.py


check if the current running U-Boot vers == tb.uboot_vers

and SPL vers == tb.spl_vers



------------------------------------------------

.. _tc_ub_cmp_py:

uboot/tc_ub_cmp.py
==================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_cmp.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_cmp.py

- compare 2 the contents of tb.tc_ub_cmp_addr1 with tb.tc_ub_cmp_addr2

bytes tb.tc_ub_cmp_len length


------------------------------------------------

.. _tc_ub_create_am335x_reg_file_py:

uboot/tc_ub_create_am335x_reg_file.py
=====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_create_am335x_reg_file.py

start with

python2.7 src/common/tbot.py -s lab_denx -s labconfigname -c boardconfigname -t tc_ub_create_am335x_reg_file.py


creates U-Boot register dump files for an am335x based board.

using testcase tc_ub_create_reg_file_py_


dumps:

- pinmux  44e10000 - 44e10004

- pinmux  44e10010 - 44e10010 

- pinmux  44e10040 - 44e10040

- pinmux  44e10110 - 44e10110

- pinmux  44e10428 - 44e11440

- cm per  44e00000 - 44e00150

- cm wkup 44e00400 - 44e004d0

- cm dpll 44e00500 - 44e0053c

- cm mpu  44e00600 - 44e00604

- cm device 44e00700 - 44e00700

- emif    4c000000 - 4c000120

- ddr     44e12000 - 44e121dc


into files found in src/files/

create for your board a subdir in the directory,

and move the new created files into it, so you have

them as a base for comparing further use.



------------------------------------------------

.. _tc_ub_create_imx28_reg_file_py:

uboot/tc_ub_create_imx28_reg_file.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_create_imx28_reg_file.py

start with

python2.7 src/common/tbot.py -s lab_denx -s labconfigname -c boardconfigname -t tc_ub_create_imx28_reg_file.py


creates U-Boot register dump files for an imx28 based board.

using testcase tc_ub_create_reg_file_py_


dumps:

- pinmux  80018000 - 80018b40

- clkctrl 80044000 - 80044170

- emi     800e0000 - 800e02ec

- gpmi    8000c000 - 8000c0d4

- enet 0  800f0000 - 800f0684

- enet 1  800f4000 - 800f4684


into files found in src/files/

create for your board a subdir in the directory,

and move the new created files into it, so you have

them as a base for comparing further use.



------------------------------------------------

.. _tc_ub_create_imx6_reg_file_py:

uboot/tc_ub_create_imx6_reg_file.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_create_imx6_reg_file.py

start with

python2.7 src/common/tbot.py -s lab_denx -s labconfigname -c boardconfigname -t tc_ub_create_imx6_reg_file.py


creates U-Boot register dump files for an imx6 based board.

using testcase tc_ub_create_reg_file_py_


dumps:

- pinmux  20e0000 - 20e0950


into files found in src/files/

create for your board a subdir in the directory,

and move the new created files into it, so you have

them as a base for comparing further use.



------------------------------------------------

.. _tc_ub_create_reg_file_py:

uboot/tc_ub_create_reg_file.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_create_reg_file.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_create_reg_file.py

creates a reg file tb.tc_ub_create_reg_file_name on the tbot host

in tb.workdir

read from tb.tc_ub_create_reg_file_start to tb.tc_ub_create_reg_file_stop

and writes the results in the regfile tb.tc_ub_create_reg_file_name

format of the regfile:

regaddr mask type defval

This reg file can be used as a default file, how the

registers must be setup, check it with testcase

tc_ub_check_reg_file_py_

ToDo: use the file from the lab host, not the tbot host


------------------------------------------------

.. _tc_ub_dfu_py:

uboot/tc_ub_dfu.py
==================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_dfu.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_dfu.py

test dfu

- use dfu-util in tb.config.tc_ub_dfu_dfu_util_path

- upload file tb.config.tc_ub_dfu_dfu_util_alt_setting to

tb.config.tc_ub_dfu_dfu_util_downloadfile

- download it back to the board

- upload it again

- and compare the two files


------------------------------------------------

.. _tc_ub_dfu_random_py:

uboot/tc_ub_dfu_random.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_dfu_random.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_dfu_random.py

test a U-Boot dfu alt setting tb.config.tc_ub_dfu_dfu_util_alt_setting

Therefore write a random file with size tb.config.tc_ub_dfu_rand_size

to it, reread it and compare it. TC fails if files differ

(If readen file is longer, this is no error!)


If dfu-util is not installed on the lab PC, set

tb.config.tc_ub_dfu_dfu_util_ssh for connecting with ssh to a PC

which have it installed, and a USB cable connected to the board.

Set tb.config.tc_ub_dfu_dfu_util_path to the path of dfu-util, if

you have a self compiled version of it.

Set tb.config.tc_ub_dfu_rand_ubcmd for the executed command on

U-Boot shell for getting into DFU mode


------------------------------------------------

.. _tc_ub_dfu_random_default_py:

uboot/tc_ub_dfu_random_default.py
=================================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_dfu_random_default.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_dfu_random_default.py

test a U-Boot dfu alt setting tb.config.tc_ub_dfu_dfu_util_alt_setting

with reading / writing different sizes


------------------------------------------------

.. _tc_ub_get_bc_py:

uboot/tc_ub_get_bc.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_get_bc.py

get in uboot bootcount value

if not found testcases end with failure

value returned in var tb.ub_bc


------------------------------------------------

.. _tc_ub_get_filesize_py:

uboot/tc_ub_get_filesize.py
===========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_get_filesize.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_get_filesize.py

simple get the content of U-Boot env variable filesize

and store it in tb.ub_filesize


------------------------------------------------

.. _tc_ub_get_version_py:

uboot/tc_ub_get_version.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_get_version.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_get_version.py

get the U-Boot and/or SPL version from a binary

and save it in tb.uboot_vers or tb.spl_vers


------------------------------------------------

.. _tc_ub_help_py:

uboot/tc_ub_help.py
===================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_help.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_help.py

- test U-Boots help cmd

may we add a list as parameter, so we can adapt it board

specific.


------------------------------------------------

.. _tc_ub_load_board_env_py:

uboot/tc_ub_load_board_env.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_load_board_env.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_load_board_env.py


task: load U-Boot Environment env.txt file with tftp for the

board tb.config.tftpboardname to the addr tb.config.ub_load_board_env_addr

from subdir tb.config.ub_load_board_env_subdir

and imports the the textfile with 'env import'


options:

if tb.config.tc_ub_boot_linux_load_env == 'no' than TC does nothing


if tb.config.tc_ub_boot_linux_load_env == 'set' or == 'setend'

than TC executes the cmds in list tb.config.ub_load_board_env_set


if tb.config.tc_ub_boot_linux_load_env == 'setend' TC returns

after executing the commands with True


else TC executes the steps described in 'task'


tb.config.ub_load_board_env_testcase != ''

call a board specific testcase, whichs name is defined in

tb.config.ub_load_board_env_testcase for setting U-Boot

Env. If this testcase succeeds, end True.


------------------------------------------------

.. _tc_ub_reset_py:

uboot/tc_ub_reset.py
====================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_reset.py


simply call U-Boots reset command

This testcase works only on the console connection c_con



------------------------------------------------

.. _tc_ub_setenv_py:

uboot/tc_ub_setenv.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_setenv.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_setenv.py

set U-Boot Environmentvariable tb.config.setenv_name with value

tb.config.setenv_value


------------------------------------------------

.. _tc_ub_setenv_fkt_py:

uboot/tc_ub_setenv_fkt.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_setenv_fkt.py

start with

python2.7 src/common/tbot.py -s lab_denx -c beagleboneblack -t tc_ub_setenv_fkt.py

set U-Boot Environmentvariable tb.config.setenv_name with value

tb.config.setenv_value


This is for demonstration how to use functions in tbot only.

So, this testcase sets 3 times the U-Boot Envvariable:

- The new way with importing the functions from testcase

src/tc/uboot/tc_ub_testfkt_py_

- The oldstyled way with calling the testcase tc_ub_testfkt_py_

with tb.eof_call_tc()

- The oldstyled way with calling the testcase tc_ub_testfkt_py_

with tb.call_tc() and getting the return value.


------------------------------------------------

.. _tc_ub_test_py_py:

uboot/tc_ub_test_py.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_test_py.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_test_py.py

call test/py from u-boot source

- disconnect console

- call test/py

- connect back to console

test/py hookscript directory:

tb.config.tc_ub_test_py_hook_script_path


you can disable this testcase with tb.config.tc_ub_test_py_start = 'no'


may a configure file is needed, so create it with

tb.config.tc_ub_test_py_configfile. This variable contains

the config file, which gets created.



------------------------------------------------

.. _tc_ub_testfkt_py:

uboot/tc_ub_testfkt.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_testfkt.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_testfkt.py


This testcase is for demonstration of using functions in

testcases, and use them from other testcases.


testcase which calls this function for demo:

src/tc/uboot/tc_ub_setenv_fkt_py_


defines 2 functions:

- ub_setenv(tb, c, name, val)

set Environment variable name with value val

- ub_checkenv(tb, c, name, val)

checks, if U-Boot Environmentvariable name

has the value val.


there are 2 ways from calling this testcase directly

from the cmdline:


- with arguments:

tbot.py -s lab_denx -c beagleboneblack -t tc_ub_testfkt.py -a "Heiko Schochernew"


name = tb.arguments.split()[0]

val = tb.arguments.split()[1]


- without arguments:

tbot.py -s lab_denx -c beagleboneblack -t tc_ub_testfkt.py


in this case 

name = tb.config.setenv_name

val = tb.config.setenv_value



------------------------------------------------

.. _tc_ub_tftp_file_py:

uboot/tc_ub_tftp_file.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_tftp_file.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_tftp_file.py

load file tb.config.tc_ub_tftp_file_name to tb.config.tc_ub_tftp_file_addr

with tftp command in uboot


------------------------------------------------

.. _tc_ub_ubi_check_volume_py:

uboot/tc_ub_ubi_check_volume.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_check_volume.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_check_volume.py

- checks if ubi volume tb.config.tc_ub_ubi_load_name exists


------------------------------------------------

.. _tc_ub_ubi_create_volume_py:

uboot/tc_ub_ubi_create_volume.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_create_volume.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_create_volume.py

- create ubi volume tb.config.tc_ub_ubi_create_vol_name with size

tb.config.tc_ub_ubi_create_vol_sz


------------------------------------------------

.. _tc_ub_ubi_erase_py:

uboot/tc_ub_ubi_erase.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_erase.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_erase.py

- erase an ubi device

execute U-Boot Env tbot_ubi_erase


------------------------------------------------

.. _tc_ub_ubi_info_py:

uboot/tc_ub_ubi_info.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_info.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_info.py

- simple print ubi info


------------------------------------------------

.. _tc_ub_ubi_prepare_py:

uboot/tc_ub_ubi_prepare.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_prepare.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_prepare.py

- ubi prepare

execute "ubi part" ith tb.config.tc_ub_ubi_prep_partname

if tb.config.tc_ub_ubi_prep_offset != 'none'

with offset tb.config.tc_ub_ubi_prep_offset


------------------------------------------------

.. _tc_ub_ubi_read_py:

uboot/tc_ub_ubi_read.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_read.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_read.py

- read ubi volume tb.config.tc_ub_ubi_prep_offset to tb.tc_ub_ubi_read_addr

with len tb.tc_ub_ubi_read_len


------------------------------------------------

.. _tc_ub_ubi_write_py:

uboot/tc_ub_ubi_write.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_write.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubi_write.py

- write image @ tb.config.tc_ub_ubi_write_addr to ubi volume

tb.config.tc_ub_ubi_write_vol_name with len tb.config.tc_ub_ubi_write_len


------------------------------------------------

.. _tc_ub_ubifs_ls_py:

uboot/tc_ub_ubifs_ls.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubifs_ls.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubifs_ls.py

- ls ubifs tb.config.tc_ub_ubifs_ls_dir


------------------------------------------------

.. _tc_ub_ubifs_mount_py:

uboot/tc_ub_ubifs_mount.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubifs_mount.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_ubifs_mount.py

- mount ubifs tb.config.tc_ub_ubifs_volume_name


------------------------------------------------

.. _tc_ub_upd_spl_py:

uboot/tc_ub_upd_spl.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_upd_spl.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_upd_spl.py

update new spl to board if tb.config.tc_ub_upd_spl_withspl == 'yes'


steps:

- load tbot u-boot env vars

- execute "run tbot_upd_spl"

- execute "run tbot_cmp_spl"

- reset board

- get u-boot


------------------------------------------------

.. _tc_ub_upd_uboot_py:

uboot/tc_ub_upd_uboot.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_upd_uboot.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_upd_uboot.py

update new uboot to board

steps:

- load tbot u-boot env vars

- execute "run tbot_upd_uboot"

- execute "run tbot_cmp_uboot"

- reset board

- get u-boot


------------------------------------------------

.. _tc_uboot_check_kconfig_py:

uboot/tc_uboot_check_kconfig.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_check_kconfig.py

start with

python2.7 src/common/tbot.py -s lab_denx -c uboot_kconfig_check -t tc_uboot_check_kconfig.py


check for all boards, if a patch changes the u-boot binary

If U-boot binary changed by the patch this testcase fails.

use this testcase, if you for example move a config option

into Kconfig. As we need reproducable builds, we need to

patch U-Boot with tb.config.tc_uboot_check_kconfig_preparepatch

find this patch here: src/files/ub-patches/0001-U-Boot-version-fix.patch

copy it to the lab pc and adapt tb.config.tc_uboot_check_kconfig_preparepatch


Steps from this testcase:

- rm U-Boot code with tc_workfd_rm_uboot_code_py_

- get U-Boot code with tc_lab_get_uboot_source_py_

- set SOURCE_DATE_EPOCH=0 to get reproducible builds

- apply patch from tb.config.tc_uboot_check_kconfig_preparepatch

get rid of local version ToDo: find a way to disable CONFIG_LOCALVERSION_AUTO

so this patch is not longer needed.

- if tb.config.tc_uboot_check_kconfig_read_sumfile is != 'none'

read a list of boards and md5sums from the file in

tb.config.tc_uboot_check_kconfig_read_sumfile

else

- create a list of boards (all defconfigs)

- do for all boards:

- get architecture and set toolchain

- compile U-Boot and calculate md5sum

with tc_workfd_compile_uboot_py_ and tc_workfd_md5sum_py_

- if tb.config.tc_uboot_check_kconfig_create_sumfile != 'none'

save the board md5sum lists in the file

tb.config.tc_uboot_check_kconfig_create_sumfile

you can use this now as a reference, so no need

to calculate always for all boards the md5sums

-> saves a lot of time!


- apply patch(es) with tc_workfd_apply_patches_py_

- do for all boards:

- compile U-Boot again (patched version)

- calculate md5sum again

- calculate md5sums

- check if they are the same


------------------------------------------------

.. _tc_uboot_ext2load_py:

uboot/tc_uboot_ext2load.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_ext2load.py

start with

python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_uboot_ext2load.py


load a file from ext2 into ram with ext2ls cmd.

check if the file has crc32 checksum 0x2144df1c


How to create such a file, which has crc32 checksum of 0x2144df1c ?


$ dd if=/dev/urandom of=test.bin bs=1M count=1

$ crc32 test.bin

4f3fef33

$ perl -e 'print pack "H\*", "33ef3f4f"' >> test.bin

$ crc32 test.bin

2144df1c


https://stackoverflow.com/questions/28591991/crc32-of-already-crc32-treated-data-with-the-crc-data-appended


!! Don;t forget Big into little endian conversion


used vars:

tc_uboot_ext2load_interface = 'usb'

tc_uboot_ext2load_dev = '0:1'

tc_uboot_ext2load_addr = '10000000'

tc_uboot_ext2load_file = '/test.bin'

tc_uboot_ext2load_check = 'no'

if 'yes' check if the file tc_uboot_ext2load_file

has the checksum 0x2144df1c


------------------------------------------------

.. _tc_uboot_ext2ls_py:

uboot/tc_uboot_ext2ls.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_ext2ls.py

start with

python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_uboot_ext2ls.py


simply call ext2ls


used vars:

tb.config.tc_uboot_ext2ls_expect = ['lost+found']

strings we expect from the ext2ls command

tb.config.tc_uboot_ext2ls_interface = 'usb'

tb.config.tc_uboot_ext2ls_dev = '0:1'

tb.config.tc_uboot_ext2ls_dir = '/'


------------------------------------------------

.. _tc_uboot_get_arch_py:

uboot/tc_uboot_get_arch.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_get_arch.py

start with

python2.7 src/common/tbot.py -c config/tbot_dxr2_uboot_kconfig_check.cfg -t tc_uboot_get_arch.py

get architecture from u-boot config


------------------------------------------------

.. _tc_uboot_load_bin_with_kermit_py:

uboot/tc_uboot_load_bin_with_kermit.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_load_bin_with_kermit.py

start with

tbot.py -c -s lab_denx -c nero -t tc_uboot_load_bin_with_kermit.py

start tc:

load binary into ram with loadb


if tb.config.tc_uboot_load_bin_with_kermit_possible != 'yes'

do nothing return True

default: 'yes'


precondition:

kermit must be used


steps:

- loadb tb.config.tc_uboot_load_bin_ram_addr

- leave kermit

- send tb.config.tc_uboot_load_bin_file

protocol: kermit_protocol='kermit'

wait for "C-Kermit>"

connect

you must get back something like this:

Total Size      = 0x00050bc0 = 330688 Bytes

Start Addr      = 0x81000000


------------------------------------------------

.. _tc_uboot_usb_info_py:

uboot/tc_uboot_usb_info.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_usb_info.py

start with

python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_uboot_usb_info.py


call "usb info" command


used vars:

tb.config.tc_uboot_usb_info_expect = ['Hub,  USB Revision 2.0',

'Mass Storage,  USB Revision 2.0']


------------------------------------------------

.. _tc_uboot_usb_start_py:

uboot/tc_uboot_usb_start.py
===========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_usb_start.py

start with

python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_uboot_usb_start.py


call "usb start" command


used vars:

tb.config.tc_uboot_usb_start_expect = ['Storage Device(s) found']


------------------------------------------------


.. _Directory_yocto:

***************
Directory yocto
***************

.. _tc_workfd_bitbake_py:

yocto/tc_workfd_bitbake.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_bitbake.py


simple call bitbake with tb.config.tc_workfd_bitbake_args


if tb.config.tc_workfd_bitbake_machine is set, also cat

the content of the newest file in tmp/log/cooker/" + tb.config.tc_workfd_bitbake_machine + "/\*


------------------------------------------------

.. _tc_workfd_check_repo_cmd_py:

yocto/tc_workfd_check_repo_cmd.py
=================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_check_repo_cmd.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_check_repo_cmd.py


check if repo cmd exists, if not try to set

PATH variable stored in tb.config.tc_workfd_repo_path



------------------------------------------------

.. _tc_workfd_get_with_repo_py:

yocto/tc_workfd_get_with_repo.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_get_with_repo.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_get_with_repo.py


get yocto code with repo tool and configure sources


- check if repo command exists

if not try to set path to it, if tb.config.tc_workfd_repo_path

is set, else failure


- goto repo code

if dir $TBOT_BASEDIR_REPO does not exist create it

- call "repo init" with variables

tb.config.tc_workfd_get_with_repo_u

tb.config.tc_workfd_get_with_repo_m

tb.config.tc_workfd_get_with_repo_b


- get newest sources with "repo sync"


- setup environment with samples from meta-

tb.config.tc_workfd_get_with_repo_metaname

default: 'beld'


- check if build directory "build_" + tb.config.tc_workfd_bitbake_machine

exists, if not create it and set DL_DIR and SSTATE_DIR in local.conf

with the values from tb.config.tc_workfd_get_yocto_source_conf_dl_dir

and tb.config.tc_workfd_get_yocto_source_conf_sstate_dir


and setup site.conf with specific settings



------------------------------------------------

.. _tc_workfd_get_yocto_source_py:

yocto/tc_workfd_get_yocto_source.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_get_yocto_source.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_get_yocto_source.py

get yocto source tb.config.tc_workfd_get_yocto_patches_git_repo with "git clone"

check out branch:

tb.config.tc_workfd_get_yocto_patches_git_branch

check out commit ID:

tb.config.tc_workfd_get_yocto_git_commit_id


if tb.config.tc_workfd_get_yocto_patches_git_repo != 'none'

apply patches with "git am" from directory:

tb.config.tc_workfd_get_yocto_clone_apply_patches_git_am_dir


additionally define a reference for cloning:

tb.config.tc_workfd_get_yocto_source_git_reference

if a user/password for cloning is needed, define the user:

tb.config.tc_workfd_get_yocto_source_git_repo_user

and set the password in password_py_


get other layers defined in the list:

tb.config.tc_workfd_get_yocto_source_layers

one element contains the follwoing list element:

['git repo',

'git branch',

'git commit id',

'apply_patches_dir'

'apply_patches_git_am_dir',

'source_git_reference',

'source_git_repo_user',

'source_git_repo_name'

]


if tb.config.tc_workfd_get_yocto_source_autoconf == 'none'

overwrite yocto configuration found in

tb.config.tc_workfd_get_yocto_source_conf_dir

else

try to autogenerate bblayers.conf and site.conf


clones into directory tb.config.yocto_name

created with tc_workfd_goto_yocto_code_py_



------------------------------------------------

.. _tc_workfd_goto_repo_code_py:

yocto/tc_workfd_goto_repo_code.py
=================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_goto_repo_code.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_goto_repo_code.py


switch into yocto source tb.config.tc_lab_source_dir + "/repo-" + tb.config.boardlabname


set tb.config.repo_name to "repo-" + tb.config.boardlabname

and tb.config.repo_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.repo_name

and set $TBOT_BASEDIR_REPO to tb.config.repo_fulldir_name



------------------------------------------------

.. _tc_workfd_goto_yocto_code_py:

yocto/tc_workfd_goto_yocto_code.py
==================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_goto_yocto_code.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_goto_yocto_code.py

switch into yocto source tb.config.tc_lab_source_dir + "/yocto-" + tb.config.boardlabname

set tb.config.yocto_name to "yocto-" + tb.config.boardlabname

and tb.config.yocto_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.yocto_name

and set $TBOT_BASEDIR_YOCTO to tb.config.yocto_fulldir_name


------------------------------------------------

.. _tc_workfd_yocto_basic_check_py:

yocto/tc_workfd_yocto_basic_check.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_yocto_basic_check.py

start with

tbot.py -s lab_denx -c boardname -t tc_workfd_yocto_basic_check.py


do basic yocto checks


- check rootfs version

only if tb.config.tc_workfd_yocto_basic_check_rootfsversion == 'yes'

which is the default.

- check dmesg output

check if strings defined in tb.config.tc_demo_yocto_test_checks

are found in dmesg output

- check if devmem2 tool is in rootfs, if so, do register checks



------------------------------------------------

.. _tc_workfd_yocto_check_rootfs_version_py:

yocto/tc_workfd_yocto_check_rootfs_version.py
=============================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_yocto_check_rootfs_version.py

start with

tbot.py -s lab_denx -c boardname -t tc_workfd_yocto_check_rootfs_version.py


check if the current /etc/version on the target rootfs is the

same as in tb.onfig.tc_yocto_get_rootfs_from_tarball



------------------------------------------------

.. _tc_workfd_yocto_generate_bblayers_py:

yocto/tc_workfd_yocto_generate_bblayers.py
==========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_yocto_generate_bblayers.py

create bblayer.conf file



------------------------------------------------

.. _tc_workfd_yocto_patch_site_py:

yocto/tc_workfd_yocto_patch_site.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_yocto_patch_site.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_yocto_patch_site.py


patch / create site.conf


if tb.config.tc_workfd_yocto_patch_site_path_default_file != 'none'

use this file as default


add SWUPDATE_PRIVATE_KEY if tb.config.tc_workfd_yocto_patch_site_swu_priv_key

!= 'none'

add SWUPDATE_PASSWORD_FILE if tb.config.tc_workfd_yocto_patch_site_swu_priv_passout

!= 'none'

add SWUPDATE_PUBLIC_KEY if tb.config.tc_workfd_yocto_patch_site_swu_pub_key

!= 'none'

add UB_KEY_PATH if tb.config.tc_workfd_yocto_patch_site_ub_key

!= 'none'

add DL_DIR if tb.config.tc_workfd_yocto_patch_site_dl_dir != 'none'

add SSTATE_DIR if tb.config.tc_workfd_yocto_patch_site_sstate_dir != 'none'

add SRC_LINUX_STABLE if tb.config.tc_workfd_yocto_patch_site_src_linux_stable != 'none'

add PREMIRRORS_prepend if tb.config.tc_workfd_yocto_patch_site_premirrors != 'none'


------------------------------------------------

.. _tc_yocto_get_rootfs_from_tarball_py:

yocto/tc_yocto_get_rootfs_from_tarball.py
=========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_yocto_get_rootfs_from_tarball.py

start with

tbot.py -s lab_denx -c boardname -t tc_yocto_get_rootfs_from_tarball.py


get rootfs version from rootfs tar ball filepath and name stored in

tb.config.tc_yocto_get_rootfs_from_tarball

and store versionstring in variable:

tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version


------------------------------------------------

.. _tc_yocto_install_rootfs_as_nfs_py:

yocto/tc_yocto_install_rootfs_as_nfs.py
=======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_yocto_install_rootfs_as_nfs.py


- install tb.config.rootfs_tar_file in path tb.config.tc_yocto_install_rootfs_as_nfs_path

into tb.config.nfs_subdir



------------------------------------------------


.. _tc_board_git_bisect_py:

**********************
tc_board_git_bisect.py
**********************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_board_git_bisect.py

start with

python2.7 src/common/tbot.py -c tbot_tqm5200s.cfg -t tc_board_git_bisect.py

get a source code with tc tb.config.board_git_bisect_get_source_tc

and start a "git bisect" session

current commit is bad

good commit id is defined through tb.config.board_git_bisect_good_commit

tc for testing good or bad is tb.config.board_git_bisect_call_tc

if you have some local patches, which needs to be applied

each git bisect step, set tb.config.board_git_bisect_patches


if you need to restore your board after a failure, set the

variable tb.config.board_git_bisect_restore to the tc name

which restores the board.


------------------------------------------------

.. _tc_cp_and_start_script_py:

*************************
tc_cp_and_start_script.py
*************************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_cp_and_start_script.py



------------------------------------------------

.. _tc_dummy_py:

***********
tc_dummy.py
***********

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_dummy.py

This is only a dummy testcase, with which you can start

to write a testcase.


which explains what your testcase do and how, which

variables it uses.



------------------------------------------------

.. _tc_lab_apply_patches_py:

***********************
tc_lab_apply_patches.py
***********************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_apply_patches.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_apply_patches.py


set workfd to c_ctrl

call  tc_workfd_apply_patches_py_

restore old workfd



------------------------------------------------

.. _tc_lab_compile_uboot_py:

***********************
tc_lab_compile_uboot.py
***********************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_compile_uboot.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_compile_uboot.py


set workfd to c_ctrl

call tc_workfd_compile_uboot_py_

restore old workfd



------------------------------------------------

.. _tc_lab_cp_file_py:

*****************
tc_lab_cp_file.py
*****************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_cp_file.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_cp_file.py

simple copy  file from arg.get('s')

to arg.get('t') on the channel arg.get('ch')


------------------------------------------------

.. _tc_lab_get_uboot_source_py:

**************************
tc_lab_get_uboot_source.py
**************************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_get_uboot_source.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_get_uboot_source.py


get U-Boot source

and go into the source tree



------------------------------------------------

.. _tc_lab_poweroff_py:

******************
tc_lab_poweroff.py
******************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_poweroff.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_poweroff.py

simple power off the board


------------------------------------------------

.. _tc_lab_poweron_py:

*****************
tc_lab_poweron.py
*****************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_poweron.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_poweron.py

simple power on the board


------------------------------------------------

.. _tc_lab_rm_dir_py:

****************
tc_lab_rm_dir.py
****************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_rm_dir.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_rm_dir.py

simple rm a directory on the lab


------------------------------------------------

.. _tc_lab_set_toolchain_py:

***********************
tc_lab_set_toolchain.py
***********************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_set_toolchain.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_set_toolchain.py

set the toolchain


------------------------------------------------

.. _tc_test_bootcounter_py:

**********************
tc_test_bootcounter.py
**********************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_test_bootcounter.py

Test U-Boot / Linux bootcounter functionality

- go into U-Boot

- get bootcounter value

- reset

- get bootcounter value (must be previous + 1)

- reset

- get bootcounter value (must be previous + 1)

- boot linux

- get bootcounter value (must be the same as in U-Boot)

- set bootcounter value in linux

- power off the board

- power on the board

- go into U-Boot

- get bootcounter value (must be +1 the value set in linux)

- power off the board

- power on the board

- go into U-Boot

- get bootcounter value (must be 1)



------------------------------------------------

.. _tc_ub_boot_linux_py:

*******************
tc_ub_boot_linux.py
*******************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_ub_boot_linux.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_boot_linux.py

- load u-boot environment with testcase "tc_ub_load_board_env_py_"

- execute u-boot cmd tb.config.ub_boot_linux_cmd


------------------------------------------------

.. _tc_workfd_apply_patches_py:

**************************
tc_workfd_apply_patches.py
**************************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_workfd_apply_patches.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_apply_patches.py

apply patches to source


------------------------------------------------

.. _tc_workfd_compile_uboot_py:

**************************
tc_workfd_compile_uboot.py
**************************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_workfd_compile_uboot.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_compile_uboot.py

compile u-boot


------------------------------------------------

.. _tc_workfd_git_clone_source_py:

*****************************
tc_workfd_git_clone_source.py
*****************************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_workfd_git_clone_source.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_git_clone_source.py

get source from git repo tb.config.tc_lab_git_clone_source_git_repo with "git clone"

and go into the source tree. 

check out branch tb.config.tc_lab_git_clone_source_git_branch

and Apply patches if needed with:

tc_lab_apply_patches_py_ and patches from directory

tb.config.tc_lab_git_clone_apply_patches_dir

use as reference tb.config.tc_lab_git_clone_source_git_reference

if != 'none'

You can give the repo a name with setting

tb.config.tc_lab_git_clone_source_git_repo_name

!= 'none'

If you need a user/password for clining, you can define

the username through:

tb.config.tc_lab_git_clone_source_git_repo_user

define the password for this in password_py_

boardname in password_py_ is used as tb.config.tc_lab_git_clone_source_git_repo


------------------------------------------------

.. _tc_workfd_set_toolchain_py:

**************************
tc_workfd_set_toolchain.py
**************************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_workfd_set_toolchain.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_set_toolchain.py


set the toolchain, dependend on the architecture setting in

tb.config.tc_workfd_set_toolchain_arch

or source script set with tb.config.tc_workfd_set_toolchain_source

if tb.config.tc_workfd_set_toolchain_source != 'no'


supported toolchains defined in

tb.config.tc_workfd_set_toolchain_t_p and tb.config.tc_workfd_set_toolchain_cr_co


set also the ARCH environment variable with the value from

tb.config.tc_workfd_set_toolchain_arch


Add a list of also executed cmds in tb.config.tc_workfd_set_toolchain_addlist



------------------------------------------------

.. _tc_workfd_write_cmd_check_py:

****************************
tc_workfd_write_cmd_check.py
****************************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_workfd_write_cmd_check.py


Wrap a testcase around tb.write_cmd_check.


This testcase can be called via

tb.call_tc('tc_workfd_write_cmd_check_py_', cmd='foo', string='bar').



------------------------------------------------


The End

