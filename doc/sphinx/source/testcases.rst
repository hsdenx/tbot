.. include:: special.rst

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



:usedvar:`used variables`


.. _tb.config.bbb_check_crng_init:

- tb.config.bbb_check_crng_init

| wait for string "crng init"
| default: 'yes'


------------------------------------------------

.. _tc_board_bbb_bootmode_py:

board/bbb/tc_board_bbb_bootmode.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_bbb_bootmode.py


switch bootmode for the bbb

in the lab tbot2go.


- power off the board
- set bootmode
|   2 states:
|   normal: we use emmc
|   recovery: we boot from sd card


------------------------------------------------

.. _tc_board_bbb_bootmode_labdenx_py:

board/bbb/tc_board_bbb_bootmode_labdenx.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_bbb_bootmode_labdenx.py


switch bootmode for the bbb in the denx vlab


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

:usedvar:`used variables`


.. _tb.config.linux_user_nfsrootfs:

- tb.config.linux_user_nfsrootfs

| nfs rootfs username
| default: ''

.. _tb.config.linux_prompt_default_nfsrootfs:

- tb.config.linux_prompt_default_nfsrootfs

| default prompt from nfs rootfs
| default: ''


------------------------------------------------

.. _tc_board_yocto_boot_sdcard_py:

board/bbb/tc_board_yocto_boot_sdcard.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_yocto_boot_sdcard.py


- set jumper to normal
- boot sd card image

:usedvar:`used variables`


.. _tb.config.linux_user_yoctorootfs:

- tb.config.linux_user_yoctorootfs

| yocto rootfs username
| default: ''


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

same as in tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version_


If tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version_ is not set

try to get it from tb.config.yocto_results_dir_lab_ + tb.config.rootfs_tar_file_

with testcase tc_yocto_get_rootfs_from_tarball_py_



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
- if tb.config.rootfs_sdcard_file_ != 'none'
copy sd card image into nfs

- restore old workfd

:usedvar:`used variables`


.. _tb.config.rootfs_sdcard_file:

- tb.config.rootfs_sdcard_file

| if != 'none' copy tb.config.rootfs_sdcard_file_ file
| from tb.config.yocto_results_dir_lab_ to nfs directory
| tb.config.nfs_subdir_ + '/boot'
| default: 'none'


------------------------------------------------

.. _tc_board_yocto_install_sdcard_py:

board/bbb/tc_board_yocto_install_sdcard.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/board/bbb/tc_board_yocto_install_sdcard.py


install sd card image from

/boot/ + tb.config.rootfs_sdcard_file_ into

of=/dev/mmcblk + devnr


devnr gets detected with 'dmesg | grep mmc | grep SD'



------------------------------------------------


.. _tc_board_aristainetos2_py:

board/tc_board_aristainetos2.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_aristainetos2.py

start all testcases for the aristainetos2 board

tc_board_aristainetos2_linux_tests_py_

tc_workfd_set_toolchain_py_


------------------------------------------------

.. _tc_board_aristainetos2_linux_py:

board/tc_board_aristainetos2_linux.py
=====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_aristainetos2_linux.py

start all linux testcases for the aristainetos2 board


------------------------------------------------

.. _tc_board_aristainetos2_linux_bisect_py:

board/tc_board_aristainetos2_linux_bisect.py
============================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_aristainetos2_linux_bisect.py

start a git bisect for the aristainetos2 board


------------------------------------------------

.. _tc_board_aristainetos2_linux_tests_py:

board/tc_board_aristainetos2_linux_tests.py
===========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_aristainetos2_linux_tests.py

start all linux testcases for the aristainetos2 board


------------------------------------------------

.. _tc_board_ccu1_tests_py:

board/tc_board_ccu1_tests.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_ccu1_tests.py

start all testcases for the ccu1 board


------------------------------------------------

.. _tc_board_corvus_py:

board/tc_board_corvus.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_corvus.py

start all testcases for the corvus board


------------------------------------------------

.. _tc_board_dxr2_py:

board/tc_board_dxr2.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_dxr2.py

start all testcases for the dxr2 board


------------------------------------------------

.. _tc_board_dxr2_linux_py:

board/tc_board_dxr2_linux.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_dxr2_linux.py

start all linux testcases for the dxr2 board


------------------------------------------------

.. _tc_board_dxr2_lx_ubi_tests_py:

board/tc_board_dxr2_lx_ubi_tests.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_dxr2_lx_ubi_tests.py

more dxr2 specific ubi tests, maybe make them common


------------------------------------------------

.. _tc_board_dxr2_ub_py:

board/tc_board_dxr2_ub.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_dxr2_ub.py

start all u-boot testcases for the dxr2 board


------------------------------------------------

.. _tc_board_dxr2_ub_ubi_py:

board/tc_board_dxr2_ub_ubi.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_dxr2_ub_ubi.py

start all ubi testcases for the dxr2 board


------------------------------------------------

.. _tc_board_dxr2_uboot_patchwork_py:

board/tc_board_dxr2_uboot_patchwork.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_dxr2_uboot_patchwork.py

dxr2 check all patches with patchworknumber > default_nr

in patchwork, if it is checkpatch clean and applies to

current mainline without errors


------------------------------------------------

.. _tc_board_fipad_py:

board/tc_board_fipad.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad.py

start all U-Boot/linux testcases for the fipad board


------------------------------------------------

.. _tc_board_fipad_linux_py:

board/tc_board_fipad_linux.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad_linux.py

start all linux testcases for the fipad board


------------------------------------------------

.. _tc_board_fipad_ub_tests_py:

board/tc_board_fipad_ub_tests.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad_ub_tests.py

start all U-Boot testcases for the fipad board


------------------------------------------------

.. _tc_board_fipad_ub_usb_py:

board/tc_board_fipad_ub_usb.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad_ub_usb.py


do some simple usb test

- usb start
- usb info (check some output)
- list root dir on the stick
(ext2 formatted stick)

- load test.bin from this partition with ext2load
- check if test.bin has the crc32 sum 0x2144df1c

:usedvar:`used variables`


.. _tb.config.tc_board_fipad_uboot_ext2load_files:

- tb.config.tc_board_fipad_uboot_ext2load_files

| list of files which get load and crc32 tested
| default: '[]'


------------------------------------------------

.. _tc_board_fipad_upd_ub_py:

board/tc_board_fipad_upd_ub.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad_upd_ub.py

update SPL and u-boot.img on the SPI NOR or the MMC0

card, and boot it ...


------------------------------------------------

.. _tc_board_fipad_upd_ub_mmc_py:

board/tc_board_fipad_upd_ub_mmc.py
==================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad_upd_ub_mmc.py

update SPL and u-boot.img on the MMC0


------------------------------------------------

.. _tc_board_fipad_upd_ub_spi_py:

board/tc_board_fipad_upd_ub_spi.py
==================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_fipad_upd_ub_spi.py

update SPL and u-boot.img on the SPI NOR


------------------------------------------------

.. _tc_board_flea3_py:

board/tc_board_flea3.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_flea3.py

start all testcases for the flea3 board

currently only test the nor unprotect with linux


------------------------------------------------

.. _tc_board_mcx_py:

board/tc_board_mcx.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_mcx.py

start all testcases for the mcx board linux stable and linux-ml


------------------------------------------------

.. _tc_board_mcx_tests_py:

board/tc_board_mcx_tests.py
===========================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_mcx_tests.py

start all testcases for the mcx board


------------------------------------------------

.. _tc_board_shc_py:

board/tc_board_shc.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_shc.py

start all testcases for the shc board linux and linux-stable


------------------------------------------------

.. _tc_board_shc_compile_ml_py:

board/tc_board_shc_compile_ml.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_shc_compile_ml.py

compile ML linux kernel for the shc board


------------------------------------------------

.. _tc_board_shc_tests_py:

board/tc_board_shc_tests.py
===========================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_shc_tests.py

start all testcases for the shc board


------------------------------------------------

.. _tc_board_shc_ub_create_regdump_py:

board/tc_board_shc_ub_create_regdump.py
=======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_shc_ub_create_regdump.py

create a uboot regdump for all interesting registers

on the shc board


------------------------------------------------

.. _tc_board_shc_ub_tests_py:

board/tc_board_shc_ub_tests.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_shc_ub_tests.py

start all U-Boot testcases for the shc board


------------------------------------------------

.. _tc_board_shc_uboot_git_bisect_py:

board/tc_board_shc_uboot_git_bisect.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_shc_uboot_git_bisect.py

start git bisect for the shc board


------------------------------------------------

.. _tc_board_shc_upd_ub_py:

board/tc_board_shc_upd_ub.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_shc_upd_ub.py

update MLO and u-boot.img on the SD card or the eMMC

card, and boot it ...


------------------------------------------------

.. _tc_board_sigmatek-nand_py:

board/tc_board_sigmatek-nand.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_sigmatek-nand.py

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

remove, clone current mainline U-Boot, then

start tc_board_smartweb_test_ub_py_


------------------------------------------------

.. _tc_board_smartweb_test_ub_py:

board/tc_board_smartweb_test_ub.py
==================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_smartweb_test_ub.py

start all ub testcases for the smartweb board


------------------------------------------------

.. _tc_board_taurus_py:

board/tc_board_taurus.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_taurus.py

start all testcases for the taurus board


------------------------------------------------

.. _tc_board_thuban_py:

board/tc_board_thuban.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_thuban.py

get u-boot code with tc_demo_get_ub_code_py_


and call testcase tc_demo_compile_install_test_py_


------------------------------------------------

.. _tc_board_thuban_test_uboot_py:

board/tc_board_thuban_test_uboot.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_thuban_test_uboot.py

trigger a bug in old U-Boot ubi implementation

and test, if with current U-Boot this bug does

not appear anymore.


boot into linux and install a buggy nand image


go into u-boot and start an old u-boot binary,

which has the bug, which leads into a reset


After the reset, the new U-Boot is booted.


run 'ubi part rootfs 2048' which repairs the buggy

nand and no U-Boot reset should ocur.


after the new U-Boot has repaired the nand, the old

U-Boot should also work again.


call testcase tc_demo_uboot_tests_py_ for doing

U-Boot standard tests.



------------------------------------------------

.. _tc_board_tqm5200s_try_cur_ub_py:

board/tc_board_tqm5200s_try_cur_ub.py
=====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_tqm5200s_try_cur_ub.py

remove current u-boot code on the lab PC

then call tc tc_board_tqm5200s_ub_comp_install_py_


------------------------------------------------

.. _tc_board_tqm5200s_ub_comp_install_py:

board/tc_board_tqm5200s_ub_comp_install.py
==========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_board_tqm5200s_ub_comp_install.py

compile and install U-Boot for the tqm5200s board

install U-Boot with BDI


------------------------------------------------

.. _tc_linux_create_reg_file_am335x_py:

board/tc_linux_create_reg_file_am335x.py
========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_linux_create_reg_file_am335x.py

create a regfile for am335x SoC registers


------------------------------------------------

.. _tc_linux_create_reg_file_imx6qdl_py:

board/tc_linux_create_reg_file_imx6qdl.py
=========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/board/tc_linux_create_reg_file_imx6qdl.py

create a regfile for imx6qdl SoC registers


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

connect to the BDI if tb.config.board_has_debugger_ == 'yes'

- send to workfd tb.config.lab_bdi_upd_uboot_bdi_cmd_
- set BDI prompt tb.config.lab_bdi_upd_uboot_bdi_prompt_
- wait for BDI prompt

:usedvar:`used variables`


.. _tb.config.lab_bdi_upd_uboot_bdi_cmd:

- tb.config.lab_bdi_upd_uboot_bdi_cmd

| command for connecting to BDI
| default: 'telnet bdi6'

.. _tb.config.lab_bdi_upd_uboot_bdi_prompt:

- tb.config.lab_bdi_upd_uboot_bdi_prompt

| BDI prompt string
| default: 'BDI>'


------------------------------------------------

.. _tc_lab_bdi_create_dump_py:

debugger/bdi/tc_lab_bdi_create_dump.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/debugger/bdi/tc_lab_bdi_create_dump.py


check if we are on the BDI already, if not switch to it

with tc_lab_bdi_connect_py_


- send "halt"
- dump registers from tb.config.tc_lab_bdi_create_dump_start_
to tb.config.tc_lab_bdi_create_dump_stop_ with mask

tb.config.tc_lab_bdi_create_dump_mask_ and stepsize

tb.config.tc_lab_bdi_create_dump_type_ into the file

tb.config.tc_lab_bdi_create_dump_filename_


:usedvar:`used variables`


.. _tb.config.tc_lab_bdi_create_dump_filename:

- tb.config.tc_lab_bdi_create_dump_filename

| filename, to witch registers get dumped
| default: ''

.. _tb.config.tc_lab_bdi_create_dump_start:

- tb.config.tc_lab_bdi_create_dump_start

| register start address from which dump gets created
| default: ''

.. _tb.config.tc_lab_bdi_create_dump_stop:

- tb.config.tc_lab_bdi_create_dump_stop

| register stop address to which dump gets created
| default: ''

.. _tb.config.tc_lab_bdi_create_dump_mask:

- tb.config.tc_lab_bdi_create_dump_mask

| default mask, which get added
| default: ''

.. _tb.config.tc_lab_bdi_create_dump_type:

- tb.config.tc_lab_bdi_create_dump_type

| type with which registers get read
| default: ''


------------------------------------------------

.. _tc_lab_bdi_disconnect_py:

debugger/bdi/tc_lab_bdi_disconnect.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/debugger/bdi/tc_lab_bdi_disconnect.py

disconnect from the BDI

- send bdi command "quit"
- set tb.config.linux_prompt_

------------------------------------------------

.. _tc_lab_bdi_run_py:

debugger/bdi/tc_lab_bdi_run.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/debugger/bdi/tc_lab_bdi_run.py

BDI run

- send "res halt" to workfd
- send BDI cmd tb.config.lab_bdi_upd_uboot_bdi_run_

:usedvar:`used variables`


.. _tb.config.lab_bdi_upd_uboot_bdi_run:

- tb.config.lab_bdi_upd_uboot_bdi_run

| command for resetting U-Boot
| default: "[{'cmd':'res run', 'val':'resetting target passed'}]"


------------------------------------------------

.. _tc_lab_bdi_upd_uboot_py:

debugger/bdi/tc_lab_bdi_upd_uboot.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/debugger/bdi/tc_lab_bdi_upd_uboot.py

update u-boot with BDI

- send BDI cmd: "res halt"
- send BDI cmd: "era"
- send BDI cmd:
tb.config.lab_bdi_upd_uboot_bdi_prog_ + ' ' + tb.config.lab_bdi_upd_uboot_bdi_file_ + ' BIN'

- send BDI cmd: tb.config.lab_bdi_upd_uboot_bdi_run_

:usedvar:`used variables`


.. _tb.config.lab_bdi_upd_uboot_bdi_era:

- tb.config.lab_bdi_upd_uboot_bdi_era

| command for erasing
| default: 'era'

.. _tb.config.lab_bdi_upd_uboot_bdi_prog:

- tb.config.lab_bdi_upd_uboot_bdi_prog

| command for programming
| default: 'prog 0xfc000000'

.. _tb.config.lab_bdi_upd_uboot_bdi_file:

- tb.config.lab_bdi_upd_uboot_bdi_file

| filename, which get programmed
| default: '/tftpboot/tqm5200s/tbot/u-boot.bin'


------------------------------------------------



.. _Directory_default:

*****************
Directory default
*****************

.. _tc_def_lx_py:

default/tc_def_lx.py
====================

https://github.com/hsdenx/tbot/blob/master/src/tc/default/tc_def_lx.py

simple set default values for linux testcases


:usedvar:`used variables`


.. _tb.config.tc_lx_mount_dir:

- tb.config.tc_lx_mount_dir

|  path where testcase tc_lx_mount_py_ mounts
|  default: '/home/hs/mnt'

.. _tb.config.uboot_get_parameter_file_list:

- tb.config.uboot_get_parameter_file_list

| list of files, where TC searches for the define
| used by: tc_workfd_get_uboot_config_string_py_
| tc_workfd_get_uboot_config_hex_py_
| default: ''

.. _tb.config.uboot_config_option:

- tb.config.uboot_config_option

| config option which get searched
| used by: tc_workfd_get_uboot_config_string_py_
| tc_workfd_get_uboot_config_hex_py_
| default: ''

.. _tb.config.tc_workfd_lx_get_bc_file:

- tb.config.tc_workfd_lx_get_bc_file

| path with filename to bootcounter file
| default: '/sys/devices/soc0/soc/2100000.aips-bus/21a0000.i2c/i2c-0/0-0008/bootcount'


------------------------------------------------

.. _tc_def_tbot_py:

default/tc_def_tbot.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/default/tc_def_tbot.py

simple set default values for tbot


:usedvar:`used variables`


.. _tb.config.ip:

- tb.config.ip

| ip of the lab PC
| default: ''

.. _tb.config.user:

- tb.config.user

| username for loggin into lab PC
| default: ''

.. _tb.config.boardname:

- tb.config.boardname

| boardname: name of the board.
| default: ''

.. _tb.config.uboot_strings:

- tb.config.uboot_strings

| Strings found when U-Boot is booting
| default: "['Autobooting in', 'noautoboot',  'autoboot', 'EOF', 'RomBOOT']"

.. _tb.config.tc_lab_source_dir:

- tb.config.tc_lab_source_dir

| tbot source directory on lab PC
| default: '/work/hs/tbot'

.. _tb.config.tc_workfd_work_dir:

- tb.config.tc_workfd_work_dir

| tbots workdirectory on labor PC
| default: tb.config.tc_lab_source_dir_

.. _tb.config.tc_workfd_tbotfiles_dir:

- tb.config.tc_workfd_tbotfiles_dir

| place for tbot to store tempfiles on labor PC
| default: tb.config.tc_workfd_work_dir_ + '/tmpfiles'

.. _tb.config.board_has_debugger:

- tb.config.board_has_debugger

| if 'yes' board has a debugger
| default: 'no'

.. _tb.config.lab_tmp_dir:

- tb.config.lab_tmp_dir

| directory on lab PC, where tbot stores temporary files.
| default: '/var/tmp'

.. _tb.config.compile_pc_workdir:

- tb.config.compile_pc_workdir

| tbots workdirectory on compile PC
| default: tb.config.tc_lab_source_dir_

.. _tb.config.debug:

- tb.config.debug

| If 'True' enable debugprint() output
| default: 'False'

.. _tb.config.debugstatus:

- tb.config.debugstatus

| If 'True' enable statusprintf() output
| default: 'False'

.. _tb.config.state_uboot_timeout:

- tb.config.state_uboot_timeout

| u-boot read timeout in seconds (float)
| default: '1'

.. _tb.config.uboot_autoboot_key:

- tb.config.uboot_autoboot_key

| U-Boots autoboot key, send if autoboot is read, and != 'none'
| default: 'none'

.. _tb.config.tb_power_state:

- tb.config.tb_power_state

| last read powerstate
| default: 'undef'

.. _tb.config.term_line_length:

- tb.config.term_line_length

| maximal line length of terminal
| default: '200'

.. _tb.config.wdt_timeout:

- tb.config.wdt_timeout

| wdt timeout in seconds
| default: '120'

.. _tb.config.state_linux_timeout:

- tb.config.state_linux_timeout

| linux timeout in seconds when reading from channel
| default: '4'

.. _tb.config.labsshprompt:

- tb.config.labsshprompt

| prompt after login into lab with ssh
| default: '$ '

.. _tb.config.tc_return:

- tb.config.tc_return

| used as return value from testcases
| default: 'True'

.. _tb.config.ub_boot_linux_cmd:

- tb.config.ub_boot_linux_cmd

| bootcommand for booting linux
| default: 'run tbot_boot_linux'

.. _tb.config.do_connect_to_board:

- tb.config.do_connect_to_board

| connect to boards console on tbot start
| default: 'True'

.. _tb.config.tftpboardname:

- tb.config.tftpboardname

| tftp subdir name for board
| default: tb.config.boardname_

.. _tb.config.boardlabname:

- tb.config.boardlabname

| boardsname in the lab
| default: tb.config.boardname_

.. _tb.config.boardlabpowername:

- tb.config.boardlabpowername

| boards name in the lab for power on/off
| default: tb.config.boardname_

.. _tb.config.tftpboardrootdir:

- tb.config.tftpboardrootdir

| root path for tftp directory (if needed for u-boot)
| default: 'none'

.. _tb.config.tc_lab_denx_power_tc:

- tb.config.tc_lab_denx_power_tc

| Name of testcase, which controlls power state of the board
| default: 'tc_lab_denx_power_py_'

.. _tb.config.tc_lab_denx_get_power_state_tc:

- tb.config.tc_lab_denx_get_power_state_tc

| Name of the testcase, which reads the current powerstate of the board
| default: 'tc_lab_denx_get_power_state_py_'

.. _tb.config.tc_lab_denx_connect_to_board_tc:

- tb.config.tc_lab_denx_connect_to_board_tc

| Name of the testcase, which connects to boards console
| default: 'tc_lab_denx_connect_to_board_py_'

.. _tb.config.tc_lab_denx_disconnect_from_board_tc:

- tb.config.tc_lab_denx_disconnect_from_board_tc

| Name of the testcase, which disconnects from boards console
| default: 'tc_lab_denx_disconnect_from_board_py_'

.. _tb.config.linux_prompt_default:

- tb.config.linux_prompt_default

| linux default prompt, after login into console
| default: 'root@generic-armv7a-hf:~# '

.. _tb.config.labprompt:

- tb.config.labprompt

| prompt of the lab, tbot set after login
| default: tb.config.linux_prompt_

.. _tb.config.linux_prompt:

- tb.config.linux_prompt

| prompt of the lab, tbot set after login
| default: ''

.. _tb.config.linux_user:

- tb.config.linux_user

| Username for linux used on the board
| default: 'root'

.. _tb.config.create_dot:

- tb.config.create_dot

| Call the "dot" backend after tbot finsihed
| default: 'no'

.. _tb.config.create_statistic:

- tb.config.create_statistic

| Call the "statistic" backend after tbot finsihed
| default: 'no'

.. _tb.config.create_dashboard:

- tb.config.create_dashboard

| Call the "dashboard" backend after tbot finsihed
| default: 'no'

.. _tb.config.create_webpatch:

- tb.config.create_webpatch

| Call the "webpatch" backend after tbot finsihed
| default: 'no'

.. _tb.config.create_html_log:

- tb.config.create_html_log

| Call the "html_log" backend after tbot finsihed
| default: 'no'

.. _tb.config.create_documentation:

- tb.config.create_documentation

| Call the "documentation" backend after tbot finsihed
| default: 'no'

.. _tb.config.event_documentation_strip_list:

- tb.config.event_documentation_strip_list

| see documentation backend documentation
| default: '[]'

.. _tb.config.create_documentation_auto:

- tb.config.create_documentation_auto

| see documentation backend documentation
| default: '[]'

.. _tb.config.create_junit:

- tb.config.create_junit

| Call the "junit" backend after tbot finsihed
| default: 'no'

.. _tb.config.config.junit_tclist:

- tb.config.config.junit_tclist

| list of testcasenames, for which the logfile get delivered to jenkins
| default: "['tc_lab_get_uboot_source_py_',
|            'tc_workfd_set_toolchain_py_', 'tc_workfd_compile_uboot_py_',
|            'tc_workfd_connect_with_kermit_py_', 'tc_ub_upd_uboot_py_',
|            'tc_ub_upd_spl_py_', 'tc_ub_check_version_py_']"

.. _tb.config.junit_ignlist:

- tb.config.junit_ignlist

| list of testcasesnames, which get not passed to jenkins
| default: "['tc_workfd_check_cmd_success_py_',
|            'tc_dummy_py_']"

.. _tb.config.tb_set_after_linux:

- tb.config.tb_set_after_linux

| testcase called after logging into linux on board.
| default: 'none'


------------------------------------------------

.. _tc_def_ub_py:

default/tc_def_ub.py
====================

https://github.com/hsdenx/tbot/blob/master/src/tc/default/tc_def_ub.py

simple set default values for U-Boot testcases


:usedvar:`used variables`


.. _tb.config.tc_ub_tftp_file_addr:

- tb.config.tc_ub_tftp_file_addr

| ram address to which the file gets loaded
| default: tb.config.ub_load_board_env_addr_

.. _tb.config.tc_ub_tftp_file_name:

- tb.config.tc_ub_tftp_file_name

| file name for the tftp command
| default: ''

.. _tb.config.tc_ub_tftp_path:

- tb.config.tc_ub_tftp_path

| tftp boot directory path for tftp U-Boot command
| default: tb.config.tftpboardname_ + '/' + tb.config.ub_load_board_env_subdir_


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


- goto linux code with testcase tc_workfd_goto_linux_code_py_
- compile with testcase tc_workfd_compile_linux_py_
- deploy it. If tb.config.tc_demo_linux_test_deploy_ != 'none'
|  call boardspecific testcase for deploying linux sources.
|  else copy files from "$TBOT_BASEDIR_LINUX/arch/arm/boot/"
|  to tb.config.tftpboardname_ + '/' + tb.config.ub_load_board_env_subdir_

:usedvar:`used variables`


.. _tb.config.tc_demo_linux_test_deploy:

- tb.config.tc_demo_linux_test_deploy

| contains the testcasename which get called for deploying linux
| default: 'none'


------------------------------------------------

.. _tc_demo_linux_test_py:

demo/linux/tc_demo_linux_test.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/linux/tc_demo_linux_test.py


- if tb.config.tc_board_bootmode_tc_ is defined
call tc tb.config.tc_board_bootmode_tc_

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


- if tb.config.tc_board_bootmode_tc_ is set, call
tb.config.tc_board_bootmode_tc_

- boot a linux kernel if tb.config.tc_demo_linux_tc_boot_lx_
is set to 'yes' 

- get booted linux version
- grep through dmesg and check if strings in
tb.config.tc_demo_linux_test_dmesg_ exist

- check with devmem2 if the register values defined
in the register files tb.config.tc_demo_linux_test_reg_files_

are identical with the values defined in the files

- start cmd defined in tb.config.tc_demo_linux_test_basic_cmd_
and check the returning strings.

- call testcase names defined in list tb.config.tc_demo_linux_tc_list_

:usedvar:`used variables`


.. _tb.config.tc_demo_linux_tc_boot_lx:

- tb.config.tc_demo_linux_tc_boot_lx

| if == 'yes' boot a linux kernel
| default: 'yes'

.. _tb.config.tc_demo_linux_test_dmesg:

- tb.config.tc_demo_linux_test_dmesg

| list of strings, which must be in dmesg
| default: 'none'

.. _tb.config.tc_demo_linux_test_reg_files:

- tb.config.tc_demo_linux_test_reg_files

| list of register filenames, which get
| checked with testcase tc_lx_check_reg_file_py_
| default: 'none'

.. _tb.config.tc_demo_linux_test_basic_cmd:

- tb.config.tc_demo_linux_test_basic_cmd

| list of dictionary with key = 'cmd' and value = 'val'
| command in 'cmd gets executed and checked if string in 'val'
| is found. if 'val' == 'undef', no check, only command is
| executed.
| default: 'none'

.. _tb.config.tc_demo_linux_tc_list:

- tb.config.tc_demo_linux_tc_list

| list of testcasenames, which get called
| default: 'none'


------------------------------------------------


.. _u-boot:

Directory demo/u-boot
=====================

.. _tc_demo_compile_install_test_py:

demo/u-boot/tc_demo_compile_install_test.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/u-boot/tc_demo_compile_install_test.py

- if tb.config.tc_board_bootmode_tc_ is defined
|   call tc tb.config.tc_board_bootmode_tc_
|   (set bootmode for the board)
- go to uboot code with tc_workfd_goto_uboot_code_py_
- set toolchain with tc_workfd_set_toolchain_py_
- compile source tree with tc_workfd_compile_uboot_py_
- if tb.config.tc_demo_uboot_test_deploy_ != ''
|     call tb.config.tc_demo_uboot_test_deploy_
|   else
|     copy files in list tb.config.tc_demo_compile_install_test_files_
|     tb.config.tc_demo_compile_install_test_files_ contains a list of files,
|     which are copied to tftp directory
|     tb.config.tftpdir_ + tb.config.tftpboardname_ + '/' + tb.config.ub_load_board_env_subdir_
- get u-boot version from binary with tc_ub_get_version_py_
- if tb.config.tc_demo_uboot_test_update_ != '':
|     call tb.config.tc_demo_uboot_test_update_
|   else:
|     call tc_ub_upd_uboot_py_
|     call tc_ub_upd_spl_py_
- if tb.config.tc_demo_compile_install_test_spl_vers_file_ and/or
|   tb.config.tc_demo_compile_install_test_ub_vers_file_ != ''
|   check if the new installed version is the same
|   as in the binary files, defined in
|   tb.config.tc_demo_compile_install_test_ub_vers_file_ or
|   tb.config.tc_demo_compile_install_test_spl_vers_file_
- call tb.config.tc_demo_compile_install_test_name_
|     which should contain a testcase, which tests the new
|     installed u-boot
- if tb.config.tc_demo_compile_install_test_poweroff_ == 'yes':
|     power off board at the end.

:usedvar:`used variables`:


.. _tb.config.tc_demo_compile_install_test_ub_vers_file:

- tb.config.tc_demo_compile_install_test_ub_vers_file

| if != 'none' contains the filename, in which testcase
| tc_ub_get_version_py_ find the U-Boot version
| default: 'none'

.. _tb.config.tc_demo_compile_install_test_spl_vers_file:

- tb.config.tc_demo_compile_install_test_spl_vers_file

| if != 'none' contains the filename, in which testcase
| tc_ub_get_version_py_ find the U-Boot SPL version
| default: 'none'

.. _tb.config.tc_demo_uboot_test_deploy:

- tb.config.tc_demo_uboot_test_deploy

| if != 'none' call testcase with name tb.config.tc_demo_uboot_test_deploy_
| for installing U-Boot
| default: 'none'

.. _tb.config.tc_board_bootmode_tc:

- tb.config.tc_board_bootmode_tc

| if != 'none' call testcase with name tb.config.tc_board_bootmode_tc_
| for switching bootmode of the board
| default: 'none'

.. _tb.config.tc_demo_compile_install_test_poweroff:

- tb.config.tc_demo_compile_install_test_poweroff

| if 'yes, switch off board power after successful test
| default: 'yes'

.. _tb.config.tc_demo_compile_install_test_name:

- tb.config.tc_demo_compile_install_test_name

| if != 'none' call testcase with name tb.config.tc_demo_compile_install_test_name_
| to test the new installed u-boot
| default: 'none'

.. _tb.config.tc_demo_compile_install_test_files:

- tb.config.tc_demo_compile_install_test_files

| list of files which get copied into tftpdirectory
| default: 'none'

.. _tb.config.tc_demo_uboot_test_update:

- tb.config.tc_demo_uboot_test_update

| if != 'none' testcasename which gets called for updating U-Boot
| default: 'none'


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

- rm old u-boot tree (if there is one)
- tc_lab_get_uboot_source_py_

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


start all "standard" u-boot testcases


- if tb.config.tc_demo_uboot_test_reg_files_ contains
a list of files, check for each file with testcase

tc_ub_check_reg_file_py_ if the registersettings are

correct.


- start cmd defined in tb.config.tc_demo_uboot_test_basic_cmd_
and check the returning strings.


- tb.eof_call_tc("uboot/duts/tc_ub_start_all_duts_py_")

- tb.eof_call_tc("tc_ub_test_py_py_")

- call a list of testcases defined in
tb.config.tc_demo_uboot_tc_list_


:usedvar:`used variables`:


.. _tb.config.tc_demo_uboot_test_reg_files:

- tb.config.tc_demo_uboot_test_reg_files

| list of register files, which contain registerdumps
| used for testcase
| tc_ub_check_reg_file_py_
| default: 'none'

.. _tb.config.tc_demo_uboot_test_basic_cmd:

- tb.config.tc_demo_uboot_test_basic_cmd

| list of dictionary, which contains key = 'cmd' and
| value = 'val' entries
| default: 'none'
| example: [
|              {"cmd":"help", "val":"i2c"},
|              {"cmd":"md", "val":"undef"},
|          ]
|
| If "val" = 'undef' only command gets executed, no check

.. _tb.config.tc_demo_uboot_tc_list:

- tb.config.tc_demo_uboot_tc_list

| list of testcasesnames, which get called
| default: 'none'


------------------------------------------------


.. _tc_demo_can_part1_py:

demo/tc_demo_can_part1.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/tc_demo_can_part1.py

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

start tc:


- set workfd to c_ctrl
- call tc_demo_uboot_test_py_


------------------------------------------------

.. _tc_demo_part2_py:

demo/tc_demo_part2.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/tc_demo_part2.py

start tc:

- call tc_demo_get_ub_code_py_
- call tc_demo_compile_install_test_py_

------------------------------------------------

.. _tc_demo_part3_py:

demo/tc_demo_part3.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/demo/tc_demo_part3.py

start tc: tc_board_git_bisect_py_


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

connect to board tb.config.boardlabname_ with

connect script


------------------------------------------------

.. _tc_lab_denx_disconnect_from_board_py:

lab/denx/tc_lab_denx_disconnect_from_board.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_denx_disconnect_from_board.py

disconnect from board tb.config.boardlabname_

in denx vlab


------------------------------------------------

.. _tc_lab_denx_get_power_state_py:

lab/denx/tc_lab_denx_get_power_state.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_denx_get_power_state.py

get the power state of the board tb.config.boardlabpowername,_

and save it in tb.power_state



------------------------------------------------

.. _tc_lab_denx_power_py:

lab/denx/tc_lab_denx_power.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_denx_power.py

power on/off the board tb.config.boardlabpowername_


------------------------------------------------

.. _tc_lab_interactive_get_power_state_py:

lab/denx/tc_lab_interactive_get_power_state.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_interactive_get_power_state.py

get the power state of the board through user input,

and save it in tb.power_state


Currently nothing done.



------------------------------------------------

.. _tc_lab_interactive_power_py:

lab/denx/tc_lab_interactive_power.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_interactive_power.py

power on/off the board tb.config.boardlabpowername_ manually


You will see a countdown from 3 to 1


Than you have to power on or off the board manually


------------------------------------------------


.. _tc_lab_kmtronic_get_power_state_py:

lab/tc_lab_kmtronic_get_power_state.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_kmtronic_get_power_state.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_kmtronic_get_power_state.py

power on/off the board


get the power state of the board attached to a kmtronic usb relay:


http://info.kmtronic.com/kmtronic-usb-relay-test-software.html


and save it in tb.power_state


use testcase "tc_lab_kmtronic_get_variables_py_" for setting

the serial and the index you need for the specific board.


This file is an example for a setup, you need to adapt

this to your needs.



------------------------------------------------

.. _tc_lab_kmtronic_get_variables_py:

lab/tc_lab_kmtronic_get_variables.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_kmtronic_get_variables.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_kmtronic_get_variables.py

get tty device tb.config.kmtronic_dev_ and

tb.config.kmtronic_addr_

for the kmtronic usb relay, see:


http://info.kmtronic.com/kmtronic-usb-relay-test-software.html



------------------------------------------------

.. _tc_lab_kmtronic_set_power_state_py:

lab/tc_lab_kmtronic_set_power_state.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_kmtronic_set_power_state.py

start with

python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_kmtronic_set_power_state.py

power on/off the board


get the power state of the board attached to a kmtronic usb relay:


http://info.kmtronic.com/kmtronic-usb-relay-test-software.html


and save it in tb.power_state


use testcase "tc_lab_kmtronic_get_variables_py_" for setting

the serial and the index you need for the specific board.


This file is an example for a setup, you need to adapt

this to your needs.



------------------------------------------------

.. _tc_lab_power_onoff_gpio_py:

lab/tc_lab_power_onoff_gpio.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_power_onoff_gpio.py


Switch on/off boardpower through a GPIO pin

from the lab PC


define the gpio for powering on/off in your board config

file with for example:

gpio_power_on = gpo(21) # gpio number of gpio used to controll power of board


:usedvar:`used variables`


.. _tb.config.gpio_power_on:

- tb.config.gpio_power_on

| gpio pin used for powering on / off the board
| default: ''


------------------------------------------------

.. _tc_lab_prepare_py:

lab/tc_lab_prepare.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_prepare.py


when logging into a lab, do some basic setup

- go into workdir
- if tb.config.tc_lab_prepare_tc_name_ != 'none' then call
testcase which name is defined in tb.config.tc_lab_prepare_tc_name_


In this testcase, you can do lab specific setup you need

and set the variable tb.config.tc_lab_prepare_tc_name_

with the name you give your testcase for lab specific setup.


:usedvar:`used variables`


.. _tb.config.tc_lab_prepare_tc_name:

- tb.config.tc_lab_prepare_tc_name

| call testcase with this name for settings up lab specific
| tasks.
| default: 'none'


------------------------------------------------

.. _tc_lab_prepare_laptop_hs_py:

lab/tc_lab_prepare_laptop_hs.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_prepare_laptop_hs.py


do setup needed for the laptop from hs, when used as

lapPC



------------------------------------------------

.. _tc_lab_prepare_tbot2go_py:

lab/tc_lab_prepare_tbot2go.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_prepare_tbot2go.py


do setup needed for the pi in tbot2go mode, when used as

lapPC



------------------------------------------------

.. _tc_lab_sispmctl_get_power_state_py:

lab/tc_lab_sispmctl_get_power_state.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_sispmctl_get_power_state.py

get the power state of the board through sispmctl

and save it in tb.power_state

find more information for the Gembird Silver Shield PM power controller:

http://sispmctl.sourceforge.net/


use testcase tc_lab_sispmctl_get_variables_py_ for setting

the serial and the index you need for the specific board.


This file is an example for a setup, you need to adapt

this to your needs.



------------------------------------------------

.. _tc_lab_sispmctl_get_variables_py:

lab/tc_lab_sispmctl_get_variables.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_sispmctl_get_variables.py

get serial and index for tb.config.boardlabpowername_ for

controlling the Gembird Silver Shield PM power controller

and save it in tb.config.gembird_serial_ and tb.config.gembird_index_


:usedvar:`used variables`


.. _tb.config.gembird_serial:

- tb.config.gembird_serial

| setup at runtime of testcase tc_lab_sispmctl_get_variables_py_
| contains the serial number of the gembird controller
| to which the tb.config.boardlabpowername_ is connected

.. _tb.config.gembird_index:

- tb.config.gembird_index

| setup at runtime of testcase tc_lab_sispmctl_get_variables_py_
| contains the device index of the gembird controller
| to which the tb.config.boardlabpowername_ is connected


------------------------------------------------

.. _tc_lab_sispmctl_set_power_state_py:

lab/tc_lab_sispmctl_set_power_state.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_sispmctl_set_power_state.py

power on/off the board with Gembird Silver Shiels


get the power state of the board through sispmctl tool

and save it in tb.power_state

find more information for the Gembird Silver Shield PM power controller:

http://sispmctl.sourceforge.net/


use testcase tc_lab_sispmctl_get_variables_py_ for setting

the tb.config.gembird_serial_ and tb.config.gembird_index_

you need for the specific board.



------------------------------------------------

.. _tc_lab_usb_relay_power_py:

lab/tc_lab_usb_relay_power.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_usb_relay_power.py

power on / off the board tb.config.boardlabpowername_

with testcase tc_linux_relay_simple_set_py_


simple util must be installed, source see

src/files/relay/simple.c


adapt dependend on tb.config.boardlabpowername_

which port you use..


If you have more than one USB relay from sainsmart

adapt simple.c to work with the serial ID, and adapt

also tb.config.tc_linux_relay_simple_set_cmd_



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

get relay tbot configuration


:usedvar:`used variables`


.. _tb.config.tc_linux_relay_simple_set_cmd:

- tb.config.tc_linux_relay_simple_set_cmd

| command string for simple command
| default: '/home/hs/Software/usbrelais/src/simple '

.. _tb.config.tc_linux_relay_simple_set_sudo:

- tb.config.tc_linux_relay_simple_set_sudo

| if 'yes' preceed tb.config.tc_linux_relay_simple_set_cmd_
| with sudo
| default: 'yes'

.. _tb.config.tc_linux_relay_set_tc:

- tb.config.tc_linux_relay_set_tc

| testcase which get called for setting the relay
| default: 'tc_linux_relay_simple_set_py_'


------------------------------------------------

.. _tc_linux_relay_set_py:

linux/relay/tc_linux_relay_set.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/relay/tc_linux_relay_set.py

set relay port tb.config.tc_linux_relay_set_port_ to state

tb.config.tc_linux_relay_set_state._


you need to adapt tc_linux_relay_get_config_py_, which does

the mapping from port/state to your specific lab settings.


:usedvar:`used variables`



------------------------------------------------

.. _tc_linux_relay_simple_set_py:

linux/relay/tc_linux_relay_simple_set.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/relay/tc_linux_relay_simple_set.py

set relay port with the simple cmd to state

find the c source code for the simple cmd in src/files/relay/simple.c


tb.config.tc_linux_relay_simple_set_sudo_ if 'yes' "sudo" is prwpended to

tb.config.tc_linux_relay_simple_set_cmd_ and if password is needed, password

is searched in password_py_ with board = tb.config.ip_ and user = tb.config.user_ + '_sudo'



------------------------------------------------


.. _ubi:

Directory linux/ubi
===================

.. _tc_lx_ubi_attach_py:

linux/ubi/tc_lx_ubi_attach.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/ubi/tc_lx_ubi_attach.py

call ubiattach



------------------------------------------------

.. _tc_lx_ubi_def_py:

linux/ubi/tc_lx_ubi_def.py
,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/ubi/tc_lx_ubi_def.py

simply set defaults for linux ubi tests


:usedvar:`used variables`


.. _tb.config.tc_ubi_cmd_path:

- tb.config.tc_ubi_cmd_path

| path to ubi commands (in mtd-utils package)
| default: '/work/tbot/mtd-utils'

.. _tb.config.tc_ubi_mtd_dev:

- tb.config.tc_ubi_mtd_dev

| mtd device used
| default: '/dev/mtd4'

.. _tb.config.tc_ubi_ubi_dev:

- tb.config.tc_ubi_ubi_dev

| ubi device used
| default: '/dev/ubi0'

.. _tb.config.tc_ubi_min_io_size:

- tb.config.tc_ubi_min_io_size

| ubi minimum io size
| http://www.linux-mtd.infradead.org/faq/ubi.html#L_find_min_io_size
| may you detect them with testcase tc_lx_get_ubi_parameters_py_
| default: '1024'

.. _tb.config.tc_ubi_max_leb_cnt:

- tb.config.tc_ubi_max_leb_cnt

| used leb number
| may you detect them with testcase tc_lx_get_ubi_parameters_py_
| default: '100'

.. _tb.config.tc_ubi_leb_size:

- tb.config.tc_ubi_leb_size

| http://www.linux-mtd.infradead.org/faq/ubi.html#L_find_min_io_size
| may you detect them with testcase tc_lx_get_ubi_parameters_py_
| default: '126976'

.. _tb.config.tc_ubi_vid_hdr_offset:

- tb.config.tc_ubi_vid_hdr_offset

| http://www.linux-mtd.infradead.org/doc/ubi.html#L_ubi_headers
| http://www.linux-mtd.infradead.org/faq/ubi.html#L_vid_offset_mismatch
| default: 'default'

.. _tb.config.tc_lx_ubi_format_filename:

- tb.config.tc_lx_ubi_format_filename

| filename for ubiformat
| default: '/home/hs/ccu1/ecl-image-usbc.ubi'


------------------------------------------------

.. _tc_lx_ubi_detach_py:

linux/ubi/tc_lx_ubi_detach.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/ubi/tc_lx_ubi_detach.py

detach ubi device tb.config.tc_ubi_mtd_dev_


------------------------------------------------

.. _tc_lx_ubi_format_py:

linux/ubi/tc_lx_ubi_format.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/ubi/tc_lx_ubi_format.py

ubiformat tb.config.tc_ubi_mtd_dev_ with tb.config.tc_lx_ubi_format_filename_


------------------------------------------------

.. _tc_lx_ubi_info_py:

linux/ubi/tc_lx_ubi_info.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/ubi/tc_lx_ubi_info.py

ubinfo tb.config.tc_ubi_ubi_dev_


------------------------------------------------

.. _tc_lx_ubi_tests_py:

linux/ubi/tc_lx_ubi_tests.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/ubi/tc_lx_ubi_tests.py

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


start latency command tb.config.tc_xenomai_latency_lcmd_ from the xenomai

tools. Use paramter -g for creating histogram to file

tb.config.tc_xenomai_latency_tmpfile_ in gnuplot format.

Save this file into tb.config.tc_xenomai_latency_datfile2_

on the lab PC.


While latency test is running, extract the content of the

line starting with "RTD" into the file

tb.config.tc_xenomai_latency_datfile_


This testcase runs the latency tool until tb.config.tc_xenomai_latency_count_

lines are read. While running it checks if the value

of the column "lat max" is lower than tb.config.tc_xenomai_latency_max_

Than this testcase ends with True, else Testcase ends with False.


If the value from column 'overrun' != 0 Testcase fails.


At the end of this tetscase, it creates the png images

of the files tb.config.tc_xenomai_latency_datfile_

and tb.config.tc_xenomai_latency_datfile2_ on the host PC

using gnuplot tool.


Therefore the files

src/files/balkenplot_lat_tbot.sem

src/files/balkenplot_latency.sem

are used.


:usedvar:`used variables`


.. _tb.config.tc_xenomai_latency_lcmd:

- tb.config.tc_xenomai_latency_lcmd

| latency command
| default: '/usr/xenomai/bin/latency'

.. _tb.config.tc_xenomai_latency_tmpfile:

- tb.config.tc_xenomai_latency_tmpfile

| if != 'none' add paramter "-g" to latency command
| with filename tb.config.tc_xenomai_latency_tmpfile_
| default: '/tmp/latency.dat'

.. _tb.config.tc_xenomai_latency_datfile:

- tb.config.tc_xenomai_latency_datfile

| name of latency results file on lab PC
| default: 'lat_tbot.dat'

.. _tb.config.tc_xenomai_latency_datfile2:

- tb.config.tc_xenomai_latency_datfile2

| name of latency results file on Host PC
| default: 'latency_tbot.dat'

.. _tb.config.tc_xenomai_latency_count:

- tb.config.tc_xenomai_latency_count

| number of lines containing 'RTD' read, before
| Testcase ends latency command.
| default: '100'

.. _tb.config.tc_xenomai_latency_max:

- tb.config.tc_xenomai_latency_max

| maximum value which is allowed in latency output column
| 'max'. If a value > tb.config.tc_xenomai_latency_max_
| Testcase fails with error.
| default: '42'

.. _tb.config.tc_xenomai_latency_opt:

- tb.config.tc_xenomai_latency_opt

| latency options added to tb.config.tc_xenomai_latency_lcmd_
| default: 'none'


------------------------------------------------


.. _tb_workfd_check_if_process_run_py:

linux/tb_workfd_check_if_process_run.py
=======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tb_workfd_check_if_process_run.py

check if proces with name

tb.config.tc_workfd_check_if_process_run_name_

runs


:usedvar:`used variables`


.. _tb.config.tc_workfd_check_if_process_run_name:

- tb.config.tc_workfd_check_if_process_run_name

| check if process with name tb.config.tc_workfd_check_if_process_run_name_
| runs.
| default: 'none'


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


The vars tb.config.compile_pc_ip,_ tb.config.compile_pc_user_

tb.config.connect_to_compilepc_ssh_opt,_ tb.config.connect_to_compilepc_ssh_cmd_prompt_

could also be a list of strings.


:usedvar:`used variables`


.. _tb.config.compile_pc_ip:

- tb.config.compile_pc_ip

| ip address to the compile PC
| default: ''

.. _tb.config.compile_pc_user:

- tb.config.compile_pc_user

| login user name of compile PC
| default:

.. _tb.config.connect_to_compilepc_ssh_opt:

- tb.config.connect_to_compilepc_ssh_opt

| ssh options for the ssh command for logging into compile PC
| default:

.. _tb.config.connect_to_compilepc_ssh_cmd_prompt:

- tb.config.connect_to_compilepc_ssh_cmd_prompt

| prompt of the compile PC, after login
| default:


------------------------------------------------

.. _tc_git_get_branch_commit_py:

linux/tc_git_get_branch_commit.py
=================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_git_get_branch_commit.py

get current branch, commit from git tree in directory

tb.config.tc_git_get_branch_commit_tree_


save values in

tb.config.tc_git_get_branch_commit_dirty_

tb.config.tc_git_get_branch_commit_branch_

tb.config.tc_git_get_branch_commit_commit_


:usedvar:`used variables`


.. _tb.config.tc_git_get_branch_commit_tree:

- tb.config.tc_git_get_branch_commit_tree

|  path to the git tree, for which infos get collected
|  default: ''

.. _tb.config.tc_git_get_branch_commit_dirty:

- tb.config.tc_git_get_branch_commit_dirty

| is tree tb.config.tc_git_get_branch_commit_tree_ dirty
| default: no default, get set on runtime of tc_git_get_branch_commit_py_

.. _tb.config.tc_git_get_branch_commit_branch:

- tb.config.tc_git_get_branch_commit_branch

| current branch of tree tb.config.tc_git_get_branch_commit_tree_
| default: no default, get set on runtime of tc_git_get_branch_commit_py_

.. _tb.config.tc_git_get_branch_commit_commit:

- tb.config.tc_git_get_branch_commit_commit

| current commit of tree tb.config.tc_git_get_branch_commit_tree_
| default: no default, get set on runtime of tc_git_get_branch_commit_py_


------------------------------------------------

.. _tc_linux_top_py:

linux/tc_linux_top.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_linux_top.py


This testcase starts the linux "top" command

with the top cmdline arguments tb.config.tc_linux_top_count_

and tb.config.tc_linux_top_sec_


and analyses the output and write them into the file

tb.config.tc_linux_top_filename_ in a gnuplot format.


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

tb.config.create_documentation_auto_ = 'linux_top'


:usedvar:`used variables`


.. _tb.config.tc_linux_top_count:

- tb.config.tc_linux_top_count

| top count argument
| default: '10'

.. _tb.config.tc_linux_top_sec:

- tb.config.tc_linux_top_sec

| top seconds argument
| default: '2'

.. _tb.config.tc_linux_top_filename:

- tb.config.tc_linux_top_filename

| filename where the results are stored
| default: 'top-stat.dat'



------------------------------------------------

.. _tc_lx_bonnie_py:

linux/tc_lx_bonnie.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_bonnie.py

run a bonnie test, if timer tc_workfd_check_tc_time_py_ timed out

- if bonnie is not installed, try to install bonnie with
|  tc_lx_bonnie_install_py_
- start bonnie on device tb.config.tc_lx_bonnie_dev_ with
|   size tb.config.tc_lx_bonnie_sz_

:usedvar:`used variables`


.. _tb.config.tc_lx_bonnie_dev:

- tb.config.tc_lx_bonnie_dev

| device used for bonnie
| default: '/dev/sda1'

.. _tb.config.tc_lx_bonnie_sz:

- tb.config.tc_lx_bonnie_sz

| bonnie size
| default: '968'


------------------------------------------------

.. _tc_lx_bonnie_install_py:

linux/tc_lx_bonnie_install.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_bonnie_install.py

get bonnie source and install it


go into tbot workdir with tc_workfd_goto_tbot_workdir_py_

check, if bonnie++ is installed.


if not, try to download and install it.



------------------------------------------------

.. _tc_lx_check_devmem2_py:

linux/tc_lx_check_devmem2.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_check_devmem2.py

simply check, if we have the devmem2 cmd

if not, try to find it


:usedvar:`used variables`


.. _tb.config.tc_lx_check_devmem2_path:

- tb.config.tc_lx_check_devmem2_path

| path to devmem2 command
| default: '/home/debian'


------------------------------------------------

.. _tc_lx_check_reg_file_py:

linux/tc_lx_check_reg_file.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_check_reg_file.py

checks if the default values in reg file tb.config.tc_lx_create_reg_file_name_

on the tbot host in tb.workdir have the same values, as the

registers on the board. Needs devmem2 installed.

format of the regfile:

regaddr mask type defval


If you have to call devmem2 with a "header"

set it through tb.config.devmem2_pre_

so on the bbb with original rootfs -> no devmem2 installed

so to use tc which use devmem2 you have to copy devmem2

bin to the rootfs, and start it with 'sudo ...'


ToDo: use the file from the lab host, not the tbot host


:usedvar:`used variables`


.. _tb.config.devmem2_pre:

- tb.config.devmem2_pre

| path to devmem2 command
| default: ''


------------------------------------------------

.. _tc_lx_check_usb_authorized_py:

linux/tc_lx_check_usb_authorized.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_check_usb_authorized.py

check if usb device tb.config.tc_lx_check_usb_authorized_ needs authorizing


:usedvar:`used variables`


.. _tb.config.tc_lx_check_usb_authorized:

- tb.config.tc_lx_check_usb_authorized

| usb device string
| default: 'usb 1-1'


------------------------------------------------

.. _tc_lx_cmd_and_grep_py:

linux/tc_lx_cmd_and_grep.py
===========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_cmd_and_grep.py


loop over the list of strings in the tb.config.tc_lx_cmd_and_grep_

"cmds" key.

for each command save the output in a temporary file, and

search that all strings in key="cmd" are in the temporary file.


:usedvar:`used variables`


.. _tb.config.tc_lx_cmd_and_grep:

- tb.config.tc_lx_cmd_and_grep

| dictionary with key="cmds" value is a list of commands.
| Each command get exectuted and in the command output
| the list of strings stored in the dictionary with the
| key=command get searched.
|
| example tb.config.tc_lx_cmd_and_grep_
| tc_lx_cmd_and_grep = {"cmds" : ["cat /proc/partitions",
| 				"cat /proc/mounts"],
| 		"cat /proc/partitions" :
|			[
|				"mmcblk0p1",
|				"mmcblk0p2",
|			]
| 		,
| 		"cat /proc/mounts" : [
| 			"/ squashfs ro,noatime 0 0",
| 			"tmp /tmp tmpfs rw,relatime 0 0",
| 		]}
|
| This will do:
| - "cat /proc/partitions > gnlmpf"
| - search if gnlmpf contains the strings "mmcblk0p1" and "mmcblk0p2"
| - "cat /proc/mounts > gnlmpf"
| - search if gnlmpf contains the strings
|   "/ squashfs ro,noatime 0 0"
|   "tmp /tmp tmpfs rw,relatime 0 0"
|


------------------------------------------------

.. _tc_lx_cpufreq_py:

linux/tc_lx_cpufreq.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_cpufreq.py

check if frequencies in tb.config.tc_lx_cpufreq_frequences_

are possible to set with cpufreq-info


:usedvar:`used variables`


.. _tb.config.tc_lx_cpufreq_frequences:

- tb.config.tc_lx_cpufreq_frequences

| list of frequencies
| default: "['294']"


------------------------------------------------

.. _tc_lx_create_dummy_file_py:

linux/tc_lx_create_dummy_file.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_create_dummy_file.py

create a random dummy file tb.tc_lx_dummy_file_tempfile in tb.config.lab_tmp_dir_

on tb.c_con with bs = tb.tc_lx_dummy_file_bs and

count = tb.tc_lx_dummy_file_count


:usedvar:`used variables`


.. _tb.config.tc_lx_dummy_file_tempfile:

- tb.config.tc_lx_dummy_file_tempfile

| name of the created dummy file
| testcase tc_lx_create_dummy_file_py_ adds fullpath
| default: ''

.. _tb.config.tc_lx_dummy_file_bs:

- tb.config.tc_lx_dummy_file_bs

| dd bs paramter
| default: ''

.. _tb.config.tc_lx_dummy_file_count:

- tb.config.tc_lx_dummy_file_count

| dd count paramter
| default: ''


------------------------------------------------

.. _tc_lx_create_reg_file_py:

linux/tc_lx_create_reg_file.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_create_reg_file.py

creates a reg file tb.config.tc_lx_create_reg_file_name_ on the tbot host

in tb.workdir

read from tb.config.tc_lx_create_reg_file_start_ to tb.config.tc_lx_create_reg_file_stop_

and writes the results in the regfile

format of the regfile:

regaddr mask type defval

This reg file can be used as a default file, how the

registers must be setup, check it with testcase

tc_lx_check_reg_file_py_


If you have to call devmem2 with a "header"

set it through tb.config.devmem2_pre_

so on the bbb with original rootfs -> no devmem2 installed

so to use tc which use devmem2 you have to copy devmem2

bin to the rootfs, and start it with 'sudo ...'


ToDo: use the file from the lab host, not the tbot host


:usedvar:`used variables`


.. _tb.config.tc_lx_create_reg_file_name:

- tb.config.tc_lx_create_reg_file_name

| name of the register file
| default: 'pinmux.reg'

.. _tb.config.tc_lx_create_reg_file_start:

- tb.config.tc_lx_create_reg_file_start

| start address of registerdump
| default: '0x44e10800'

.. _tb.config.tc_lx_create_reg_file_stop:

- tb.config.tc_lx_create_reg_file_stop

| end address for register dump
| default: '0x44e10a34'

.. _tb.config.tc_lx_readreg_mask:

- tb.config.tc_lx_readreg_mask

| used mask
| default: '0xffffffff'

.. _tb.config.tc_lx_readreg_type:

- tb.config.tc_lx_readreg_type

| devmem2 type for reading register
| default: 'w'


------------------------------------------------

.. _tc_lx_devmem2_install_py:

linux/tc_lx_devmem2_install.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_devmem2_install.py

get devmem2 source from www.lartmaker.nl/lartware/port/devmem2.c

and install it


------------------------------------------------

.. _tc_lx_dmesg_grep_py:

linux/tc_lx_dmesg_grep.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_dmesg_grep.py


check if string tb.config.tc_lx_dmesg_grep_name_ is in dmesg output.

make the grep options configurable through tb.config.tc_lx_dmesg_grep_options_


:usedvar:`used variables`


.. _tb.config.tc_lx_dmesg_grep_name:

- tb.config.tc_lx_dmesg_grep_name

| string which must be in dmesg output
| default: ''

.. _tb.config.tc_lx_dmesg_grep_options:

- tb.config.tc_lx_dmesg_grep_options

|
| default: '--color=never'


------------------------------------------------

.. _tc_lx_eeprom_py:

linux/tc_lx_eeprom.py
=====================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_eeprom.py

Test an eeprom:

- read the content from eeprom @ tb.config.tc_lx_eeprom_tmp_dir_
with "cat" into tmpfile

- check tb.config.tc_lx_eeprom_wp_gpio_ != 'none'
if WP pin works

- generate random file with tb.config.tc_lx_eeprom_wp_sz_ size
- write it into eeprom
- reread it
- compare it with original
- restore original eeprom content at end

:usedvar:`used variables`


.. _tb.config.tc_lx_eeprom_file:

- tb.config.tc_lx_eeprom_file

| linux path to eeprom
| default: '/sys/class/i2c-dev/i2c-0/device/0-0050/eeprom'

.. _tb.config.tc_lx_eeprom_tmp_dir:

- tb.config.tc_lx_eeprom_tmp_dir

| temp directory, where eeprom content get stored
| default: tb.config.lab_tmp_dir_

.. _tb.config.tc_lx_eeprom_wp_gpio:

- tb.config.tc_lx_eeprom_wp_gpio

| if 'none' check only if eeprom is readable
| else check also if wp pin tb.config.tc_lx_eeprom_wp_gpio_ works
| default: 'none'

.. _tb.config.tc_lx_eeprom_wp_val:

- tb.config.tc_lx_eeprom_wp_val

| gpio protected state '0' or '1'
| default: '0'

.. _tb.config.tc_lx_eeprom_wp_sz:

- tb.config.tc_lx_eeprom_wp_sz

| size of eeprom test
| default: '4096'

.. _tb.config.tc_lx_eeprom_wp_obs:

- tb.config.tc_lx_eeprom_wp_obs

| dd obs size for writting into eeprom
| default: '32'

.. _tb.config.tc_lx_eeprom_wp_wc:

- tb.config.tc_lx_eeprom_wp_wc

| dd count size for writting into eeprom
| default: '128'


------------------------------------------------

.. _tc_lx_get_ubi_parameters_py:

linux/tc_lx_get_ubi_parameters.py
=================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_get_ubi_parameters.py

get ubi parameters of ubi device tb.config.tc_ubi_mtd_dev_

save them into:

tb.config.tc_ubi_max_leb_cnt_

tb.config.tc_ubi_min_io_size_

tb.config.tc_ubi_leb_size_


------------------------------------------------

.. _tc_lx_get_version_py:

linux/tc_lx_get_version.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_get_version.py

get the linux version and create event LINUX_VERSION

save the linux version in tb.config.tc_return_


------------------------------------------------

.. _tc_lx_gpio_py:

linux/tc_lx_gpio.py
===================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_gpio.py

set in linux gpio tb.config.tc_lx_gpio_nr_ to direction tb.config.tc_lx_gpio_dir_

and value tb.config.tc_lx_gpio_val_


:usedvar:`used variables`


.. _tb.config.tc_lx_gpio_nr:

- tb.config.tc_lx_gpio_nr

| gpio number
| default: '69'

.. _tb.config.tc_lx_gpio_dir:

- tb.config.tc_lx_gpio_dir

| direction to witch gpio get set 'in' or 'out'
| default: 'out'

.. _tb.config.tc_lx_gpio_val:

- tb.config.tc_lx_gpio_val

| state of gpio '0' or '1'
| default: '1'


------------------------------------------------

.. _tc_lx_mount_py:

linux/tc_lx_mount.py
====================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_mount.py

mount device tb.config.tc_lx_mount_dev_ with fs type tb.config.tc_lx_mount_fs_type_

to tb.config.tc_lx_mount_dir_


:usedvar:`used variables`


.. _tb.config.tc_lx_mount_dev:

- tb.config.tc_lx_mount_dev

| device which get mounted
| default: '/dev/sda1'

.. _tb.config.tc_lx_mount_fs_type:

- tb.config.tc_lx_mount_fs_type

| fs type for mount command
| default: 'ext4'


------------------------------------------------

.. _tc_lx_mtdutils_install_py:

linux/tc_lx_mtdutils_install.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_mtdutils_install.py

check if mtdutils are installed. If not, clone the code with

git clone git://git.infradead.org/mtd-utils.git mtd-utils

and install it into tb.config.tc_workfd_work_dir_


------------------------------------------------

.. _tc_lx_partition_check_py:

linux/tc_lx_partition_check.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_partition_check.py

cp a dummy file into a partiton umount/mount it and

compare it.

- Mount tb.config.tc_lx_mount_dir_ with tc_lx_mount_py_

------------------------------------------------

.. _tc_lx_partitions_grep_py:

linux/tc_lx_partitions_grep.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_partitions_grep.py


check, if all strings in tb.config.tc_lx_ps_partitions_ are

in "cat /proc/partitions" output.


:usedvar:`used variables`


.. _tb.config.tc_lx_ps_partitions:

- tb.config.tc_lx_ps_partitions

| list of strings, which must be in ps output
| default: '[]'


------------------------------------------------

.. _tc_lx_printenv_py:

linux/tc_lx_printenv.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_printenv.py

simple printenv linux command


------------------------------------------------

.. _tc_lx_ps_grep_py:

linux/tc_lx_ps_grep.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_ps_grep.py


check, if all strings in tb.config.tc_lx_ps_grep_ are

in ps output.



:usedvar:`used variables`


.. _tb.config.tc_lx_ps_grep:

- tb.config.tc_lx_ps_grep

| list of strings, which must be in ps output
| default: '[]'


------------------------------------------------

.. _tc_lx_regulator_py:

linux/tc_lx_regulator.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_regulator.py

check if regulators in tb.config.tc_lx_regulator_nrs_ exist, and have

the correct microvolts settings.


:usedvar:`used variables`


.. _tb.config.tc_lx_regulator_nrs:

- tb.config.tc_lx_regulator_nrs

| list of regulator strings. one string has 3 values
| seperated by a space:
| regulator_number name microvoltsvalue
| default:


------------------------------------------------

.. _tc_lx_trigger_wdt_py:

linux/tc_lx_trigger_wdt.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_trigger_wdt.py

simple trigger wdt with command tb.config.tc_lx_trigger_wdt_cmd_


:usedvar:`used variables`


.. _tb.config.tc_lx_trigger_wdt_cmd:

- tb.config.tc_lx_trigger_wdt_cmd

| command with which wdt gets triggered.
| default: '/home/hs/wdt &'


------------------------------------------------

.. _tc_lx_uname_py:

linux/tc_lx_uname.py
====================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_lx_uname.py

simple linux "uname -a" command


------------------------------------------------

.. _tc_workfd_apply_local_patches_py:

linux/tc_workfd_apply_local_patches.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_apply_local_patches.py

apply patches from directory tb.config.tc_workfd_apply_local_patches_dir_

with 'git am -3' to the source in current directory.


if tb.config.tc_workfd_apply_local_patches_dir_ == 'none'

do nothing.


if tb.config.tc_workfd_apply_local_patches_checkpatch_cmd_ != 'none'

check the patches with the checkpatch cmd tb.config.tc_workfd_apply_local_patches_checkpatch_cmd_

before applying.


:usedvar:`used variables`


.. _tb.config.tc_workfd_apply_local_patches_dir:

- tb.config.tc_workfd_apply_local_patches_dir

| path to patches which testcase should apply with "git am -3"
| default: 'none'

.. _tb.config.tc_workfd_apply_local_patches_checkpatch_cmd:

- tb.config.tc_workfd_apply_local_patches_checkpatch_cmd

| if != 'none' contains command for checking patch
| for styling errors (normaly with checkpatch)
| default: 'none'

.. _tb.config.tc_workfd_apply_local_patches_checkpatch_cmd_strict:

- tb.config.tc_workfd_apply_local_patches_checkpatch_cmd_strict

| if 'yes' return testcase with failure if checkpatch finds
| errors.
| default: 'no'


------------------------------------------------

.. _tc_workfd_apply_patchwork_patches_py:

linux/tc_workfd_apply_patchwork_patches.py
==========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_apply_patchwork_patches.py

apply patchworkpatches from list:

tb.config.tc_workfd_apply_patchwork_patches_list:_

to source in current directory.

creates event:

- PW_NR: which patchwork number used
- PW_CLEAN: is it checkpatch clean
- PW_AA: already applied
- PW_APPLY: apply it clean to source

:usedvar:`used variables`


.. _tb.config.tc_workfd_apply_patchwork_patches_list:

- tb.config.tc_workfd_apply_patchwork_patches_list

| list of patchwork numbers, which should be used with
| testcasetc_workfd_apply_patchwork_patches_py_
| default: '[]'

.. _tb.config.tc_workfd_apply_patchwork_patches_checkpatch_cmd:

- tb.config.tc_workfd_apply_patchwork_patches_checkpatch_cmd

| command with which the patches get checked
| default: 'none'

.. _tb.config.tc_workfd_apply_patchwork_patches_eof:

- tb.config.tc_workfd_apply_patchwork_patches_eof

| if 'yes' end testcase with failure, if applying fails.
| default: 'yes'


------------------------------------------------

.. _tc_workfd_can_py:

linux/tc_workfd_can.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_can.py


minimal can test:

starts a new connection named tb_canm. This connection runs

on board/PC which has a can conncetion to the board tbot

tests, named CAN PC.

If necessary (tb.config.tc_workfd_can_ssh_ != 'no'), tc connects first

to ssh (if the CAN PC is not the lab PC). Also if necessary

(tb.config.tc_workfd_can_su_ != 'no', switch to superuser on the CAN PC.


Set on the CAN PC, with the "ip" command the bitrate

tb.config.tc_workfd_can_bitrate_ for the can device tb.config.tc_workfd_can_dev_

and activate the interface.


Now on the board, go into tb.config.tc_workfd_can_iproute_dir_

(which contains the "ip" command ...

Set the bitrate with it and activate the can interface.

Goto into tb.config.tc_workfd_can_util_dir_ which contains canutils

Send '123#DEADBEEF' with cansend


check if the CAN PC gets this string.

End True if this is the case, False else


ToDo:

- get rid of tb.config.tc_workfd_can_iproute_dir_ and tb.config.tc_workfd_can_util_dir_
(add the commands to rootfs ...)

- support different can devices on the CAN PC and board

:usedvar:`used variables`


.. _tb.config.tc_workfd_can_ssh:

- tb.config.tc_workfd_can_ssh

| if != 'no' first ssh to PC on which we have can adapter
| default: 'no'

.. _tb.config.tc_workfd_can_ssh_prompt:

- tb.config.tc_workfd_can_ssh_prompt

| default login prompt after login
| default: '$'

.. _tb.config.tc_workfd_can_su:

- tb.config.tc_workfd_can_su

| do we nned sudo for can utilities
| default: 'no'

.. _tb.config.tc_workfd_can_iproute_dir:

- tb.config.tc_workfd_can_iproute_dir

| path to iproute2 utilities
| default: '/home/hs/iproute2'

.. _tb.config.tc_workfd_can_util_dir:

- tb.config.tc_workfd_can_util_dir

| path to can utilities
| default: '/home/hs/can-utils'

.. _tb.config.tc_workfd_can_dev:

- tb.config.tc_workfd_can_dev

| can device used
| default: 'can0'

.. _tb.config.tc_workfd_can_bitrate:

- tb.config.tc_workfd_can_bitrate

| can bitrate used for test
| default: '500000'


------------------------------------------------

.. _tc_workfd_cd_to_dir_py:

linux/tc_workfd_cd_to_dir.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_cd_to_dir.py

simple cd into directory tb.config.tc_workfd_cd_name_


:usedvar:`used variables`


.. _tb.config.tc_workfd_cd_name:

- tb.config.tc_workfd_cd_name

| name of path
| default: 'none'


------------------------------------------------

.. _tc_workfd_check_cmd_success_py:

linux/tc_workfd_check_cmd_success.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_cmd_success.py

simple check if previous shell command was succesful


------------------------------------------------

.. _tc_workfd_check_if_cmd_exist_py:

linux/tc_workfd_check_if_cmd_exist.py
=====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_if_cmd_exist.py

check if a command tb.config.tc_workfd_check_if_cmd_exist_cmdname_

exists


:usedvar:`used variables`


.. _tb.config.tc_workfd_check_if_cmd_exist_cmdname:

- tb.config.tc_workfd_check_if_cmd_exist_cmdname

| command name which gets checked
| default: 'none'


------------------------------------------------

.. _tc_workfd_check_if_device_exist_py:

linux/tc_workfd_check_if_device_exist.py
========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_if_device_exist.py

check if a device tb.config.tc_workfd_check_if_device_exists_name_ exist

this tc returns always true, but sets

tb.config.tc_return_ True or False, because we may not

want to end testcase failed, if device not exists.


:usedvar:`used variables`


.. _tb.config.tc_workfd_check_if_device_exists_name:

- tb.config.tc_workfd_check_if_device_exists_name

| device name
| default: ''


------------------------------------------------

.. _tc_workfd_check_if_dir_exist_py:

linux/tc_workfd_check_if_dir_exist.py
=====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_if_dir_exist.py

check if a dir in tbot workdir exist

this tc returns always true, but sets

tb.config.tc_return_ True or False, because we may not

want to end testcase failed, if dir not exists.


if tb.config.tc_workfd_check_if_dir_exists_create_ != 'no'

create the directory.



:usedvar:`used variables`


.. _tb.config.tc_workfd_check_if_dir_exists_name:

- tb.config.tc_workfd_check_if_dir_exists_name

| name of directory
| default: 'mtd-utils'

.. _tb.config.tc_workfd_check_if_dir_exists_create:

- tb.config.tc_workfd_check_if_dir_exists_create

| if 'yes' create directory if it does not exist
| default: 'no'


------------------------------------------------

.. _tc_workfd_check_if_file_exist_py:

linux/tc_workfd_check_if_file_exist.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_if_file_exist.py

check if a file in tbot workdir exist


:usedvar:`used variables`


.. _tb.config.tc_workfd_check_if_file_exists_name:

- tb.config.tc_workfd_check_if_file_exists_name

| filename
| default: 'bonnie++-1.03e.tgz'


------------------------------------------------

.. _tc_workfd_check_tar_content_py:

linux/tc_workfd_check_tar_content.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_tar_content.py

check if the strings in the tb.config.tc_workfd_check_tar_content_elements_

list are in the tar file tb.config.tc_workfd_check_tar_content_path_


tb.config.tc_workfd_check_tar_content_path_ path and file name

tb.config.tc_workfd_check_tar_content_elements_ list of elements in the tar file

tb.config.tc_workfd_check_tar_content_endtc_onerror_ end TC when element is not found


:usedvar:`used variables`


.. _tb.config.tc_workfd_check_tar_content_path:

- tb.config.tc_workfd_check_tar_content_path

| tar file with full path
| default: ''

.. _tb.config.tc_workfd_check_tar_content_elements:

- tb.config.tc_workfd_check_tar_content_elements

| list of elements which must be in tar file
| default: ''

.. _tb.config.tc_workfd_check_tar_content_endtc_onerror:

- tb.config.tc_workfd_check_tar_content_endtc_onerror

| if 'yes' end testcase with failure
| default: 'yes'


------------------------------------------------

.. _tc_workfd_check_tc_time_py:

linux/tc_workfd_check_tc_time.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_check_tc_time.py

check if time for a special testcase is expired.

some testcases (like writting in a flash) are not good for

execute them every day, so give them a timeout. This testcase

checks, if the testcases is ready for a new run.

False means time is not expired

True means time is expired


:usedvar:`used variables`


.. _tb.config.tc_workfd_check_tc_time_tcname:

- tb.config.tc_workfd_check_tc_time_tcname

| tc name
| default: ''

.. _tb.config.tc_workfd_check_tc_time_timeout:

- tb.config.tc_workfd_check_tc_time_timeout

| timeout in seconds
| default: '2592000' which is 30 days


------------------------------------------------

.. _tc_workfd_compile_linux_py:

linux/tc_workfd_compile_linux.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_compile_linux.py

compile linux:

- set toolchain with tc_lab_set_toolchain_py_
- if tb.config.tc_workfd_compile_linux_clean_ == 'yes'
call "make mrproper"

- tb.config.tc_workfd_compile_linux_load_addr_ != 'no'
add LOAD_ADDR=tb.config.tc_workfd_compile_linux_load_addr_ to make

- make tb.config.tc_workfd_compile_linux_boardname_ defconfig
- make tb.config.tc_workfd_compile_linux_makeoptions_ tb.config.tc_workfd_compile_linux_make_target_
- if tb.config.tc_workfd_compile_linux_modules_ != 'none'
compile modules

- if tb.config.tc_workfd_compile_linux_dt_name_ != 'none'
compile DTB from list tb.config.tc_workfd_compile_linux_dt_name_

- if tb.config.tc_workfd_compile_linux_fit_its_file_ != 'no'
create FIT image

mkimage path: tb.config.tc_workfd_compile_linux_mkimage_

fit description file: tb.config.tc_workfd_compile_linux_fit_its_file_

tb.config.tc_workfd_compile_linux_fit_file_

- if tb.config.tc_workfd_compile_linux_append_dt_ != 'no'
append dtb to kernel image

tb.config.tc_workfd_compile_linux_boardname_ _defconfig


:usedvar:`used variables`


.. _tb.config.tc_workfd_compile_linux_clean:

- tb.config.tc_workfd_compile_linux_clean

| if 'yes' call 'make mrproper'
| default: 'yes'

.. _tb.config.tc_workfd_compile_linux_load_addr:

- tb.config.tc_workfd_compile_linux_load_addr

| if != 'no' add LOADADDR= before make
| default: 'no'

.. _tb.config.tc_workfd_compile_linux_makeoptions:

- tb.config.tc_workfd_compile_linux_makeoptions

| string of makeoptions
| default: 'none'

.. _tb.config.tc_workfd_compile_linux_make_target:

- tb.config.tc_workfd_compile_linux_make_target

| make target normally zImage or uImage
| default: 'uImage'

.. _tb.config.tc_workfd_compile_linux_fit_its_file:

- tb.config.tc_workfd_compile_linux_fit_its_file

| if != 'no' create fit image
| its file is tb.config.tc_workfd_compile_linux_fit_its_file_
| output file is tb.config.tc_workfd_compile_linux_fit_file_
| default: 'no'

.. _tb.config.tc_workfd_compile_linux_fit_file:

- tb.config.tc_workfd_compile_linux_fit_file

| output file name if creating fit image
| default: 'no'

.. _tb.config.tc_workfd_compile_linux_boardname:

- tb.config.tc_workfd_compile_linux_boardname

| name for the used defconfig (without '_defconfig')
| default: tb.config.boardname_

.. _tb.config.tc_workfd_compile_linux_modules:

- tb.config.tc_workfd_compile_linux_modules

| if != 'none' build modules
| default: 'none'

.. _tb.config.tc_workfd_compile_linux_modules_path:

- tb.config.tc_workfd_compile_linux_modules_path

| if != 'none' contains modules path for 'make modules_install' step
| INSTALL_MOD_PATH=tb.config.tc_workfd_compile_linux_modules_path_
| default: 'none'

.. _tb.config.tc_workfd_compile_linux_dt_name:

- tb.config.tc_workfd_compile_linux_dt_name

| contains a string or a list of strings of
| dtb targets
| default: 'none'

.. _tb.config.tc_workfd_compile_linux_append_dt:

- tb.config.tc_workfd_compile_linux_append_dt

| if != 'no' append tb.config.tc_workfd_compile_linux_dt_name_
| to 'z' + tb.config.tc_workfd_compile_linux_append_dt_
| default: 'no'

.. _tb.config.tc_workfd_compile_linux_mkimage:

- tb.config.tc_workfd_compile_linux_mkimage

| path to mkimage tool (incl. mkimage)
| default: '/home/hs/i2c/u-boot/tools/mkimage'


------------------------------------------------

.. _tc_workfd_connect_with_conmux_py:

linux/tc_workfd_connect_with_conmux.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_connect_with_conmux.py

connect to console with conmux

Never tested !!!


------------------------------------------------

.. _tc_workfd_connect_with_kermit_py:

linux/tc_workfd_connect_with_kermit.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_connect_with_kermit.py

connect with kermit to serials board console

- if tb.config.tc_workfd_connect_with_kermit_ssh_ != 'none'
connect first with ssh to another PC (where kermit is started)

- start kermit
- if tb.config.tc_workfd_connect_with_kermit_rlogin_ == 'none'
set line tb.config.kermit_line_ and speed tb.config.kermit_speed_ and

kermit parameter list tb.config.tc_workfd_connect_with_kermit_settings_

than connect to serial line.

else

connect with command in tb.config.tc_workfd_connect_with_kermit_rlogin_

- if you need sudo rights set tb.config.tc_workfd_connect_with_kermit_sudo_ = 'yes'
and a sudo is preceded to kermit.

the sudo password is searched with

user:  tb.config.user_ + '_kermit'

board: tb.config.boardname_



:usedvar:`used variables`


.. _tb.config.kermit_line:

- tb.config.kermit_line

| used serial linux device
| default: '/dev/ttyUSB0'

.. _tb.config.kermit_speed:

- tb.config.kermit_speed

| serial line speed
| default: '115200'

.. _tb.config.tc_workfd_connect_with_kermit_ssh:

- tb.config.tc_workfd_connect_with_kermit_ssh

| call tc_workfd_ssh_py_ with
| tb.config.workfd_ssh_cmd_ = tb.config.tc_workfd_connect_with_kermit_ssh_
| default: 'none'

.. _tb.config.tc_workfd_connect_with_kermit_sudo:

- tb.config.tc_workfd_connect_with_kermit_sudo

| use sudo for kermit
| default: 'none'

.. _tb.config.tc_workfd_connect_with_kermit_rlogin:

- tb.config.tc_workfd_connect_with_kermit_rlogin

| rlogin string for kermit. If != 'none'
| do not 'set line', 'set speed' and 'connect'
| default: 'none'

.. _tb.config.tc_workfd_connect_with_kermit_settings:

- tb.config.tc_workfd_connect_with_kermit_settings

| list of additionally kermit parameter, which get
| set after 'set line' and 'set speed'
| default: '["set carrier-watch off",
|        "set handshake none",
|        "set flow-control none",
|        "robust",
|        "set file type bin",
|        "set file name lit",
|        "set rec pack 1000",
|        "set send pack 1000",
|        "set window 5",
|    ]'


------------------------------------------------

.. _tc_workfd_connect_with_ssh_py:

linux/tc_workfd_connect_with_ssh.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_connect_with_ssh.py


connect wit ssh to board, and use it as console


:usedvar:`used variables`


.. _tb.config.connect_with_ssh_user:

- tb.config.connect_with_ssh_user

| username for connecting to boards "console"
| default: 'root'

.. _tb.config.connect_with_ssh_ip:

- tb.config.connect_with_ssh_ip

| ip to connect with
| default: '192.168.3.23'


------------------------------------------------

.. _tc_workfd_cp_file_py:

linux/tc_workfd_cp_file.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_cp_file.py

simple copy file from tb.config.tc_workfd_cp_file_from_ to tb.config.tc_workfd_cp_file_to_


:usedvar:`used variables`


.. _tb.config.tc_workfd_cp_file_from:

- tb.config.tc_workfd_cp_file_from

| source path + filename
| default: ''

.. _tb.config.tc_workfd_cp_file_to:

- tb.config.tc_workfd_cp_file_to

| target path + filename
| default: ''


------------------------------------------------

.. _tc_workfd_create_ubi_rootfs_py:

linux/tc_workfd_create_ubi_rootfs.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_create_ubi_rootfs.py

create a ubifs rootfs

ubi rootfs path: tb.config.tc_workfd_create_ubi_rootfs_path_

ubi parameters:

tb.config.tc_ubi_min_io_size_ tb.config.tc_ubi_leb_size_ tb.config.tc_ubi_max_leb_cnt_

output path: tb.config.tc_workfd_create_ubi_rootfs_target_


:usedvar:`used variables`


.. _tb.config.tc_workfd_create_ubi_rootfs_path:

- tb.config.tc_workfd_create_ubi_rootfs_path

| path into which the ubifs image with name
| tb.config.tc_workfd_create_ubi_rootfs_target_ get created
| default: '/opt/eldk-5.4/armv7a-hf/rootfs-minimal-mtdutils'

.. _tb.config.tc_workfd_create_ubi_rootfs_target:

- tb.config.tc_workfd_create_ubi_rootfs_target

| name of the ubi image which get created
| default: '/tftpboot/dxr2/tbot/rootfs-minimal.ubifs'


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


don;t forget to describe here variables you use in

your testcase. Format


- tb.config.varname_
|  some text, which describes the function of the variable
|  default: and of course, say what is the default value


------------------------------------------------

.. _tc_workfd_disconnect_with_kermit_py:

linux/tc_workfd_disconnect_with_kermit.py
=========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_disconnect_with_kermit.py

disconnect from a kermit connection

and set linux prompt.


------------------------------------------------

.. _tc_workfd_generate_random_file_py:

linux/tc_workfd_generate_random_file.py
=======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_generate_random_file.py

simple create a random file tb.tc_workfd_generate_random_file_name

with tb.tc_workfd_generate_random_file_length length.


:usedvar:`used variables`


.. _tb.config.tc_workfd_generate_random_file_name:

- tb.config.tc_workfd_generate_random_file_name

| name of random file which get created
| default: ''

.. _tb.config.tc_workfd_generate_random_file_length:

- tb.config.tc_workfd_generate_random_file_length

| lenght in bytes which get created
| default: ''


------------------------------------------------

.. _tc_workfd_get_linux_source_py:

linux/tc_workfd_get_linux_source.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_get_linux_source.py

get Linux source tb.config.tc_lab_get_linux_source_git_repo_ with "git clone"

and go into the source tree.

check out branch tc_lab_get_linux_source_git_branch if tc_lab_get_linux_source_git_commit_id == 'none'

else checkout commit tc_lab_get_linux_source_git_commit_id

Apply patches if needed with:

tc_lab_apply_patches_py_ and tc_workfd_apply_local_patches_py_


:usedvar:`used variables`


.. _tb.config.tc_lab_get_linux_source_git_repo:

- tb.config.tc_lab_get_linux_source_git_repo

| git repo to checkout
| default: '/home/git/linux.git'

.. _tb.config.tc_lab_get_linux_source_git_branch:

- tb.config.tc_lab_get_linux_source_git_branch

| branch which get checkout
| default: 'master'

.. _tb.config.tc_lab_get_linux_source_git_reference:

- tb.config.tc_lab_get_linux_source_git_reference

| if != 'none' add --reference option to git clone
| default: 'none'

.. _tb.config.tc_lab_get_linux_source_git_commit_id:

- tb.config.tc_lab_get_linux_source_git_commit_id

| if != 'none' checkout commit id instead branch
| default: 'none'

.. _tb.config.tc_lab_get_linux_source_git_repo_user:

- tb.config.tc_lab_get_linux_source_git_repo_user

| if a username is needed for cloning
| password comes from password_py_
| default: 'none'


------------------------------------------------

.. _tc_workfd_get_list_of_files_in_dir_py:

linux/tc_workfd_get_list_of_files_in_dir.py
===========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_get_list_of_files_in_dir.py

get a list of files from directory tb.config.tc_workfd_get_list_of_files_dir_

tb.config.tc_workfd_get_list_of_files_mask_


:usedvar:`used variables`


.. _tb.config.tc_workfd_get_list_of_files_dir:

- tb.config.tc_workfd_get_list_of_files_dir

| directory in which files get searched
| default: ''

.. _tb.config.tc_workfd_get_list_of_files_mask:

- tb.config.tc_workfd_get_list_of_files_mask

| find expression
| default: '\*'


------------------------------------------------

.. _tc_workfd_get_patchwork_number_list_py:

linux/tc_workfd_get_patchwork_number_list.py
============================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_get_patchwork_number_list.py

get a list of patchworknumbers

which are delegated to specific user

tb.config.workfd_get_patchwork_number_user_

currently, this testcase reads "http://patchwork.ozlabs.org/project/uboot/list/"

and filters out the patches, which are for

tb.config.workfd_get_patchwork_number_user_

It would be better to login and look for the users

ToDo list, but I did not find out, how to login ...

ignore patches on blacklist:

tb.config.tc_workfd_apply_patchwork_patches_blacklist_

also you can set the patch order with:

tb.config.tc_workfd_get_patchwork_number_list_order_


:usedvar:`used variables`


.. _tb.config.workfd_get_patchwork_number_user:

- tb.config.workfd_get_patchwork_number_user

| patchwork username
| default: 'hs'

.. _tb.config.tc_workfd_apply_patchwork_patches_blacklist:

- tb.config.tc_workfd_apply_patchwork_patches_blacklist

| patchwork numbers, which get ignored
| default: '[]'

.. _tb.config.tc_workfd_get_patchwork_number_list_order:

- tb.config.tc_workfd_get_patchwork_number_list_order

| ?order= parameter for request patchwork page
| default: '-delegate'


------------------------------------------------

.. _tc_workfd_get_uboot_config_hex_py:

linux/tc_workfd_get_uboot_config_hex.py
=======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_get_uboot_config_hex.py

get a hex parameter from U-Boot configuration


return value:

TC ends True, if hex value found, else False

tb.config_result: founded hex value, else 'undef'


------------------------------------------------

.. _tc_workfd_get_uboot_config_string_py:

linux/tc_workfd_get_uboot_config_string.py
==========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_get_uboot_config_string.py

start with

get a string parameter from U-Boot configuration


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


'CONFIG_SYS_SDRAM_BASE' saved in tb.config.tc_ub_memory_ram_ws_base_

tb.config.tc_ub_memory_ram_ws_base_alt_ = tc_ub_memory_ram_ws_base + 0x100000

tb.config.tc_ub_memory_ram_big_ depended on CONFIG_SYS_ARCH

if CONFIG_SYS_ARCH == powerpc than yes else no


:usedvar:`used variables`


.. _tb.config.tc_ub_memory_ram_ws_base:

- tb.config.tc_ub_memory_ram_ws_base

| base address for memory tests in RAM
| if 'undef' testcase tc_workfd_get_uboot_config_vars_py_
| try to detect a good value from U-Boot config
| default: 'undef'

.. _tb.config.tc_ub_memory_ram_ws_base_alt:

- tb.config.tc_ub_memory_ram_ws_base_alt

| alternate address in RAM for memory tests
| if 'undef' testcase tc_workfd_get_uboot_config_vars_py_
| try to detect a good value from U-Boot config
| default: 'undef'

.. _tb.config.tc_ub_memory_ram_big:

- tb.config.tc_ub_memory_ram_big

| big or little endian
| if 'undef' testcase tc_workfd_get_uboot_config_vars_py_
| try to detect a good value from U-Boot config
| default: 'undef'

.. _tb.config.tc_ub_memory_base:

- tb.config.tc_ub_memory_base

| only output the content of the 'help base' and
| 'base' and 'md tb.config.tc_ub_memory_ram_ws_base_ 0xc'
| command.
| default: 'yes'


------------------------------------------------

.. _tc_workfd_git_rebase_py:

linux/tc_workfd_git_rebase.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_git_rebase.py


go into git source tree tb.config.tc_workfd_git_rebase_git_src_path_

checkout branch tb.config.tc_workfd_git_rebase_git_base_branch_

call "git fetch" and "git pull"

checkout branch tb.config.tc_workfd_git_rebase_git_work_branch_

and rebase tb.config.tc_workfd_git_rebase_git_work_branch_ with

tb.config.tc_workfd_git_rebase_git_base_branch_


:usedvar:`used variables`


.. _tb.config.tc_workfd_git_rebase_git_src_path:

- tb.config.tc_workfd_git_rebase_git_src_path

| path to source tree
| default: ''

.. _tb.config.tc_workfd_git_rebase_git_base_branch:

- tb.config.tc_workfd_git_rebase_git_base_branch

| branch name, which get rebased against tb.config.tc_workfd_git_rebase_git_work_branch_
| default: ''

.. _tb.config.tc_workfd_git_rebase_git_work_branch:

- tb.config.tc_workfd_git_rebase_git_work_branch

| branch name with which tb.config.tc_workfd_git_rebase_git_base_branch_ gets rebased
| default: ''


------------------------------------------------

.. _tc_workfd_goto_lab_source_dir_py:

linux/tc_workfd_goto_lab_source_dir.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_goto_lab_source_dir.py

switch into lab PC source directory tb.config.tc_lab_source_dir_

set TBOT_BASEDIR to tb.config.tc_lab_source_dir_


if workfd == 'tb_cpc' go into workdirectory

on compile PC, and set there TBOT_BASEDIR to tb.config.compile_pc_workdir_



------------------------------------------------

.. _tc_workfd_goto_linux_code_py:

linux/tc_workfd_goto_linux_code.py
==================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_goto_linux_code.py

switch into linux source tb.config.tc_lab_source_dir_ + "/linux-" + tb.config.boardlabname_

set tb.config.linux_name_ to "linux-" + tb.config.boardlabname_

and tb.config.linux_fulldir_name_ to tb.config.tc_lab_source_dir_ + "/" + tb.config.linux_name_

and set $TBOT_BASEDIR_LINUX to tb.config.linux_fulldir_name_


:usedvar:`used variables`


.. _tb.config.linux_name:

- tb.config.linux_name

| "linux-" + tb.config.boardlabname_
| directory in lab source dir
| default: get set from tc_workfd_goto_linux_code_py_


------------------------------------------------

.. _tc_workfd_goto_tbot_workdir_py:

linux/tc_workfd_goto_tbot_workdir.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_goto_tbot_workdir.py

go into the tbot work dir tb.config.tc_workfd_work_dir_

if not exist, create it


------------------------------------------------

.. _tc_workfd_goto_uboot_code_py:

linux/tc_workfd_goto_uboot_code.py
==================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_goto_uboot_code.py

switch into U-Boot source tb.config.tc_lab_source_dir_ + "/u-boot-" + tb.config.boardlabname_

set tb.config.uboot_name_ to "u-boot-" + tb.config.boardlabname_

and tb.config.uboot_fulldir_name_ to tb.config.tc_lab_source_dir_ + "/" + tb.config.uboot_name_

and set $TBOT_BASEDIR_UBOOT to tb.config.uboot_fulldir_name_



:usedvar:`used variables`


.. _tb.config.uboot_name:

- tb.config.uboot_name

| "u-boot-" + tb.config.boardlabname_
| default: set from testcase tc_workfd_goto_uboot_code_py_

.. _tb.config.uboot_fulldir_name:

- tb.config.uboot_fulldir_name

| "$TBOT_BASEDIR/" + tb.config.uboot_name_
| default: set from testcase tc_workfd_goto_uboot_code_py_


------------------------------------------------

.. _tc_workfd_grep_py:

linux/tc_workfd_grep.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_grep.py


search string tb.config.tc_workfd_grep_string_ in file tb.config.tc_workfd_grep_file_

grep options configurable through tb.config.tc_workfd_grep_option_

default '--color=never'


:usedvar:`used variables`


.. _tb.config.tc_workfd_grep_file:

- tb.config.tc_workfd_grep_file

| file in which we grep
| default: ''

.. _tb.config.tc_workfd_grep_string:

- tb.config.tc_workfd_grep_string

| string we search in file
| default: ''

.. _tb.config.tc_workfd_grep_option:

- tb.config.tc_workfd_grep_option

| grep options
| default: '--color=never'


------------------------------------------------

.. _tc_workfd_hdparm_py:

linux/tc_workfd_hdparm.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_hdparm.py

make a minimal hdparm check

call hdparm -t tb.config.tc_workfd_hdparm_dev_

and check if read speed is greater than tb.config.tc_workfd_hdparm_min_

It is possible to add a PATH tb.config.tc_workfd_hdparm_path_

where hdparm is installed

Testcase fails if readen speed is <= tb.config.tc_workfd_hdparm_min_


:usedvar:`used variables`


.. _tb.config.tc_workfd_hdparm_path:

- tb.config.tc_workfd_hdparm_path

| path to hdparm utility
| default: '/home/hs/shc/hdparm-9.50/'

.. _tb.config.tc_workfd_hdparm_dev:

- tb.config.tc_workfd_hdparm_dev

| hdparm device "-t tb.config.tc_workfd_hdparm_dev"_
| default: '/dev/mmcblk1'

.. _tb.config.tc_workfd_hdparm_min:

- tb.config.tc_workfd_hdparm_min

| Testcase fails if readen speed is <= tb.config.tc_workfd_hdparm_min_
| default: '12.0'


------------------------------------------------

.. _tc_workfd_insmod_py:

linux/tc_workfd_insmod.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_insmod.py

insmod module tb.config.tc_workfd_insmod_module_ with

module path tb.config.tc_workfd_insmod_mpath_ and

tb.config.tc_workfd_insmod_module_path_

check if the strings in list tb.config.tc_workfd_insmod_module_checks_

come back when inserting the module.


:usedvar:`used variables`


.. _tb.config.tc_workfd_insmod_module:

- tb.config.tc_workfd_insmod_module

| module name without '.ko'
| default: ''

.. _tb.config.tc_workfd_insmod_mpath:

- tb.config.tc_workfd_insmod_mpath

| path to modules
| default: ''

.. _tb.config.tc_workfd_insmod_module_path:

- tb.config.tc_workfd_insmod_module_path

| path to module
| default: ''

.. _tb.config.tc_workfd_insmod_module_checks:

- tb.config.tc_workfd_insmod_module_checks

| list of strings which must be found when loading module
| default: ''


------------------------------------------------

.. _tc_workfd_iperf_py:

linux/tc_workfd_iperf.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_iperf.py


make a minimal iperf check

starts an iperf server on tb.tc_workfd_c_sr connection

with ip addr tb.tc_workfd_iperf_sip

starts an iperf "slave" on tb.tc_workfd_c_sl

waiting for the first result of iperf measure and

check if the resulting speed is bigger then

tb.config.tc_workfd_iperf_minval_


if you have not the iperf cmd instead iperf 3, you can

set

tb.config.tc_workfd_c_sr_vers_ or tb.config.tc_workfd_c_sl_vers_

to '3'


:usedvar:`used variables`


.. _tb.config.tc_workfd_c_sr:

- tb.config.tc_workfd_c_sr

| tbot connection where iperf server is started
| default: ''

.. _tb.config.tc_workfd_c_sl:

- tb.config.tc_workfd_c_sl

| tbot connection where iperf slave is started
| default: ''
| default: ''

.. _tb.config.tc_workfd_iperf_sip:

- tb.config.tc_workfd_iperf_sip

| iperf server ip used for iperf slave
| default: ''

.. _tb.config.tc_workfd_iperf_minval:

- tb.config.tc_workfd_iperf_minval

| if iperf result is greater than tb.config.tc_workfd_iperf_minval_
| testcase tc_workfd_iperf_py_ returns True
| default: ''

.. _tb.config.tc_workfd_c_sr_vers:

- tb.config.tc_workfd_c_sr_vers

| iperf version
| default: ''

.. _tb.config.tc_workfd_c_sl_vers:

- tb.config.tc_workfd_c_sl_vers

| iperf version
| default: ''


------------------------------------------------

.. _tc_workfd_linux_get_ifconfig_py:

linux/tc_workfd_linux_get_ifconfig.py
=====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_linux_get_ifconfig.py

read from tb.config.linux_get_ifconfig_dev_ the current

ip addr and save it in tb.config.linux_get_ifconfig_ip_

broadcast and save it in tb.config.linux_get_ifconfig_broadcast_

mask and save it in tb.config.linux_get_ifconfig_mask_


:usedvar:`used variables`


.. _tb.config.linux_get_ifconfig_dev:

- tb.config.linux_get_ifconfig_dev

| network device, for which ip, mask and broadcast address get detected.
| default: ''

.. _tb.config.linux_get_ifconfig_ip:

- tb.config.linux_get_ifconfig_ip

| set from testcase tc_workfd_linux_get_ifconfig_py_
| contains current ip address from tb.config.linux_get_ifconfig_dev_
| default:

.. _tb.config.linux_get_ifconfig_broadcast:

- tb.config.linux_get_ifconfig_broadcast

| set from testcase tc_workfd_linux_get_ifconfig_py_
| contains current broadcast address from tb.config.linux_get_ifconfig_dev_
| default:

.. _tb.config.linux_get_ifconfig_mask:

- tb.config.linux_get_ifconfig_mask

| set from testcase tc_workfd_linux_get_ifconfig_py_
| contains current mask from tb.config.linux_get_ifconfig_dev_
| default:


------------------------------------------------

.. _tc_workfd_linux_get_uboot_env_py:

linux/tc_workfd_linux_get_uboot_env.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_linux_get_uboot_env.py

read U-Boot Environment variable from tb.config.linux_get_uboot_env_name_

from linux with fw_printenv, and save the value in tb.config.linux_get_uboot_env_value_


:usedvar:`used variables`


.. _tb.config.linux_get_uboot_env_name:

- tb.config.linux_get_uboot_env_name

| U-Boot Envvariable, which get read
| default: ''

.. _tb.config.linux_get_uboot_env_value:

- tb.config.linux_get_uboot_env_value

| get set from testcase tc_workfd_linux_get_uboot_env_py_
| default:


------------------------------------------------

.. _tc_workfd_linux_mkdir_py:

linux/tc_workfd_linux_mkdir.py
==============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_linux_mkdir.py

check if the directory tb.config.tc_workfd_linux_mkdir_dir_ exists.

if not, create it


:usedvar:`used variables`


.. _tb.config.tc_workfd_linux_mkdir_dir:

- tb.config.tc_workfd_linux_mkdir_dir

| directory which get created
| default:


------------------------------------------------

.. _tc_workfd_lx_get_bc_py:

linux/tc_workfd_lx_get_bc.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_lx_get_bc.py

get in linux bootcount value

through file tb.config.tc_workfd_lx_get_bc_file_

if not found testcases end with failure

value returned in var tb.lx_bc


------------------------------------------------

.. _tc_workfd_lx_set_bc_py:

linux/tc_workfd_lx_set_bc.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_lx_set_bc.py

set in linux bootcount value tb.lx_bc

through file tb.config.tc_workfd_lx_get_bc_file_


------------------------------------------------

.. _tc_workfd_md5sum_py:

linux/tc_workfd_md5sum.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_md5sum.py

calculate md5sum of file tb.config.tc_workfd_md5sum_name_ , and store it in

tb.tc_workfd_md5sum_sum


:usedvar:`used variables`


.. _tb.config.tc_workfd_md5sum_name:

- tb.config.tc_workfd_md5sum_name

| path with filename, for which md5sum gets calculated
| default:


------------------------------------------------

.. _tc_workfd_rm_dir_py:

linux/tc_workfd_rm_dir.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_rm_dir.py


remove the path tb.config.tc_lab_rm_dir_



------------------------------------------------

.. _tc_workfd_rm_file_py:

linux/tc_workfd_rm_file.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_rm_file.py

simple rm file tb.config.tc_workfd_rm_file_name_ on the lab


:usedvar:`used variables` tc_workfd_rm_file_name


.. _tb.config.tc_workfd_rm_file_name:

- tb.config.tc_workfd_rm_file_name

| filenam which get removed (call rm tb.config.tc_workfd_rm_file_name)_
| default: 'none'


------------------------------------------------

.. _tc_workfd_rm_linux_code_py:

linux/tc_workfd_rm_linux_code.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_rm_linux_code.py

rm linux source tb.config.tc_lab_source_dir_ + '/linux-' + tb.config.boardlabname_


------------------------------------------------

.. _tc_workfd_rm_uboot_code_py:

linux/tc_workfd_rm_uboot_code.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_rm_uboot_code.py

rm U-Boot source tb.config.tc_lab_source_dir_ + '/u-boot-' + tb.config.boardlabname_


------------------------------------------------

.. _tc_workfd_scp_py:

linux/tc_workfd_scp.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_scp.py


start an scp transfer

tb.config.tc_workfd_scp_opt:_ scp options

tb.config.tc_workfd_scp_from:_ from where

tb.config.tc_workfd_scp_to:_ to where


If the scp command asks for  "password" the testcase extracts

the user and ip from scp output "user@ip's password:"

and writes the password it find in password_py_ with


tb.write_stream_passwd(tb.workfd, user, ip)


to the scp command ... if no user and or ip

is found ... scp command fails and so the testcase.


An errorneous scp command exits with an error code.

check this error code when scp command finished,

and return True, if no error, else False.



:usedvar:`used variables`


.. _tb.config.tc_workfd_scp_opt:

- tb.config.tc_workfd_scp_opt

| if != 'none' contains scp option string
| default: 'none'

.. _tb.config.tc_workfd_scp_from:

- tb.config.tc_workfd_scp_from

| string from where scp copy
| default: ''

.. _tb.config.tc_workfd_scp_to:

- tb.config.tc_workfd_scp_to

| string to where scp copy
| default: ''


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


login with ssh to tb.config.workfd_ssh_cmd_ and ssh options

tb.config.tc_workfd_ssh_opt._

This testcases expects

tb.config.workfd_ssh_cmd_prompt_

as the prompt it get, after a succefull log in.

When logged in call

if tb.config.workfd_ssh_do_first_ == 'yes':

tb.do_first_settings_after_login(c)



:usedvar:`used variables`


.. _tb.config.workfd_ssh_cmd:

- tb.config.workfd_ssh_cmd

| ssh command string
| default:

.. _tb.config.workfd_ssh_cmd_prompt:

- tb.config.workfd_ssh_cmd_prompt

| prompt after successful ssh
| default: '$'

.. _tb.config.workfd_ssh_opt:

- tb.config.workfd_ssh_opt

| option string for ssh
| default: 'none'

.. _tb.config.workfd_ssh_do_first:

- tb.config.workfd_ssh_do_first

| if == 'yes', call
|     tb.do_first_settings_after_login(c)
| after successful login.
| default: 'yes'


------------------------------------------------

.. _tc_workfd_sudo_cp_file_py:

linux/tc_workfd_sudo_cp_file.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_sudo_cp_file.py

simple copy file from tb.config.tc_workfd_cp_file_from_ to tb.config.tc_workfd_cp_file_to_

with sudo rights


------------------------------------------------

.. _tc_workfd_switch_su_py:

linux/tc_workfd_switch_su.py
============================

https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_switch_su.py

switch to superuser with user 'root' and password

tb.config.switch_su_board_


:usedvar:`used variables`


.. _tb.config.switch_su_board:

- tb.config.switch_su_board

| boardname with which password get searched in password file.
| default: 'lab'


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

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/02_UBootBasic.tc;h=5503cc6c716d2748732d30d63b0801e651fe1706;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_bdinfo_py:

uboot/duts/tc_ub_bdinfo.py
,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_bdinfo.py

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootBdinfo.tc;h=aa794a93ac5c8d2c3aea4aa5d02433ca2ee0f010;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_boot_py:

uboot/duts/tc_ub_boot.py
,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_boot.py

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootBoot.tc;h=f679ff09cdb1e1393829c32dc5aa5cf299e9af07;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_coninfo_py:

uboot/duts/tc_ub_coninfo.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_coninfo.py

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootConinfo.tc;h=2d028f74ba791343b8a70a97885eabe8b5944017;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_date_py:

uboot/duts/tc_ub_date.py
,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_date.py

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootDate.tc;h=03b7d53fd93bd61381db4095a4bff58b1d1efff7;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_diskboothelp_py:

uboot/duts/tc_ub_diskboothelp.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_diskboothelp.py

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootIde.tc;h=03c2a05b75c6f9f6fc257fa84a2220f965567699;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_download_py:

uboot/duts/tc_ub_download.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_download.py

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootCmdGroupDownload.tc;h=8e58d53add90b680ef7a1300894d2392f90d9824;hb=101ddd5dbd547d5046363358d560149d873b238a


:usedvar:`used variables`


.. _tb.config.tc_ub_download_load:

- tb.config.tc_ub_download_load

| if != 'yes' do only show help output
| default: 'yes'

------------------------------------------------

.. _tc_ub_dtt_py:

uboot/duts/tc_ub_dtt.py
,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_dtt.py

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootDtt.tc;h=e420c7b45cd73b00465d69f969039222868f4cc7;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_duts_fdt_py:

uboot/duts/tc_ub_duts_fdt.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_duts_fdt.py

create logfiles used for DULG


http://www.denx.de/wiki/view/DULG/UBootCmdFDT



------------------------------------------------

.. _tc_ub_duts_go_py:

uboot/duts/tc_ub_duts_go.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_duts_go.py

do the commands needed for:


http://www.denx.de/wiki/view/DULG/UBootCmdGroupExec#Section_5.9.4.3.

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

do the commands needed for:


http://www.denx.de/wiki/view/DULG/UBootCmdGroupExec#Section_5.9.4.1.


U-Boots source command



------------------------------------------------

.. _tc_ub_duts_version_py:

uboot/duts/tc_ub_duts_version.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_duts_version.py


execute U-Boots "version" cmd, and create event

- DUTS_UBOOT_VERSION
- DUTS_SPL_VERSION
- DUTS_BOARDNAME = tb.config.boardlabpowername_


------------------------------------------------

.. _tc_ub_environment_py:

uboot/duts/tc_ub_environment.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_environment.py

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootEnvironment.tc;h=18d235f427e3efe9e6a04f870a3c5426d719ec58;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_flash_py:

uboot/duts/tc_ub_flash.py
,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_flash.py

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootFlashTest.tc;h=6eea72c8e9f3f4739a76ff59bb2e9a7c693aedd9;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_flinfo_py:

uboot/duts/tc_ub_flinfo.py
,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_flinfo.py

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootFlinfo.tc;h=f5b728258250211d86dc9c6a9208639d8542b845;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_i2c_help_py:

uboot/duts/tc_ub_i2c_help.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_i2c_help.py

simple prints "help i2c" cmd


:usedvar:`used variables`


.. _tb.config.tc_ub_i2c_help_with_bus:

- tb.config.tc_ub_i2c_help_with_bus

| if 'yes' i2c help output with "i2c bus"
| default: 'no'


------------------------------------------------

.. _tc_ub_ide_py:

uboot/duts/tc_ub_ide.py
,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_ide.py

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootIde.tc;h=03c2a05b75c6f9f6fc257fa84a2220f965567699;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_memory_py:

uboot/duts/tc_ub_memory.py
,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_memory.py

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootMemory.tc;h=f5fb055499db17c322859215ab489cefb063ac47;hb=101ddd5dbd547d5046363358d560149d873b238a



------------------------------------------------

.. _tc_ub_run_py:

uboot/duts/tc_ub_run.py
,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_run.py

convert duts tests from:


http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootRun.tc;h=44f8a0a0de256afdd95b5ec20d1d4570373aeb7d;hb=101ddd5dbd547d5046363358d560149d873b238a


------------------------------------------------

.. _tc_ub_start_all_duts_py:

uboot/duts/tc_ub_start_all_duts.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_start_all_duts.py

start all DUTS tests


only start the DUTS testcases, if tb.config.tc_ub_start_all_duts_start_

is set to True (default)


:usedvar:`used variables`


.. _tb.config.tc_ub_start_all_duts_start:

- tb.config.tc_ub_start_all_duts_start

| if 'yes' start all duts testcases
| default: 'yes'


------------------------------------------------


.. _tc_ub_aristainetos2_ubi_py:

uboot/tc_ub_aristainetos2_ubi.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_aristainetos2_ubi.py

ubi testcases for the aristainetos2 board


------------------------------------------------

.. _tc_ub_check_reg_file_py:

uboot/tc_ub_check_reg_file.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_check_reg_file.py

checks if the default values in reg file tb.config.tc_ub_create_reg_file_name_

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

compare the contents of tb.config.tc_ub_cmp_addr1_ with

tb.config.tc_ub_cmp_addr2_ of tb.config.tc_ub_cmp_len_

bytes length


:usedvar:`used variables`


.. _tb.config.tc_ub_cmp_addr1:

- tb.config.tc_ub_cmp_addr1

| address one
| default: ''

.. _tb.config.tc_ub_cmp_addr2:

- tb.config.tc_ub_cmp_addr2

| address one
| default: ''

.. _tb.config.tc_ub_cmp_len:

- tb.config.tc_ub_cmp_len

| length of bytes which get compared
| default: ''


------------------------------------------------

.. _tc_ub_create_am335x_reg_file_py:

uboot/tc_ub_create_am335x_reg_file.py
=====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_create_am335x_reg_file.py


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

them as a base for comparing further.



------------------------------------------------

.. _tc_ub_create_imx28_reg_file_py:

uboot/tc_ub_create_imx28_reg_file.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_create_imx28_reg_file.py


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

creates a reg file tb.config.tc_ub_create_reg_file_name_ on the tbot host

in tb.workdir

read from tb.config.tc_ub_create_reg_file_start_ to tb.config.tc_ub_create_reg_file_stop_

and writes the results in the regfile tb.config.tc_ub_create_reg_file_name_

format of the regfile:

regaddr mask type defval

This reg file can be used as a default file, how the

registers must be setup, check it with testcase

tc_ub_check_reg_file_py_

ToDo: use the file from the lab host, not the tbot host


:usedvar:`used variables`


.. _tb.config.tc_ub_create_reg_file_name:

- tb.config.tc_ub_create_reg_file_name

| filename of regfile which gets created
| complete path: tb.workdir + "/" + tb.config.tc_ub_create_reg_file_name_
| default: ''

.. _tb.config.tc_ub_create_reg_file_start:

- tb.config.tc_ub_create_reg_file_start

| start addresse from which a register dump gets created
| default: ''

.. _tb.config.tc_ub_create_reg_file_stop:

- tb.config.tc_ub_create_reg_file_stop

| stop addresse to which a register dump gets created
| default: ''

.. _tb.config.tc_ub_readreg_mask:

- tb.config.tc_ub_readreg_mask

| mask which gets written as default into register dump file
| default:

.. _tb.config.tc_ub_readreg_type:

- tb.config.tc_ub_readreg_type

| u-boot types of md command
| 'l', 'w' or 'b'
| default: ''

.. _tb.config.tc_ub_create_reg_file_mode:

- tb.config.tc_ub_create_reg_file_mode

| filemode, for file which gets created
| default:

.. _tb.config.tc_ub_create_reg_file_comment:

- tb.config.tc_ub_create_reg_file_comment

| if != 'none' add a comment line with content of this variable
| preceeded by a '#'
| default: 'none'


------------------------------------------------

.. _tc_ub_dfu_py:

uboot/tc_ub_dfu.py
==================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_dfu.py

test dfu

- use dfu-util in tb.config.tc_ub_dfu_dfu_util_path_
- upload file tb.config.tc_ub_dfu_dfu_util_alt_setting_ to
tb.config.tc_ub_dfu_dfu_util_downloadfile_

- download it back to the board
- upload it again
- and compare the two files

:usedvar:`used variables`


.. _tb.config.tc_ub_dfu_dfu_util_path:

- tb.config.tc_ub_dfu_dfu_util_path

| path to dfu-util program
| default: '/home/hs/zug/dfu-util'

.. _tb.config.tc_ub_dfu_dfu_util_alt_setting:

- tb.config.tc_ub_dfu_dfu_util_alt_setting

| alt setting for dfu command
| default: 'Linux'

.. _tb.config.tc_ub_dfu_dfu_util_downloadfile:

- tb.config.tc_ub_dfu_dfu_util_downloadfile

| file with full path which is used as temporary file
| in this testcase.
| default: ''


------------------------------------------------

.. _tc_ub_dfu_random_py:

uboot/tc_ub_dfu_random.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_dfu_random.py

test a U-Boot dfu alt setting tb.config.tc_ub_dfu_dfu_util_alt_setting_

Therefore write a random file with size tb.config.tc_ub_dfu_rand_size_

to it, reread it and compare it. TC fails if files differ

(If readen file is longer, this is no error!)


random file is created in tb.config.lab_tmp_dir_


If dfu-util is not installed on the lab PC, set

tb.config.tc_ub_dfu_dfu_util_ssh_ for connecting with ssh to a PC

which have it installed, and a USB cable connected to the board.

Set tb.config.tc_ub_dfu_dfu_util_path_ to the path of dfu-util, if

you have a self compiled version of it.

Set tb.config.tc_ub_dfu_rand_ubcmd_ for the executed command on

U-Boot shell for getting into DFU mode


:usedvar:`used variables`


.. _tb.config.tc_ub_dfu_dfu_util_ssh:

- tb.config.tc_ub_dfu_dfu_util_ssh

| if != 'none' connect with ssh to a PC, where
| dfu-util is installed.
| default: 'none'

.. _tb.config.tc_ub_dfu_rand_size:

- tb.config.tc_ub_dfu_rand_size

| size in bytes of created random file
| default: ''

.. _tb.config.tc_ub_dfu_rand_ubcmd:

- tb.config.tc_ub_dfu_rand_ubcmd

| U-Boot command for starting dfu
| default: ''


------------------------------------------------

.. _tc_ub_dfu_random_default_py:

uboot/tc_ub_dfu_random_default.py
=================================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_dfu_random_default.py

test a U-Boot dfu alt setting tb.config.tc_ub_dfu_dfu_util_alt_setting_

with reading / writing different sizes

and calling testcase tc_ub_dfu_random_py_


:usedvar:`used variables`


.. _tb.config.dfu_test_sizes_default:

- tb.config.dfu_test_sizes_default

| default: [
|        64 - 1,
|        64,
|        64 + 1,
|        128 - 1,
|        128,
|        128 + 1,
|        960 - 1,
|        960,
|        960 + 1,
|        4096 - 1,
|        4096,
|        4096 + 1,
|        1024 \* 1024 - 1,
|        1024 \* 1024,
|        8 \* 1024 \* 1024,
|    ]


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

simple get the content of U-Boot env variable filesize

and store it in tb.ub_filesize


------------------------------------------------

.. _tc_ub_get_version_py:

uboot/tc_ub_get_version.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_get_version.py

search in tb.config.tc_ub_get_version_file_ the string

tb.config.tc_ub_get_version_string_

and save the value in tb.config.tc_return_ and create

event ID UBOOT_VERSION.


:usedvar:`used variables`


.. _tb.config.tc_ub_get_version_file:

- tb.config.tc_ub_get_version_file

| file in which string gets searched
| default: ''

.. _tb.config.tc_ub_get_version_string:

- tb.config.tc_ub_get_version_string

| string which get searched in file
| default: ''


------------------------------------------------

.. _tc_ub_help_py:

uboot/tc_ub_help.py
===================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_help.py

test U-Boots help cmd

may we add a list as parameter, so we can adapt it board

specific.


------------------------------------------------

.. _tc_ub_load_board_env_py:

uboot/tc_ub_load_board_env.py
=============================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_load_board_env.py


task: load U-Boot Environment env.txt file with tftp for the

board tb.config.tftpboardname_ to the addr tb.config.ub_load_board_env_addr_

from subdir tb.config.ub_load_board_env_subdir_

and imports the the textfile with 'env import'


options:

if tb.config.tc_ub_boot_linux_load_env_ == 'no' than TC does nothing


if tb.config.tc_ub_boot_linux_load_env_ == 'set' or == 'setend'

than TC executes the cmds in list tb.config.ub_load_board_env_set_


if tb.config.tc_ub_boot_linux_load_env_ == 'setend' TC returns

after executing the commands with True


else TC executes the steps described in 'task'


tb.config.ub_load_board_env_testcase_ != 'none'

call a board specific testcase, whichs name is defined in

tb.config.ub_load_board_env_testcase_ for setting U-Boot

Env. If this testcase succeeds, end True.


:usedvar:`used variables`


.. _tb.config.ub_load_board_env_testcase:

- tb.config.ub_load_board_env_testcase

| if != 'none' call testcase with this name for
| for setting U-Boot Environment
| default: 'none'

.. _tb.config.ub_load_board_env_addr:

- tb.config.ub_load_board_env_addr

| ram address to which the env.txt file gets loaded
| default: '0x81000000'

.. _tb.config.ub_load_board_env_subdir:

- tb.config.ub_load_board_env_subdir

| subdir name in which env.txt file is found
| default: 'tbot'

.. _tb.config.tc_ub_boot_linux_load_env:

- tb.config.tc_ub_boot_linux_load_env

| value
| 'no'      no Environment gets loaded
| 'set'     load Environment from tb.config.ub_load_board_env_set_
| 'setend'  same as 'set' just end testcase after
|           Environment is set from tb.config.ub_load_board_env_set_
| 'load'    tftp a 'env.txt' file and import it with
|           'env import -t'
| default: 'load'

.. _tb.config.ub_load_board_env_set:

- tb.config.ub_load_board_env_set

| list of Environment settings
| default: '[]'


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

set U-Boot Environmentvariable tb.config.setenv_name_ with value

tb.config.setenv_value_


:usedvar:`used variables`:


.. _tb.config.setenv_name:

- tb.config.setenv_name

| name of the U-Boot Environment variable
| default: 'tralala'

.. _tb.config.setenv_value:

- tb.config.setenv_value

| value of the U-Boot Environment variable
| defalt: 'hulalahups'


------------------------------------------------

.. _tc_ub_setenv_fkt_py:

uboot/tc_ub_setenv_fkt.py
=========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_setenv_fkt.py

set U-Boot Environmentvariable tb.config.setenv_name_ with value

tb.config.setenv_value_


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

call test/py from u-boot source

- power off the board
- disconnect console
- goto u-boot code with testcase tc_workfd_goto_uboot_code_py_
- call test/py
- power off the board
- connect back to console
test/py hookscript directory:

tb.config.tc_ub_test_py_hook_script_path_


you can disable this testcase with tb.config.tc_ub_test_py_start_ = 'no'


may a configure file is needed, so create it with

tb.config.tc_ub_test_py_configfile._ This variable contains

the config file, which gets created.


at the end create event with ID UBOOT_TEST_PY


:usedvar:`used variables`


.. _tb.config.tc_ub_test_py_hook_script_path:

- tb.config.tc_ub_test_py_hook_script_path

| full path to hook scripts for test/py
| default: '$HOME/testframework/hook-scripts'

.. _tb.config.tc_ub_test_py_configfile:

- tb.config.tc_ub_test_py_configfile

| list of strings with configsettings for test/py
| default: '[]'

.. _tb.config.tc_ub_test_py_start:

- tb.config.tc_ub_test_py_start

| if 'no' do not start test/py
| default: 'yes'


------------------------------------------------

.. _tc_ub_testfkt_py:

uboot/tc_ub_testfkt.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_testfkt.py


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

name = tb.config.setenv_name_

val = tb.config.setenv_value_



------------------------------------------------

.. _tc_ub_tftp_file_py:

uboot/tc_ub_tftp_file.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_tftp_file.py

load file tb.config.tc_ub_tftp_file_name_ to tb.config.tc_ub_tftp_file_addr_

with tftp command in uboot



------------------------------------------------

.. _tc_ub_ubi_check_volume_py:

uboot/tc_ub_ubi_check_volume.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_check_volume.py

checks if ubi volume tb.config.tc_ub_ubi_load_name_ exists


:usedvar:`used variables`


.. _tb.config.tc_ub_ubi_load_name:

- tb.config.tc_ub_ubi_load_name

| volume name
| default: 'kernel'

------------------------------------------------

.. _tc_ub_ubi_create_volume_py:

uboot/tc_ub_ubi_create_volume.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_create_volume.py

create ubi volume tb.config.tc_ub_ubi_create_vol_name_ with size

tb.config.tc_ub_ubi_create_vol_sz_


:usedvar:`used variables`


.. _tb.config.tc_ub_ubi_create_vol_name:

- tb.config.tc_ub_ubi_create_vol_name

| volume name, which get created
| default: tb.config.tc_ub_ubi_load_name_

.. _tb.config.tc_ub_ubi_create_vol_sz:

- tb.config.tc_ub_ubi_create_vol_sz

| size of volume which get created
| default: '600000'


------------------------------------------------

.. _tc_ub_ubi_erase_py:

uboot/tc_ub_ubi_erase.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_erase.py

erase an ubi device

execute U-Boot Env tbot_ubi_erase


------------------------------------------------

.. _tc_ub_ubi_info_py:

uboot/tc_ub_ubi_info.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_info.py

simple print ubi info


------------------------------------------------

.. _tc_ub_ubi_prepare_py:

uboot/tc_ub_ubi_prepare.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_prepare.py

preparation for ubi tests


load U-Boot Env with tc_ub_load_board_env_py_


check if an ubi partition is attached, if so detach it


execute "ubi part" with tb.config.tc_ub_ubi_prep_partname_

if tb.config.tc_ub_ubi_prep_offset_ != 'none'

with offset tb.config.tc_ub_ubi_prep_offset_


and detach it


:usedvar:`used variables`:


.. _tb.config.tc_ub_ubi_prep_partname:

- tb.config.tc_ub_ubi_prep_partname

| mtd partition name, which is used for ubi
| default: 'ubi'

.. _tb.config.tc_ub_ubi_prep_offset:

- tb.config.tc_ub_ubi_prep_offset

| ubi pyhsical VID header offset for 'ubi part' command
| default: 'none'


------------------------------------------------

.. _tc_ub_ubi_read_py:

uboot/tc_ub_ubi_read.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_read.py

read ubi volume tb.config.tc_ub_ubi_prep_offset_ to tb.config.tc_ub_ubi_read_addr_

with len tb.config.tc_ub_ubi_read_len_


:usedvar:`used variables`


.. _tb.config.tc_ub_ubi_read_addr:

- tb.config.tc_ub_ubi_read_addr

| ram address for 'ubi read'
| default: ''

.. _tb.config.tc_ub_ubi_read_vol_name:

- tb.config.tc_ub_ubi_read_vol_name

| ubi volume name, which get read into ram
| default: ''

.. _tb.config.tc_ub_ubi_read_len:

- tb.config.tc_ub_ubi_read_len

| length in bytes for 'ubi read'
| default: ''


------------------------------------------------

.. _tc_ub_ubi_write_py:

uboot/tc_ub_ubi_write.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubi_write.py

write image @ tb.config.tc_ub_ubi_write_addr_ to ubi volume

tb.config.tc_ub_ubi_write_vol_name_ with len tb.config.tc_ub_ubi_write_len_


:usedvar:`used variables`


.. _tb.config.tc_ub_ubi_write_addr:

- tb.config.tc_ub_ubi_write_addr

| RAM address of image, which gets written into ubi volume
| default: '14000000'

.. _tb.config.tc_ub_ubi_write_vol_name:

- tb.config.tc_ub_ubi_write_vol_name

| ubi volume name in which the image gets written
| default: tb.config.tc_ub_ubi_create_vol_name_

.. _tb.config.tc_ub_ubi_write_len:

- tb.config.tc_ub_ubi_write_len

| length in bytes which gets written into ubi volume
| default: '0xc00000'


------------------------------------------------

.. _tc_ub_ubifs_ls_py:

uboot/tc_ub_ubifs_ls.py
=======================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubifs_ls.py

ls ubifs tb.config.tc_ub_ubifs_ls_dir_


:usedvar:`used variables`


.. _tb.config.tc_ub_ubifs_ls_dir:

- tb.config.tc_ub_ubifs_ls_dir

| directory path which gets listed with 'ubifsls'
| default: '/'


------------------------------------------------

.. _tc_ub_ubifs_mount_py:

uboot/tc_ub_ubifs_mount.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_ubifs_mount.py

mount ubifs tb.config.tc_ub_ubifs_volume_name_


:usedvar:`used variables`


.. _tb.config.tc_ub_ubifs_volume_name:

- tb.config.tc_ub_ubifs_volume_name

| ubifs volume name which gets mounted with 'ubifsmount'
| default: 'ubi:rootfs'


------------------------------------------------

.. _tc_ub_upd_spl_py:

uboot/tc_ub_upd_spl.py
======================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_upd_spl.py

update new spl to board if tb.config.tc_ub_upd_spl_withspl_ == 'yes'


steps:

- load tbot u-boot env vars if tb.config.tc_ub_upd_spl_latest_ != 'no'
|  with testcase tc_ub_load_board_env_py_
- execute "run tbot_upd_spl"
- execute "run tbot_cmp_spl"
- reset board
- get u-boot

:usedvar:`used variables`


.. _tb.config.tc_ub_upd_spl_ubvars:

- tb.config.tc_ub_upd_spl_ubvars

| additionaly printed U-Boot Environmnet variables, if != 'none'
| default: 'none'

.. _tb.config.tc_ub_upd_spl_withspl:

- tb.config.tc_ub_upd_spl_withspl

| if != 'yes' do nothing, return True
| default: 'yes'

.. _tb.config.tc_ub_upd_spl_latest:

- tb.config.tc_ub_upd_spl_latest

| if == 'no' load U-Boot Environment with testcase
| tc_ub_load_board_env_py_
| default: 'no'


------------------------------------------------

.. _tc_ub_upd_uboot_py:

uboot/tc_ub_upd_uboot.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_ub_upd_uboot.py

update new uboot to board

steps:

- load tbot u-boot env vars if tb.config.tc_ub_upd_uboot_latest_ == 'no'
- execute "run tbot_upd_uboot"
- execute "run tbot_cmp_uboot"
- reset board
- get u-boot

:usedvar:`used variables`


.. _tb.config.tc_ub_upd_uboot_ubvars:

- tb.config.tc_ub_upd_uboot_ubvars

| additionaly printed U-Boot Environmnet variables, if != 'none'
| default: 'none'

.. _tb.config.tc_ub_upd_uboot_latest:

- tb.config.tc_ub_upd_uboot_latest

| if == 'no' load U-Boot Environment with testcase
| tc_ub_load_board_env_py_
| default: 'no'


------------------------------------------------

.. _tc_uboot_check_kconfig_py:

uboot/tc_uboot_check_kconfig.py
===============================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_check_kconfig.py


check for all boards, if a patch changes the u-boot binary

If U-boot binary changed by the patch this testcase fails.

use this testcase, if you for example move a config option

into Kconfig. As we need reproducable builds, we need to

patch U-Boot with tb.config.tc_uboot_check_kconfig_preparepatch_

find this patch here: src/files/ub-patches/0001-U-Boot-version-fix.patch

copy it to the lab pc and adapt tb.config.tc_uboot_check_kconfig_preparepatch_


Steps from this testcase:

- rm U-Boot code with tc_workfd_rm_uboot_code_py_
- get U-Boot code with tc_lab_get_uboot_source_py_
- set SOURCE_DATE_EPOCH=0 to get reproducible builds
- apply patch from tb.config.tc_uboot_check_kconfig_preparepatch_
get rid of local version ToDo: find a way to disable CONFIG_LOCALVERSION_AUTO

so this patch is not longer needed.

- if tb.config.tc_uboot_check_kconfig_read_sumfile_ is != 'none'
read a list of boards and md5sums from the file in

tb.config.tc_uboot_check_kconfig_read_sumfile_

else

- create a list of boards (all defconfigs)
- do for all boards:
- get architecture and set toolchain
- compile U-Boot and calculate md5sum
with tc_workfd_compile_uboot_py_ and tc_workfd_md5sum_py_

- if tb.config.tc_uboot_check_kconfig_create_sumfile_ != 'none'
save the board md5sum lists in the file

tb.config.tc_uboot_check_kconfig_create_sumfile_

you can use this now as a reference, so no need

to calculate always for all boards the md5sums

-> saves a lot of time!

- apply patch(es) with tc_workfd_apply_patches_py_
- do for all boards:
- compile U-Boot again (patched version)
- calculate md5sum again
- calculate md5sums
- check if they are the same

:usedvar:`used variables`:


.. _tb.config.tc_uboot_check_kconfig_preparepatch:

- tb.config.tc_uboot_check_kconfig_preparepatch

| full path to directory, which contains patch
| to patch U-Boot to produce reproducible builds
| default: ''

.. _tb.config.tc_uboot_check_kconfig_read_sumfile:

- tb.config.tc_uboot_check_kconfig_read_sumfile

| fix value 'none'

.. _tb.config.tc_uboot_check_kconfig_create_sumfile:

- tb.config.tc_uboot_check_kconfig_create_sumfile

| fix value 'md5sum.txt'


------------------------------------------------

.. _tc_uboot_ext2load_py:

uboot/tc_uboot_ext2load.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_ext2load.py


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


:usedvar:`used variables`


.. _tb.config.tc_uboot_ext2load_check:

- tb.config.tc_uboot_ext2load_check

| if == 'no' do not check crc
| default: 'no'

.. _tb.config.tc_uboot_ext2load_file:

- tb.config.tc_uboot_ext2load_file

| name of file, which gets loaded
| default: '/test.bin'

.. _tb.config.tc_uboot_ext2load_addr:

- tb.config.tc_uboot_ext2load_addr

| RAM address to which the file get loaded
| default: '10000000'

.. _tb.config.tc_uboot_ext2load_dev:

- tb.config.tc_uboot_ext2load_dev

| device from which the file get loaded
| default: '0:1'

.. _tb.config.tc_uboot_ext2load_interface:

- tb.config.tc_uboot_ext2load_interface

| device from which the file get loaded
| default: 'usb'


------------------------------------------------

.. _tc_uboot_ext2ls_py:

uboot/tc_uboot_ext2ls.py
========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_ext2ls.py


simply call ext2ls U-Boot command and check if

all strings in tb.config.tc_uboot_ext2ls_expect_

come back from the command.


:usedvar:`used variables`


.. _tb.config.tc_uboot_ext2ls_expect:

- tb.config.tc_uboot_ext2ls_expect

| list of strings, which should come back from
| command 'ext2ls'
| default: "['lost+found']"

.. _tb.config.tc_uboot_ext2ls_interface:

- tb.config.tc_uboot_ext2ls_interface

| used interface for ext2ls command
| default: 'usb'

.. _tb.config.tc_uboot_ext2ls_dev:

- tb.config.tc_uboot_ext2ls_dev

| device used for ext2ls command
| default: '0:1'

.. _tb.config.tc_uboot_ext2ls_dir:

- tb.config.tc_uboot_ext2ls_dir

| directory, which gets dumped
| default: '/'


------------------------------------------------

.. _tc_uboot_get_arch_py:

uboot/tc_uboot_get_arch.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_get_arch.py

get architecture from u-boot config


------------------------------------------------

.. _tc_uboot_load_bin_with_kermit_py:

uboot/tc_uboot_load_bin_with_kermit.py
======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_load_bin_with_kermit.py

load binary into ram with loadb


if tb.config.tc_uboot_load_bin_with_kermit_possible_ != 'yes'

do nothing return True

default: 'yes'


precondition:

kermit must be used


steps:

- loadb tb.config.tc_uboot_load_bin_ram_addr_
- leave kermit
- send tb.config.tc_uboot_load_bin_file_
protocol: kermit_protocol='kermit'

wait for "C-Kermit>"

connect

you must get back something like this:

## Total Size      = 0x00050bc0 = 330688 Bytes

## Start Addr      = 0x81000000


:usedvar:`used variables`


.. _tb.config.tc_uboot_load_bin_with_kermit_possible:

- tb.config.tc_uboot_load_bin_with_kermit_possible

| if != 'yes' return True, do nothing
| default: 'yes'

.. _tb.config.tc_uboot_load_bin_ram_addr:

- tb.config.tc_uboot_load_bin_ram_addr

| RAM address to which file get loaded
| default: '81000000'

.. _tb.config.tc_uboot_load_bin_file:

- tb.config.tc_uboot_load_bin_file

| filename which get loaded with kermit
| default: '/home/alka/tbot/nero-images/u-boot.img'

.. _tb.config.tc_uboot_load_bin_with_kermit_kermit_settings:

- tb.config.tc_uboot_load_bin_with_kermit_kermit_settings

| kermit settings, known to work good
| default: 
| [
|    "set carrier-watch off",
|     "set handshake none",
|     "set flow-control none",
|     "robust",
|     "set file type bin",
|     "set file name lit",
|     "set rec pack 100",
|     "set send pack 100",
|     "set window 5",
| ]'


------------------------------------------------

.. _tc_uboot_usb_info_py:

uboot/tc_uboot_usb_info.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_usb_info.py


call "usb info" command


:usedvar:`used variables`:


.. _tb.config.tc_uboot_usb_info_expect:

- tb.config.tc_uboot_usb_info_expect

| strings which must come from "usb info" command
| default: "['Hub,  USB Revision 2.0', 'Mass Storage,  USB Revision 2.0']"


------------------------------------------------

.. _tc_uboot_usb_start_py:

uboot/tc_uboot_usb_start.py
===========================

https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/tc_uboot_usb_start.py


call "usb start" command


used variable


- tb.config.tc_uboot_usb_start_expect_
| strings which must come back from "usb start" command
| default: 'Storage Device(s) found'


------------------------------------------------


.. _Directory_yocto:

***************
Directory yocto
***************

.. _tc_workfd_bitbake_py:

yocto/tc_workfd_bitbake.py
==========================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_bitbake.py


simple call bitbake with tb.config.tc_workfd_bitbake_args_


if tb.config.tc_workfd_bitbake_machine_ is != 'none', also cat

the content of the newest file in tmp/log/cooker/" + tb.config.tc_workfd_bitbake_machine_ + "/\*


:usedvar:`used variables`:


.. _tb.config.tc_workfd_bitbake_machine:

- tb.config.tc_workfd_bitbake_machine

| if != 'none' add "MACHINE=tb.config.tc_workfd_bitbake_machine_ " bofore
| bitbake command.
| default: 'none'

.. _tb.config.tc_workfd_bitbake_args:

- tb.config.tc_workfd_bitbake_args

| arguments for bitbake command
| default: ''


------------------------------------------------

.. _tc_workfd_check_repo_cmd_py:

yocto/tc_workfd_check_repo_cmd.py
=================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_check_repo_cmd.py


check if repo cmd exists, if not try to set

PATH variable stored in tb.config.tc_workfd_repo_path_


used variable:


- tb.config.tc_workfd_repo_path_
| PATH to repo command. If 'repo' command is not found
| add this path to PATH Environment variable.
| default: 'none'


------------------------------------------------

.. _tc_workfd_get_with_repo_py:

yocto/tc_workfd_get_with_repo.py
================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_get_with_repo.py


get yocto code with repo tool and configure sources


- check if repo command exists
if not try to set path to it, if tb.config.tc_workfd_repo_path_

is set, else failure


- goto repo code with testcase tc_workfd_goto_repo_code_py_
if dir $TBOT_BASEDIR_REPO does not exist create it

- call "repo init" with variables
tb.config.tc_workfd_get_with_repo_u_

tb.config.tc_workfd_get_with_repo_m_

tb.config.tc_workfd_get_with_repo_b_


- get newest sources with "repo sync"

- setup environment with samples from meta-
tb.config.tc_workfd_get_with_repo_metaname_


- check if build directory "build_" + tb.config.tc_workfd_bitbake_machine_
exists, if not create it and set DL_DIR and SSTATE_DIR in local.conf

with the values from tb.config.tc_workfd_get_yocto_source_conf_dl_dir_

and tb.config.tc_workfd_get_yocto_source_conf_sstate_dir_


and setup site.conf with specific settings


:usedvar:`used variables`:


.. _tb.config.tc_workfd_get_with_repo_metaname:

- tb.config.tc_workfd_get_with_repo_metaname

| name for meta layer, from which samples get used for
| setting up bitbake with 'TEMPLATECONF=meta-' + tb.config.tc_workfd_get_with_repo_metaname_
| default: 'beld'

.. _tb.config.builddir:

- tb.config.builddir

| bitbake builddir. If it exists, only dump site.conf
| If dir not exist, setup up this directory
| default: "$TBOT_BASEDIR_YOCTO/build_" + tb.config.tc_workfd_bitbake_machine_ + "/"

.. _tb.config.tc_workfd_get_with_repo_sync:

- tb.config.tc_workfd_get_with_repo_sync

| call 'repo sync' if yes
| default: 'yes'

.. _tb.config.tc_workfd_get_with_repo_u:

- tb.config.tc_workfd_get_with_repo_u

| '-u' paramter for repo command
| default: ''

.. _tb.config.tc_workfd_get_with_repo_m:

- tb.config.tc_workfd_get_with_repo_m

| '-m' paramter for repo command
| default: ''

.. _tb.config.tc_workfd_get_with_repo_b:

- tb.config.tc_workfd_get_with_repo_b

| '-b' paramter for repo command
| default: ''

.. _tb.config.tc_workfd_get_with_repo_target:

- tb.config.tc_workfd_get_with_repo_target

| target directory, where source is found after "repo sync"
| '$TBOT_BASEDIR_REPO/' + tb.config.tc_workfd_get_with_repo_target_
| default: ''


------------------------------------------------

.. _tc_workfd_get_yocto_source_py:

yocto/tc_workfd_get_yocto_source.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_get_yocto_source.py

get yocto source tb.config.tc_workfd_get_yocto_patches_git_repo_ with "git clone"


check out branch:

tb.config.tc_workfd_get_yocto_patches_git_branch_


check out commit ID:

tb.config.tc_workfd_get_yocto_git_commit_id_


if tb.config.tc_workfd_get_yocto_patches_git_repo_ != 'none'

apply patches with "git am" from directory:

tb.config.tc_workfd_get_yocto_clone_apply_patches_git_am_dir_


additionally define a reference for cloning:

tb.config.tc_workfd_get_yocto_source_git_reference_

if a user/password for cloning is needed, define the user:

tb.config.tc_workfd_get_yocto_source_git_repo_user_

and set the password in password_py_


get other layers defined in the list:

tb.config.tc_workfd_get_yocto_source_layers_


if tb.config.tc_workfd_get_yocto_source_autoconf_ == 'none'

overwrite yocto configuration found in

tb.config.tc_workfd_get_yocto_source_conf_dir_

else

try to autogenerate bblayers.conf and site.conf


clones into directory tb.config.yocto_name_

created with tc_workfd_goto_yocto_code_py_


:usedvar:`used variables`


.. _tb.config.tc_workfd_get_yocto_source_autoconf:

- tb.config.tc_workfd_get_yocto_source_autoconf

| if  'none' copy config files from tb.config.tc_workfd_get_yocto_source_conf_dir_
| default: 'none'

.. _tb.config.tc_workfd_get_yocto_source_conf_dir:

- tb.config.tc_workfd_get_yocto_source_conf_dir

| path, in which yocto configurations file are found
| default: 'not defined'

.. _tb.config.tc_workfd_get_yocto_patches_git_repo:

- tb.config.tc_workfd_get_yocto_patches_git_repo

| path to git repo with yocto patches
| default: ''

.. _tb.config.tc_workfd_get_yocto_patches_git_branch:

- tb.config.tc_workfd_get_yocto_patches_git_branch

| branch which get checked out in tb.config.tc_workfd_get_yocto_patches_git_repo_
| default: ''

.. _tb.config.tc_workfd_get_yocto_patches_git_repo_name:

- tb.config.tc_workfd_get_yocto_patches_git_repo_name

| name the repo with the patches gets
| default: ''

.. _tb.config.tc_workfd_get_yocto_source_git_repo:

- tb.config.tc_workfd_get_yocto_source_git_repo

| git url, to yocto code
| default: 'git://git.yoctoproject.org/poky.git'

.. _tb.config.tc_workfd_get_yocto_source_git_branch:

- tb.config.tc_workfd_get_yocto_source_git_branch

| branch which gets checked out
| default: 'pyro'

.. _tb.config.tc_workfd_get_yocto_git_commit_id:

- tb.config.tc_workfd_get_yocto_git_commit_id

| if != 'none' commit ID to which tree gets resettet
| default: 'none'

.. _tb.config.tc_workfd_get_yocto_source_layers:

- tb.config.tc_workfd_get_yocto_source_layers

| list of meta layers, which get checked out
| one element contains the following list element:
| ['git repo',
|  'git branch',
|  'git commit id',
|  'apply_patches_dir'
|  'apply_patches_git_am_dir',
|  'source_git_reference',
|  'source_git_repo_user',
|  'source_git_repo_name'
| ]
|
| default: "
| [
| ['git://git.openembedded.org/meta-openembedded', 'morty', '659d9d3f52bad33d7aa1c63e25681d193416d76e', 'none', 'none', 'none', '', 'meta-openembedded'],
| ['https://github.com/sbabic/meta-swupdate.git', 'master', 'b3abfa78d04b88b88bcef6f5be9f2adff1293544', 'none', 'none', 'none', '', 'meta-swupdate'],
| ]
| "

.. _tb.config.tc_workfd_get_yocto_source_conf_dl_dir:

- tb.config.tc_workfd_get_yocto_source_conf_dl_dir

| path to yocto download directory.
| If != 'none' testcase checks if exists, if not
| create it. Also patch local.conf
| default: 'none'

.. _tb.config.tc_workfd_get_yocto_source_conf_sstate_dir:

- tb.config.tc_workfd_get_yocto_source_conf_sstate_dir

| path to sstate directory.
| If != 'none' testcase checks if exists, if not
| create it. Also patch local.conf
| default: 'none'


------------------------------------------------

.. _tc_workfd_goto_repo_code_py:

yocto/tc_workfd_goto_repo_code.py
=================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_goto_repo_code.py


switch into yocto source directory $TBOT_BASEDIR_REPO

created with repo tool.


Which is tb.config.tc_lab_source_dir_ + "/repo-" + tb.config.boardlabname_


set tb.config.repo_name_ to "repo-" + tb.config.boardlabname_

and tb.config.repo_fulldir_name_ to tb.config.tc_lab_source_dir_ + "/" + tb.config.repo_name_

and set $TBOT_BASEDIR_REPO to tb.config.repo_fulldir_name_


:usedvar:`used variables`


.. _tb.config.tc_workfd_goto_repo_code_dirext:

- tb.config.tc_workfd_goto_repo_code_dirext

| if != 'none' add this string to tb.config.repo_name_
| default: 'none'

.. _tb.config.tc_workfd_goto_repo_code_checked:

- tb.config.tc_workfd_goto_repo_code_checked

| variable at runtime set, do not set it from a config file
| marker, if setup for this testcase is already done.

.. _tb.config.repo_name:

- tb.config.repo_name

| set to to "repo-" + tb.config.boardlabname_

.. _tb.config.repo_fulldir_name:

- tb.config.repo_fulldir_name

| set to tb.config.tc_lab_source_dir_ + "/" + tb.config.repo_name_


------------------------------------------------

.. _tc_workfd_goto_yocto_code_py:

yocto/tc_workfd_goto_yocto_code.py
==================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_goto_yocto_code.py

switch into yocto source tb.config.tc_lab_source_dir_ + "/yocto-" + tb.config.boardlabname_

set tb.config.yocto_name_ to "yocto-" + tb.config.boardlabname_

and tb.config.yocto_fulldir_name_ to tb.config.tc_lab_source_dir_ + "/" + tb.config.yocto_name_

and set $TBOT_BASEDIR_YOCTO to tb.config.yocto_fulldir_name_


:usedvar:`used variables`


.. _tb.config.tc_workfd_goto_yocto_code_dirext:

- tb.config.tc_workfd_goto_yocto_code_dirext

| if != 'none' add this string to tb.config.yocto_name_
| default: 'none'

- tb.workfd.tc_workfd_goto_yocto_code_path
| if != 'none' tb.config.yocto_name_ = os.path.basename(tb.workfd.tc_workfd_goto_yocto_code_path)
| default: 'none'

- tb.workfd.tc_workfd_goto_yocto_code_checked
| marker, if setup for this testcase is already done.
| variable at runtime set, do not set it from a config file.

.. _tb.config.yocto_fulldir_name:

- tb.config.yocto_fulldir_name

| set at runtime, full path to yocto source code

.. _tb.config.yocto_name:

- tb.config.yocto_name

| set at runtime, name of yocto source code directory
| "yocto-" + tb.config.boardlabname_


------------------------------------------------

.. _tc_workfd_yocto_basic_check_py:

yocto/tc_workfd_yocto_basic_check.py
====================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_yocto_basic_check.py


do basic yocto checks


- check rootfs version
|   only if tb.config.tc_workfd_yocto_basic_check_rootfsversion_ == 'yes'
|   which is the default.
- check dmesg output
|   check if strings defined in tb.config.tc_demo_yocto_test_checks_
|   are found in dmesg output
- check if devmem2 tool is in rootfs, if so, do register checks

:usedvar:`used variables`


.. _tb.config.tc_workfd_yocto_basic_check_rootfsversion:

- tb.config.tc_workfd_yocto_basic_check_rootfsversion

| if 'yes' check rootfs version with testcase
| tc_workfd_yocto_check_rootfs_version_py_
| default: 'yes'

.. _tb.config.tc_workfd_yocto_basic_check_board_specific:

- tb.config.tc_workfd_yocto_basic_check_board_specific

| if != 'none, call testcase with this name
| default: 'none'

.. _tb.config.tc_demo_yocto_test_checks:

- tb.config.tc_demo_yocto_test_checks

| list of strings, which must be in 'dmesg' output
| default: '[]'

.. _tb.config.tc_workfd_yocto_basic_check_regfiles:

- tb.config.tc_workfd_yocto_basic_check_regfiles

| list of filenames, which contain register dumps.
| This registerdumps are checked with testcase
| tc_lx_check_reg_file_py_ if devmem2 command exists.
| default: '[]'


------------------------------------------------

.. _tc_workfd_yocto_check_rootfs_version_py:

yocto/tc_workfd_yocto_check_rootfs_version.py
=============================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_yocto_check_rootfs_version.py


check if the current /etc/version on the target rootfs is the

same as in tb.config.tc_yocto_get_rootfs_from_tarball_



------------------------------------------------

.. _tc_workfd_yocto_generate_bblayers_py:

yocto/tc_workfd_yocto_generate_bblayers.py
==========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_yocto_generate_bblayers.py

create bblayer.conf file


:usedvar:`used variables`


.. _tb.config.tc_workfd_yocto_generate_bblayers_openembedded_layers:

- tb.config.tc_workfd_yocto_generate_bblayers_openembedded_layers

| used meta layers from meta-openembedded
| default: "['meta-networking']"

.. _tb.config.tc_workfd_yocto_generate_bblayers_xenomai_layers:

- tb.config.tc_workfd_yocto_generate_bblayers_xenomai_layers

| used meta layers from meta-xenomai
| default: '[]'


------------------------------------------------

.. _tc_workfd_yocto_patch_site_py:

yocto/tc_workfd_yocto_patch_site.py
===================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_workfd_yocto_patch_site.py


patch / create site.conf


:usedvar:`used variables`:


.. _tb.config.tc_workfd_yocto_patch_site_path_default_file:

- tb.config.tc_workfd_yocto_patch_site_path_default_file

| if != 'none' use this file as default
| default: 'none'

.. _tb.config.tc_workfd_yocto_patch_site_swu_priv_key:

- tb.config.tc_workfd_yocto_patch_site_swu_priv_key

| if != 'none' add SWUPDATE_PRIVATE_KEY if tb.config.tc_workfd_yocto_patch_site_swu_priv_key_
| default: 'none'

.. _tb.config.tc_workfd_yocto_patch_site_swu_priv_passout:

- tb.config.tc_workfd_yocto_patch_site_swu_priv_passout

| if != 'none'
| add SWUPDATE_PASSWORD_FILE if tb.config.tc_workfd_yocto_patch_site_swu_priv_passout_
-
| if != 'none'
| add SWUPDATE_PUBLIC_KEY if tb.config.tc_workfd_yocto_patch_site_swu_pub_key_
| default: 'none'

.. _tb.config.tc_workfd_yocto_patch_site_ub_key:

- tb.config.tc_workfd_yocto_patch_site_ub_key

| if != 'none'
| add UB_KEY_PATH if tb.config.tc_workfd_yocto_patch_site_ub_key_
| default: 'none'

.. _tb.config.tc_workfd_yocto_patch_site_dl_dir:

- tb.config.tc_workfd_yocto_patch_site_dl_dir

| if != 'none'
| add DL_DIR if tb.config.tc_workfd_yocto_patch_site_dl_dir_
| default: 'none'

.. _tb.config.tc_workfd_yocto_patch_site_sstate_dir:

- tb.config.tc_workfd_yocto_patch_site_sstate_dir

| if != 'none'
| add SSTATE_DIR if tb.config.tc_workfd_yocto_patch_site_sstate_dir_
| default: 'none'

.. _tb.config.tc_workfd_yocto_patch_site_src_linux_stable:

- tb.config.tc_workfd_yocto_patch_site_src_linux_stable

| if != 'none'
| add SRC_LINUX_STABLE if tb.config.tc_workfd_yocto_patch_site_src_linux_stable_
| default: 'none'

.. _tb.config.tc_workfd_yocto_patch_site_premirrors:

- tb.config.tc_workfd_yocto_patch_site_premirrors

| if != 'none'
| add PREMIRRORS_prepend if tb.config.tc_workfd_yocto_patch_site_premirrors_
| default: 'none'


------------------------------------------------

.. _tc_yocto_get_rootfs_from_tarball_py:

yocto/tc_yocto_get_rootfs_from_tarball.py
=========================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_yocto_get_rootfs_from_tarball.py


get rootfs version from rootfs tar ball filepath and name stored in

tb.config.tc_yocto_get_rootfs_from_tarball_

and store versionstring in variable:

tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version_


creates event ID DUTS_YOCTO_VERSION


:usedvar:`used variables`:


.. _tb.config.tc_yocto_get_rootfs_from_tarball:

- tb.config.tc_yocto_get_rootfs_from_tarball

| filename of tar.gz or tar.bz2 rootfsfile
| default: ''

.. _tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version:

- tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version

| created while running tc_yocto_get_rootfs_from_tarball_py_
| contains the content of '/etc/version' of a yocto builded rootfs


------------------------------------------------

.. _tc_yocto_install_rootfs_as_nfs_py:

yocto/tc_yocto_install_rootfs_as_nfs.py
=======================================

https://github.com/hsdenx/tbot/blob/master/src/tc/yocto/tc_yocto_install_rootfs_as_nfs.py


install tb.config.rootfs_tar_file_ from path tb.config.tc_yocto_install_rootfs_as_nfs_path_

into tb.config.nfs_subdir_


:usedvar:`used variables`


.. _tb.config.rootfs_tar_file:

- tb.config.rootfs_tar_file

| tar file with rootfs content
| default: ''

.. _tb.config.tc_yocto_install_rootfs_as_nfs_path:

- tb.config.tc_yocto_install_rootfs_as_nfs_path

| path to testcase finds file tb.config.rootfs_tar_file_
| default: ''

.. _tb.config.nfs_subdir:

- tb.config.nfs_subdir

| nfs path
| default: ''


------------------------------------------------


.. _tc_board_git_bisect_py:

**********************
tc_board_git_bisect.py
**********************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_board_git_bisect.py

get a source code with tc tb.config.board_git_bisect_get_source_tc_

and start a "git bisect" session


current commit is bad


good commit id is defined through tb.config.board_git_bisect_good_commit_


tc for testing good or bad is tb.config.board_git_bisect_call_tc_


if you have some local patches, which needs to be applied

each git bisect step, set tb.config.board_git_bisect_patches_


if you need to restore your board after a failure, set the

variable tb.config.board_git_bisect_restore_ to the tc name

which restores the board after each step


:usedvar:`used variables`


.. _tb.config.board_git_bisect_get_source_tc:

- tb.config.board_git_bisect_get_source_tc

|  testcase which gets called for changing into the git source
|  code.
|  default: 'tc_lab_get_uboot_source_py_'

.. _tb.config.board_git_bisect_call_tc:

- tb.config.board_git_bisect_call_tc

|  testcase, which gets called for finding out, if current
|  checked out state of the source is good or bad
|  default: 'tc_board_tqm5200s_ub_comp_install_py_'

.. _tb.config.board_git_bisect_good_commit:

- tb.config.board_git_bisect_good_commit

|  last know good commit id
|  default: 'f9860cf'

.. _tb.config.board_git_bisect_patches:

- tb.config.board_git_bisect_patches

|  patches, which get applied in each step fo git bisect
|  default: 'none'

.. _tb.config.board_git_bisect_restore:

- tb.config.board_git_bisect_restore

|  name of testcase, which gets called after each step, for
|  restoring your board. Used for example, if you bisect
|  u-boot and you break with bad source code your board.
|  default: 'none'


------------------------------------------------

.. _tc_dummy_py:

***********
tc_dummy.py
***********

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_dummy.py

This is only a dummy testcase, with which you can start

to write a testcase.


which explains what your testcase do and how.


If it defines a new variable with tb.define_variable

add the following section, where you explain the new

variable.


:usedvar:`used variables`


.. _tb.config.varname:

- tb.config.varname

|  some text, which describes the function of the variable
|  default: 'default value'


------------------------------------------------

.. _tc_lab_apply_patches_py:

***********************
tc_lab_apply_patches.py
***********************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_apply_patches.py


set workfd to c_ctrl

call  tc_workfd_apply_patches_py_

restore old workfd


:usedvar:`used variables`:


tb.config.tc_lab_apply_patches_dir_



------------------------------------------------

.. _tc_lab_compile_uboot_py:

***********************
tc_lab_compile_uboot.py
***********************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_compile_uboot.py


set workfd to c_ctrl

call tc_workfd_compile_uboot_py_

restore old workfd



------------------------------------------------

.. _tc_lab_cp_file_py:

*****************
tc_lab_cp_file.py
*****************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_cp_file.py

simple copy  file from arg.get('s')

to arg.get('t') on the channel arg.get('ch')


------------------------------------------------

.. _tc_lab_get_uboot_source_py:

**************************
tc_lab_get_uboot_source.py
**************************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_get_uboot_source.py


get U-Boot source

and go into the source tree


:usedvar:`used variables`


.. _tb.config.tc_lab_get_uboot_source_git_repo:

- tb.config.tc_lab_get_uboot_source_git_repo

|  repo to clone
|  default: '/home/git/u-boot.git'

.. _tb.config.tc_lab_get_uboot_source_git_branch:

- tb.config.tc_lab_get_uboot_source_git_branch

|  branch which get checked out
|  default: master

.. _tb.config.tc_get_ub_source_reference:

- tb.config.tc_get_ub_source_reference

|  reference which get used when cloning
|  if 'none' no "--reference=..." option is
|  used for "git clone"
|  default: 'none'


------------------------------------------------

.. _tc_lab_poweroff_py:

******************
tc_lab_poweroff.py
******************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_poweroff.py

simple power off the board with name

tb.config.boardname_


------------------------------------------------

.. _tc_lab_poweron_py:

*****************
tc_lab_poweron.py
*****************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_poweron.py

simple power on the board

with name tb.config.boardname_


------------------------------------------------

.. _tc_lab_rm_dir_py:

****************
tc_lab_rm_dir.py
****************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_rm_dir.py

simple rm a directory tb.config.tc_lab_rm_dir_

in the lab.


------------------------------------------------

.. _tc_lab_set_toolchain_py:

***********************
tc_lab_set_toolchain.py
***********************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_lab_set_toolchain.py

set eldk toolchain with eldk-switch

works only on tb.c_ctrl (change this)


:usedvar:`used variables`


.. _tb.config.tc_lab_toolchain_rev:

- tb.config.tc_lab_toolchain_rev

| toolchain revision
| default: '5.4'

.. _tb.config.tc_lab_toolchain_name:

- tb.config.tc_lab_toolchain_name

| toolchain name
| default: 'armv5te'


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

- load u-boot environment with testcase "tc_ub_load_board_env_py_"
- execute u-boot cmd tb.config.ub_boot_linux_cmd_

------------------------------------------------

.. _tc_workfd_apply_patches_py:

**************************
tc_workfd_apply_patches.py
**************************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_workfd_apply_patches.py

apply patches in tb.config.tc_lab_apply_patches_dir_


- tb.config.tc_lab_apply_patches_dir_
path to directory which contains the patches

default: 'none'



------------------------------------------------

.. _tc_workfd_compile_uboot_py:

**************************
tc_workfd_compile_uboot.py
**************************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_workfd_compile_uboot.py

compile u-boot


:usedvar:`used variables`

.. _tb.config.tc_lab_compile_uboot_export_path:

- tb.config.tc_lab_compile_uboot_export_path

| if != 'none' add in PATH the string from this variable
| default: 'none'

.. _tb.config.tc_lab_compile_uboot_boardname:

- tb.config.tc_lab_compile_uboot_boardname

| Name used for defconfig
| default: tb.config.boardname_

.. _tb.config.tc_lab_compile_uboot_makeoptions:

- tb.config.tc_lab_compile_uboot_makeoptions

| option string used for calling make
| default: '-j4'


------------------------------------------------

.. _tc_workfd_git_clone_source_py:

*****************************
tc_workfd_git_clone_source.py
*****************************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_workfd_git_clone_source.py

get source from git repo tb.config.tc_lab_git_clone_source_git_repo_ with "git clone"

and go into the source tree. 

check out branch tb.config.tc_lab_git_clone_source_git_branch_

and apply patches if needed with:

tc_lab_apply_patches_py_ and patches from directory

tb.config.tc_lab_git_clone_apply_patches_dir_

use as reference tb.config.tc_lab_git_clone_source_git_reference_

if != 'none'


You can give the repo a name with setting

tb.config.tc_lab_git_clone_source_git_repo_name_

!= 'none'


If you need a user/password for cloning, you can define

the username through:

tb.config.tc_lab_git_clone_source_git_repo_user_

define the password for this in password_py_

boardname in password_py_ is used as tb.config.tc_lab_git_clone_source_git_repo_


:usedvar:`used variables`


.. _tb.config.tc_lab_git_clone_source_git_repo:

- tb.config.tc_lab_git_clone_source_git_repo

| git url
| default: 'git://git.yoctoproject.org/poky.git'

.. _tb.config.tc_lab_git_clone_source_git_branch:

- tb.config.tc_lab_git_clone_source_git_branch

| branch which get checked out after cloning
| default: 'morty'

.. _tb.config.tc_lab_git_clone_source_git_commit_id:

- tb.config.tc_lab_git_clone_source_git_commit_id

| commit id which gets checked out if value != 'none'
| default: 'none'

.. _tb.config.tc_lab_git_clone_apply_patches_dir:

- tb.config.tc_lab_git_clone_apply_patches_dir

| directory with patches for applying with
| testcase tc_lab_apply_patches_py_
| default: 'none'

.. _tb.config.tc_lab_git_clone_apply_patches_git_am_dir:

- tb.config.tc_lab_git_clone_apply_patches_git_am_dir

| directory with patches for applying with
| testcase tc_workfd_apply_local_patches_py_
| default: 'none'

.. _tb.config.tc_lab_git_clone_source_git_reference:

- tb.config.tc_lab_git_clone_source_git_reference

| default: 'none'

.. _tb.config.tc_lab_git_clone_source_git_repo_user:

- tb.config.tc_lab_git_clone_source_git_repo_user

| default: ''

.. _tb.config.tc_lab_git_clone_source_git_repo_name:

- tb.config.tc_lab_git_clone_source_git_repo_name

| default: 'none'


------------------------------------------------

.. _tc_workfd_set_toolchain_py:

**************************
tc_workfd_set_toolchain.py
**************************

https://github.com/hsdenx/tbot/blob/master/src/tc/tc_workfd_set_toolchain.py


set the toolchain, dependend on the architecture setting in

tb.config.tc_workfd_set_toolchain_arch_

or source script set with tb.config.tc_workfd_set_toolchain_source_

if tb.config.tc_workfd_set_toolchain_source_ != 'no'


supported toolchains defined in

tb.config.tc_workfd_set_toolchain_t_p_ and tb.config.tc_workfd_set_toolchain_cr_co_


set also the ARCH environment variable with the value from

tb.config.tc_workfd_set_toolchain_arch_


Add a list of also executed cmds in tb.config.tc_workfd_set_toolchain_addlist_


:usedvar:`used variables`


.. _tb.config.tc_workfd_set_toolchain_source:

- tb.config.tc_workfd_set_toolchain_source

| if != 'none' call "source tb.config.tc_workfd_set_toolchain_source"_
| default: 'none'

.. _tb.config.tc_workfd_set_toolchain_arch:

- tb.config.tc_workfd_set_toolchain_arch

| architecture set with "export ARCH=tb.config.tc_workfd_set_toolchain_arch"_
| default: 'not set'

.. _tb.config.tc_workfd_set_toolchain_addlist:

- tb.config.tc_workfd_set_toolchain_addlist

| list of commands which get called additionally
| default: 'none'

.. _tb.config.tc_workfd_set_toolchain_t_p:

- tb.config.tc_workfd_set_toolchain_t_p

| dictionary: keys   = architecture names
|             values = path to toolchains
| default: ''
| example: https://github.com/hsdenx/tbot/blob/master/config/uboot_kconfig_check.py#L57

.. _tb.config.tc_workfd_set_toolchain_cr_co:

- tb.config.tc_workfd_set_toolchain_cr_co

| dictionary: keys   = architecture names
|             values = cross compiler prefixes
| default: ''
| example: https://github.com/hsdenx/tbot/blob/master/config/uboot_kconfig_check.py#L77


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



