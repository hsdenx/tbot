Documentation of all Testcases
==============================


src/tc/board
------------


src/tc/board/bbb
,,,,,,,,,,,,,,,,


.. _src_tc_board_bbb_tc_board_bbb_restore_uboot_py:

src/tc/board/bbb/tc_board_bbb_restore_uboot.py
..............................................

::

  # start with
  # tbot.py -s lab_denx -c beagleboneblack -t tc_demo_part1.py -l log/tbot_demo_part1.log -v
  #
  # we boot from sd card, if it is broken, we boot
  # from emmc and restore a known working uboot on
  # the sdcard.
  #
  # To switch between botmodes we can use the PIN P8_43
  # attached to GND -> boot from emmc, floating -> boot
  # from sd card.
  
  import time
  from tbotlib import tbot
  
  # switch to bootmode emmc
  tb.write_lx_cmd_check(tb.c_ctrl, 'relais   relsrv-02-02  1  on')
  tb.eof_call_tc("tc_lab_poweroff.py")
  time.sleep(2)
  tb.eof_call_tc("tc_lab_poweron.py")
  tb.set_board_state("u-boot")
  
  # set latest, so we do not load uboot env, nor do we reset
  # in tc_ub_upd_uboot.py and tc_ub_upd_spl.py
  tb.config.tc_ub_upd_uboot_latest = 'yes'
  tb.config.tc_ub_upd_spl_latest = 'yes'
  
  # call tc tc_ub_load_board_env.py
  tb.eof_call_tc("tc_ub_load_board_env.py")
  
  # set latest images
  import tc_ub_testfkt
  
  tc_ub_testfkt.ub_setenv(tb, tb.c_con, 'ubfile', 'bbb/tbot/latestworking-u-boot.img')
  tc_ub_testfkt.ub_setenv(tb, tb.c_con, 'mlofile', 'bbb/tbot/latestworking-MLO')
  
  # call upd_uboot
  tb.eof_call_tc("tc_ub_upd_uboot.py")
  
  # call upd_spl
  tb.eof_call_tc("tc_ub_upd_spl.py")
  
  
  # switch to bootmode sdcard
  tb.write_lx_cmd_check(tb.c_ctrl, 'relais   relsrv-02-02  1  off')
  tb.eof_call_tc("tc_lab_poweroff.py")
  time.sleep(2)
  tb.eof_call_tc("tc_lab_poweron.py")
  tb.set_board_state("u-boot")
  
  tb.end_tc(True)

used Testcases:

:ref:`src_tc_demo_tc_demo_part1_py`.
:ref:`src_tc_uboot_tc_ub_upd_uboot_py`.
:ref:`src_tc_uboot_tc_ub_upd_spl_py`.
:ref:`src_tc_uboot_tc_ub_load_board_env_py`.
:ref:`_tc_ub_testfkt`.
:ref:`_tc_ub_testfkt_ub_setenv(tb,`.
:ref:`_tc_ub_testfkt_ub_setenv(tb,`.

used config variables:

:ref:`tb_write_lx_cmd_check(tb_c_ctrl,`.
:ref:`tb_eof_call_tc("tc_lab_poweroff_py")`.
:ref:`tb_eof_call_tc("tc_lab_poweron_py")`.
:ref:`tb_set_board_state("u-boot")`.
:ref:`tb_config_tc_ub_upd_uboot_latest`.
:ref:`tb_config_tc_ub_upd_spl_latest`.
:ref:`tb_eof_call_tc("tc_ub_load_board_env_py")`.
:ref:`tb_c_con,`.
:ref:`tb_c_con,`.
:ref:`tb_eof_call_tc("tc_ub_upd_uboot_py")`.
:ref:`tb_eof_call_tc("tc_ub_upd_spl_py")`.
:ref:`tb_write_lx_cmd_check(tb_c_ctrl,`.
:ref:`tb_eof_call_tc("tc_lab_poweroff_py")`.
:ref:`tb_eof_call_tc("tc_lab_poweron_py")`.
:ref:`tb_set_board_state("u-boot")`.
:ref:`tb_end_tc(True)`.



https://github.com/hsdenx/tbot/tree/master/src/tc/board/bbb/tc_board_bbb_restore_uboot.py


src/tc/board/cuby
,,,,,,,,,,,,,,,,,


src/tc/board/cuby-temp
,,,,,,,,,,,,,,,,,,,,,,


.. _src_tc_board_cuby-temp_tc_board_cuby_lx_pru_py:

src/tc/board/cuby-temp/tc_board_cuby_lx_pru.py
..............................................

::

  # start with
  # tbot.py -s lab_denx -c cuby -t tc_board_cuby_lx_pru.py
  # test linux pruss

used Testcases:

:ref:`src_tc_board_cuby-temp_tc_board_cuby_lx_pru_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/cuby-temp/tc_board_cuby_lx_pru.py


.. _src_tc_board_cuby-temp_tc_board_cuby_lx_tests_py:

src/tc/board/cuby-temp/tc_board_cuby_lx_tests.py
................................................

::

  # start with
  # tbot.py -s lab_denx -c cuby -t tc_board_cuby_lx_tests.py
  # start all linux testcases for the cuby board

used Testcases:

:ref:`src_tc_board_cuby-temp_tc_board_cuby_lx_tests_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/cuby-temp/tc_board_cuby_lx_tests.py


.. _src_tc_board_cuby-temp_tc_board_cuby_sd_image_tests_py:

src/tc/board/cuby-temp/tc_board_cuby_sd_image_tests.py
......................................................

::

  # start with
  # tbot.py -s lab_denx -c cuby -t tc_board_cuby_sd_image_tests.py
  # test the sd image, which is created from yocto build

used Testcases:

:ref:`src_tc_board_cuby-temp_tc_board_cuby_sd_image_tests_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/cuby-temp/tc_board_cuby_sd_image_tests.py


.. _src_tc_board_cuby-temp_tc_board_cuby_yocto_install_py:

src/tc/board/cuby-temp/tc_board_cuby_yocto_install.py
.....................................................

::

  # start with
  # tbot.py -s lab_denx -c cuby -t tc_board_cuby_yocto_install.py
  # install yocto for the cuby board, and bitbake.

used Testcases:

:ref:`src_tc_board_cuby-temp_tc_board_cuby_yocto_install_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/cuby-temp/tc_board_cuby_yocto_install.py


.. _src_tc_board_cuby-temp_tc_board_cuby_yocto_test_py:

src/tc/board/cuby-temp/tc_board_cuby_yocto_test.py
..................................................

::

  # start with
  # tbot.py -s lab_denx -c cuby -t tc_board_cuby_yocto_test.py
  # do tests with the resulting images from a yocto buil

used Testcases:

:ref:`src_tc_board_cuby-temp_tc_board_cuby_yocto_test_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/cuby-temp/tc_board_cuby_yocto_test.py


.. _src_tc_board_tc_board_aristainetos2_py:

src/tc/board/tc_board_aristainetos2.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c aristainetos2 -t tc_board_aristainetos2.py
  # start all testcases for the aristainetos2 board
  # tc_board_aristainetos2_linux_tests.py
  # tc_workfd_set_toolchain.py

used Testcases:

:ref:`src_tc_board_tc_board_aristainetos2_py`.
:ref:`src_tc_board_tc_board_aristainetos2_linux_tests_py`.
:ref:`src_tc_tc_workfd_set_toolchain_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_aristainetos2.py


.. _src_tc_board_tc_board_aristainetos2_linux_py:

src/tc/board/tc_board_aristainetos2_linux.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c aristainetos2 -t tc_board_aristainetos2_linux.py
  # start all linux testcases for the aristainetos2 board

used Testcases:

:ref:`src_tc_board_tc_board_aristainetos2_linux_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_aristainetos2_linux.py


.. _src_tc_board_tc_board_aristainetos2_linux_bisect_py:

src/tc/board/tc_board_aristainetos2_linux_bisect.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c aristainetos2 -t tc_board_aristainetos2_linux_bisect.py
  # start a git bisect for the aristainetos2 board

used Testcases:

:ref:`src_tc_board_tc_board_aristainetos2_linux_bisect_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_aristainetos2_linux_bisect.py


.. _src_tc_board_tc_board_aristainetos2_linux_tests_py:

src/tc/board/tc_board_aristainetos2_linux_tests.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c aristainetos2 -t tc_board_aristainetos2_linux_tests.py
  # start all linux testcases for the aristainetos2 board

used Testcases:

:ref:`src_tc_board_tc_board_aristainetos2_linux_tests_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_aristainetos2_linux_tests.py


.. _src_tc_board_tc_board_ccu1_tests_py:

src/tc/board/tc_board_ccu1_tests.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c ccu1 -t tc_board_ccu1_tests.py
  # start all testcases for the ccu1 board

used Testcases:

:ref:`src_tc_board_tc_board_ccu1_tests_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_ccu1_tests.py


.. _src_tc_board_tc_board_corvus_py:

src/tc/board/tc_board_corvus.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c corvus -t tc_board_corvus.py
  # start all testcases for the corvus board

used Testcases:

:ref:`src_tc_board_tc_board_corvus_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_corvus.py


.. _src_tc_board_tc_board_dxr2_py:

src/tc/board/tc_board_dxr2.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c dxr2 -t tc_board_dxr2.py
  # start all testcases for the dxr2 board

used Testcases:

:ref:`src_tc_board_tc_board_dxr2_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_dxr2.py


.. _src_tc_board_tc_board_dxr2_linux_py:

src/tc/board/tc_board_dxr2_linux.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c dxr2 -t tc_board_dxr2_linux.py
  # start all linux testcases for the dxr2 board

used Testcases:

:ref:`src_tc_board_tc_board_dxr2_linux_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_dxr2_linux.py


.. _src_tc_board_tc_board_dxr2_lx_ubi_tests_py:

src/tc/board/tc_board_dxr2_lx_ubi_tests.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_board_dxr2_lx_ubi_tests.py
  # more dxr2 specific ubi tests, maybe make them common

used Testcases:

:ref:`src_tc_board_tc_board_dxr2_lx_ubi_tests_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_dxr2_lx_ubi_tests.py


.. _src_tc_board_tc_board_dxr2_ub_py:

src/tc/board/tc_board_dxr2_ub.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c dxr2 -t tc_board_dxr2_ub.py
  # start all u-boot testcases for the dxr2 board

used Testcases:

:ref:`src_tc_board_tc_board_dxr2_ub_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_dxr2_ub.py


.. _src_tc_board_tc_board_dxr2_ub_ubi_py:

src/tc/board/tc_board_dxr2_ub_ubi.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c dxr2 -t tc_board_dxr2_ub_ubi.py
  # start all ubi testcases for the dxr2 board

used Testcases:

:ref:`src_tc_board_tc_board_dxr2_ub_ubi_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_dxr2_ub_ubi.py


.. _src_tc_board_tc_board_dxr2_uboot_patchwork_py:

src/tc/board/tc_board_dxr2_uboot_patchwork.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot_dxr2_uboot.cfg -t tc_board_dxr2_uboot_patchwork.py
  # dxr2 check all patches with patchworknumber > default_nr
  # in patchwork, if it is checkpatch clean and applies to
  # current mainline without errors

used Testcases:

:ref:`src_tc_board_tc_board_dxr2_uboot_patchwork_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_dxr2_uboot_patchwork.py


.. _src_tc_board_tc_board_fipad_py:

src/tc/board/tc_board_fipad.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c fipad -t tc_board_fipad.py
  # start all U-Boot/linux testcases for the fipad board

used Testcases:

:ref:`src_tc_board_tc_board_fipad_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_fipad.py


.. _src_tc_board_tc_board_fipad_linux_py:

src/tc/board/tc_board_fipad_linux.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c fipad -t tc_board_fipad_linux.py
  # start all linux testcases for the fipad board

used Testcases:

:ref:`src_tc_board_tc_board_fipad_linux_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_fipad_linux.py


.. _src_tc_board_tc_board_fipad_ub_tests_py:

src/tc/board/tc_board_fipad_ub_tests.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c fipad -t tc_board_fipad_ub_tests.py
  # start all U-Boot testcases for the fipad board

used Testcases:

:ref:`src_tc_board_tc_board_fipad_ub_tests_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_fipad_ub_tests.py


.. _src_tc_board_tc_board_fipad_ub_usb_py:

src/tc/board/tc_board_fipad_ub_usb.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_board_fipad_ub_usb.py
  #
  # do some simple usb test
  # - usb start
  # - usb info (check some output)
  # - list root dir on the stick
  #   (ext2 formatted stick)
  # - load test.bin from this partition with ext2load
  # - check if test.bin has the crc32 sum 0x2144df1c
  #
  # used vars:
  # tb.config.tc_uboot_usb_info_expect = [
  #    'Hub,  USB Revision 2.0',
  #    'Mass Storage,  USB Revision 2.0',
  #    'SMI Corporation USB DISK AA04012900007453',
  #    'Vendor: 0x090c  Product 0x1000 Version 17.0'
  # ]
  # tb.config.tc_board_fipad_uboot_ext2load_files = ['test.bin']
  #   list of files which get load and crc32 tested

used Testcases:

:ref:`src_tc_board_tc_board_fipad_ub_usb_py`.

used config variables:

:ref:`tb_config_tc_uboot_usb_info_expect`.
:ref:`tb_config_tc_board_fipad_uboot_ext2load_files`.



https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_fipad_ub_usb.py


.. _src_tc_board_tc_board_fipad_upd_ub_py:

src/tc/board/tc_board_fipad_upd_ub.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c fipad -t tc_board_fipad_upd_ub.py
  # update SPL and u-boot.img on the SPI NOR or the MMC0
  # card, and boot it ...

used Testcases:

:ref:`src_tc_board_tc_board_fipad_upd_ub_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_fipad_upd_ub.py


.. _src_tc_board_tc_board_fipad_upd_ub_mmc_py:

src/tc/board/tc_board_fipad_upd_ub_mmc.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c fipad -t tc_board_fipad_upd_ub_mmc.py
  # update SPL and u-boot.img on the MMC0

used Testcases:

:ref:`src_tc_board_tc_board_fipad_upd_ub_mmc_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_fipad_upd_ub_mmc.py


.. _src_tc_board_tc_board_fipad_upd_ub_spi_py:

src/tc/board/tc_board_fipad_upd_ub_spi.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c fipad -t tc_board_fipad_upd_ub_spi.py
  # update SPL and u-boot.img on the SPI NOR

used Testcases:

:ref:`src_tc_board_tc_board_fipad_upd_ub_spi_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_fipad_upd_ub_spi.py


.. _src_tc_board_tc_board_flea3_py:

src/tc/board/tc_board_flea3.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c flea3 -t tc_board_flea3.py
  # start all testcases for the flea3 board
  # currently only test the nor unprotect with linux

used Testcases:

:ref:`src_tc_board_tc_board_flea3_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_flea3.py


.. _src_tc_board_tc_board_mcx_py:

src/tc/board/tc_board_mcx.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c mcx -t tc_board_mcx.py
  # start all testcases for the mcx board linux stable and linux-ml

used Testcases:

:ref:`src_tc_board_tc_board_mcx_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_mcx.py


.. _src_tc_board_tc_board_mcx_tests_py:

src/tc/board/tc_board_mcx_tests.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c mcx -t tc_board_mcx_tests.py
  # start all testcases for the mcx board

used Testcases:

:ref:`src_tc_board_tc_board_mcx_tests_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_mcx_tests.py


.. _src_tc_board_tc_board_shc_py:

src/tc/board/tc_board_shc.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c shc -t tc_board_shc.py
  # start all testcases for the shc board linux and linux-stable

used Testcases:

:ref:`src_tc_board_tc_board_shc_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_shc.py


.. _src_tc_board_tc_board_shc_compile_ml_py:

src/tc/board/tc_board_shc_compile_ml.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c shc -t tc_board_shc_compile_ml.py
  # compile ML linux kernel for the shc board

used Testcases:

:ref:`src_tc_board_tc_board_shc_compile_ml_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_shc_compile_ml.py


.. _src_tc_board_tc_board_shc_tests_py:

src/tc/board/tc_board_shc_tests.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c shc -t tc_board_shc_tests.py
  # start all testcases for the shc board

used Testcases:

:ref:`src_tc_board_tc_board_shc_tests_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_shc_tests.py


.. _src_tc_board_tc_board_shc_ub_create_regdump_py:

src/tc/board/tc_board_shc_ub_create_regdump.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c shc -t tc_board_shc_ub_create_regdump.py
  # create a uboot regdump for all interesting registers
  # on the shc board

used Testcases:

:ref:`src_tc_board_tc_board_shc_ub_create_regdump_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_shc_ub_create_regdump.py


.. _src_tc_board_tc_board_shc_ub_tests_py:

src/tc/board/tc_board_shc_ub_tests.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c shc -t tc_board_shc_ub_tests.py
  # start all U-Boot testcases for the shc board

used Testcases:

:ref:`src_tc_board_tc_board_shc_ub_tests_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_shc_ub_tests.py


.. _src_tc_board_tc_board_shc_uboot_git_bisect_py:

src/tc/board/tc_board_shc_uboot_git_bisect.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c shc -t tc_board_shc_uboot_git_bisect.py
  # start tc:

used Testcases:

:ref:`src_tc_board_tc_board_shc_uboot_git_bisect_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_shc_uboot_git_bisect.py


.. _src_tc_board_tc_board_shc_upd_ub_py:

src/tc/board/tc_board_shc_upd_ub.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c shc -t tc_board_shc_upd_ub.py
  # update MLO and u-boot.img on the SD card or the eMMC
  # card, and boot it ...

used Testcases:

:ref:`src_tc_board_tc_board_shc_upd_ub_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_shc_upd_ub.py


.. _src_tc_board_tc_board_sigmatek-nand_py:

src/tc/board/tc_board_sigmatek-nand.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c sigmatek-nand -t tc_board_sigmatek-nand.py
  # On the sigmatek-nand board we have problems with a crash in U-boot
  # We do:
  # - wait until linux state is reached
  # - wait random seconds (3 -10)
  # - power off the board
  # - wait 3 seconds for powering really of the board
  # - loop this 50 times

used Testcases:

:ref:`src_tc_board_tc_board_sigmatek-nand_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_sigmatek-nand.py


.. _src_tc_board_tc_board_sirius_dds_py:

src/tc/board/tc_board_sirius_dds.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot_sirius_dds.cfg -t tc_board_sirius_dds.py
  # On the sirius board we have problems with ubifs
  # on nand flash and power cuts. So this is a special
  # testcase for this board. We do:
  # - go into statte u-boot
  # - start linux with ubifs as rootfs
  # - wait until Userspace APP SiriusApplicat is started
  # - wait random seconds (3 -10)
  # - power off the board
  # - wait 3 seconds for powering really of the board
  # - loop this 50 times
  # if we have an ubifs error, testcase ends with error

used Testcases:

:ref:`src_tc_board_tc_board_sirius_dds_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_sirius_dds.py


.. _src_tc_board_tc_board_smartweb_py:

src/tc/board/tc_board_smartweb.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c smartweb -t tc_board_smartweb.py
  #
  # remove, clone current mainline U-Boot, then
  # start tc_board_smartweb_test_ub.py

used Testcases:

:ref:`src_tc_board_tc_board_smartweb_py`.
:ref:`src_tc_board_tc_board_smartweb_test_ub_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_smartweb.py


.. _src_tc_board_tc_board_smartweb_test_ub_py:

src/tc/board/tc_board_smartweb_test_ub.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c smartweb -t tc_board_smartweb.py
  # start all ub testcases for the smartweb board

used Testcases:

:ref:`src_tc_board_tc_board_smartweb_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_smartweb_test_ub.py


.. _src_tc_board_tc_board_taurus_py:

src/tc/board/tc_board_taurus.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c taurus -t tc_board_taurus.py
  # start all testcases for the taurus board

used Testcases:

:ref:`src_tc_board_tc_board_taurus_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_taurus.py


.. _src_tc_board_tc_board_tqm5200s_try_cur_ub_py:

src/tc/board/tc_board_tqm5200s_try_cur_ub.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c tqm5200s -t tc_board_tqm5200s_try_cur_ub.py
  # remove current u-boot code on the lab PC
  # then call tc tc_board_tqm5200s_ub_comp_install.py

used Testcases:

:ref:`src_tc_board_tc_board_tqm5200s_try_cur_ub_py`.
:ref:`src_tc_board_tc_board_tqm5200s_ub_comp_install_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_tqm5200s_try_cur_ub.py


.. _src_tc_board_tc_board_tqm5200s_ub_comp_install_py:

src/tc/board/tc_board_tqm5200s_ub_comp_install.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c tqm5200s -t tc_board_tqm5200s_ub_comp_install.py
  # compile and install U-Boot for the tqm5200s board
  # install U-Boot with BDI

used Testcases:

:ref:`src_tc_board_tc_board_tqm5200s_ub_comp_install_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_board_tqm5200s_ub_comp_install.py


.. _src_tc_board_tc_linux_create_reg_file_am335x_py:

src/tc/board/tc_linux_create_reg_file_am335x.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c cuby -t tc_linux_create_reg_file_am335x.py
  # create a regfile for am335x SoC registers

used Testcases:

:ref:`src_tc_board_tc_linux_create_reg_file_am335x_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_linux_create_reg_file_am335x.py


.. _src_tc_board_tc_linux_create_reg_file_at91sam9g15_py:

src/tc/board/tc_linux_create_reg_file_at91sam9g15.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot_wivue2.cfg -t tc_linux_create_reg_file_at91sam9g15.py
  # create a regfile for at91sam9g15 SoC registers

used Testcases:

:ref:`src_tc_board_tc_linux_create_reg_file_at91sam9g15_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_linux_create_reg_file_at91sam9g15.py


.. _src_tc_board_tc_linux_create_reg_file_imx6qdl_py:

src/tc/board/tc_linux_create_reg_file_imx6qdl.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c aristainetos2 -t tc_linux_create_reg_file_imx6qdl.py
  # create a regfile for am335x SoC registers

used Testcases:

:ref:`src_tc_board_tc_linux_create_reg_file_imx6qdl_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/board/tc_linux_create_reg_file_imx6qdl.py


src/tc/debugger
---------------


src/tc/debugger/bdi
,,,,,,,,,,,,,,,,,,,


.. _src_tc_debugger_bdi_tc_lab_bdi_connect_py:

src/tc/debugger/bdi/tc_lab_bdi_connect.py
.........................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_bdi_connect.py
  # connect to the BDI if tb.config.board_has_debugger != 0
  # - send to workfd tb.config.lab_bdi_upd_uboot_bdi_cmd
  # - set BDI prompt tb.config.lab_bdi_upd_uboot_bdi_prompt
  # - wait for BDI prompt

used Testcases:

:ref:`src_tc_debugger_bdi_tc_lab_bdi_connect_py`.

used config variables:

:ref:`tb_config_board_has_debugger`.
:ref:`tb_config_lab_bdi_upd_uboot_bdi_cmd`.
:ref:`tb_config_lab_bdi_upd_uboot_bdi_prompt`.



https://github.com/hsdenx/tbot/tree/master/src/tc/debugger/bdi/tc_lab_bdi_connect.py


.. _src_tc_debugger_bdi_tc_lab_bdi_create_dump_py:

src/tc/debugger/bdi/tc_lab_bdi_create_dump.py
.............................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_bdi_create_dump.py
  #
  # check if we are on the BDI already, if not switch to it
  # with tc_lab_bdi_connect.py
  #
  # - send "halt"
  # - dump registers from tb.config.tc_lab_bdi_create_dump_start
  #   to tb.config.tc_lab_bdi_create_dump_stop with mask
  #   tb.config.tc_lab_bdi_create_dump_mask and stepsize
  #   tb.config.tc_lab_bdi_create_dump_type into the file
  #   tb.config.tc_lab_bdi_create_dump_filename

used Testcases:

:ref:`src_tc_debugger_bdi_tc_lab_bdi_create_dump_py`.
:ref:`src_tc_debugger_bdi_tc_lab_bdi_connect_py`.

used config variables:

:ref:`tb_config_tc_lab_bdi_create_dump_start`.
:ref:`tb_config_tc_lab_bdi_create_dump_stop`.
:ref:`tb_config_tc_lab_bdi_create_dump_mask`.
:ref:`tb_config_tc_lab_bdi_create_dump_type`.
:ref:`tb_config_tc_lab_bdi_create_dump_filename`.



https://github.com/hsdenx/tbot/tree/master/src/tc/debugger/bdi/tc_lab_bdi_create_dump.py


.. _src_tc_debugger_bdi_tc_lab_bdi_disconnect_py:

src/tc/debugger/bdi/tc_lab_bdi_disconnect.py
............................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_bdi_disconnect.py
  # disconnect from the BDI
  # - send bdi command "quit"
  # - set tb.config.linux_prompt

used Testcases:

:ref:`src_tc_debugger_bdi_tc_lab_bdi_disconnect_py`.

used config variables:

:ref:`tb_config_linux_prompt`.



https://github.com/hsdenx/tbot/tree/master/src/tc/debugger/bdi/tc_lab_bdi_disconnect.py


.. _src_tc_debugger_bdi_tc_lab_bdi_run_py:

src/tc/debugger/bdi/tc_lab_bdi_run.py
.....................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_bdi_upd_uboot.py
  # BDI run
  # - send "res halt" to workfd
  # - send BDI cmd tb.config.lab_bdi_upd_uboot_bdi_run

used Testcases:

:ref:`src_tc_debugger_bdi_tc_lab_bdi_upd_uboot_py`.

used config variables:

:ref:`tb_config_lab_bdi_upd_uboot_bdi_run`.



https://github.com/hsdenx/tbot/tree/master/src/tc/debugger/bdi/tc_lab_bdi_run.py


.. _src_tc_debugger_bdi_tc_lab_bdi_upd_uboot_py:

src/tc/debugger/bdi/tc_lab_bdi_upd_uboot.py
...........................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_bdi_upd_uboot.py
  # update u-boot with BDI
  # - send BDI cmd: "res halt"
  # - send BDI cmd: "era"
  # - send BDI cmd:
  #   tb.config.lab_bdi_upd_uboot_bdi_prog + ' ' + tb.config.lab_bdi_upd_uboot_bdi_file + ' BIN'
  # - send BDI cmd: tb.config.lab_bdi_upd_uboot_bdi_run

used Testcases:

:ref:`src_tc_debugger_bdi_tc_lab_bdi_upd_uboot_py`.

used config variables:

:ref:`tb_config_lab_bdi_upd_uboot_bdi_prog`.
:ref:`tb_config_lab_bdi_upd_uboot_bdi_file`.
:ref:`tb_config_lab_bdi_upd_uboot_bdi_run`.



https://github.com/hsdenx/tbot/tree/master/src/tc/debugger/bdi/tc_lab_bdi_upd_uboot.py


src/tc/default
--------------


.. _src_tc_default_tc_def_tbot_py:

src/tc/default/tc_def_tbot.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c cfgfile -t tc_def_tbot.py
  # simple set default values for tbot

used Testcases:

:ref:`src_tc_default_tc_def_tbot_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/default/tc_def_tbot.py


.. _src_tc_default_tc_def_ub_py:

src/tc/default/tc_def_ub.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c cfgfile -t tc_def_ub.py
  # simple set default values for U-Boot testcases

used Testcases:

:ref:`src_tc_default_tc_def_ub_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/default/tc_def_ub.py


src/tc/demo
-----------


.. _src_tc_demo_tc_demo_can_part1_py:

src/tc/demo/tc_demo_can_part1.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot_board.cfg -t tc_demo_can_part1.py
  # start tc:
  # starts a can demo
  # For this demo the fipad board in the denx lab is used.
  # To test the CAN bus we have in the DENX lab installed a PC, called
  # CANPC to which a PEAK CAN adapter is attached, which then is connected
  # to the CAN bus the fipad board is also connected.
  #
  # We use tc_workfd_can.py for testing
  #
  # We open a new connection to the LabPC, called canm and then we ssh
  # to the CANPC, from where we then start candump, while on the console
  # connection a cansend was started. So we can read from the canm
  # connection, the bytes we send with cansend on the console connection.
  #
  # If we got the same bytes as we send -> TC True
  # else the TC returns False
  #
  # Only one cansend call is tested ... room for more.

used Testcases:

:ref:`src_tc_demo_tc_demo_can_part1_py`.
:ref:`src_tc_linux_tc_workfd_can_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/demo/tc_demo_can_part1.py


.. _src_tc_demo_tc_demo_compile_install_test_py:

src/tc/demo/tc_demo_compile_install_test.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -c -s lab_denx -c demo -t tc_demo_compile_install_test.py
  # start tc:
  # - compile source tree
  # - install bin on board
  # - call board uboot testcase tb.config.tc_demo_compile_install_test_name
  # tb.config.tc_demo_compile_install_test_files contains a list of files,
  # which are copied to
  # tb.config.tftprootdir + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir

used Testcases:

:ref:`src_tc_demo_tc_demo_compile_install_test_py`.

used config variables:

:ref:`tb_config_tc_demo_compile_install_test_name`.
:ref:`tb_config_tc_demo_compile_install_test_files`.
:ref:`tb_config_tftprootdir`.
:ref:`tb_config_tftpboardname`.
:ref:`tb_config_ub_load_board_env_subdir`.



https://github.com/hsdenx/tbot/tree/master/src/tc/demo/tc_demo_compile_install_test.py


.. _src_tc_demo_tc_demo_get_ub_code_py:

src/tc/demo/tc_demo_get_ub_code.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot_board.cfg -t tc_demo_get_ub_code.py
  # start tc:
  # - rm old u-boot tree (if there is one)
  # - tc_lab_get_uboot_source.py
  # - 

used Testcases:

:ref:`src_tc_demo_tc_demo_get_ub_code_py`.
:ref:`src_tc_tc_lab_get_uboot_source_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/demo/tc_demo_get_ub_code.py


.. _src_tc_demo_tc_demo_linux_test_py:

src/tc/demo/tc_demo_linux_test.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c beagleboneblack -t tc_demo_linux_test.py
  # get linux code and compile it for a board, and boot the
  # resulting kernel, and do some basic tests:
  #
  # - grep through dmesg and check if strings in
  #   tb.config.tc_demo_linux_test_dmesg exist
  # - check with devmem2 if the register values defined
  #   in the register files tb.config.tc_demo_linux_test_reg_files
  #   are identical with the values defined in the files
  # - start cmd defined in tb.config.tc_demo_linux_test_basic_cmd
  #   and check the returning strings.
  #

used Testcases:

:ref:`src_tc_demo_tc_demo_linux_test_py`.

used config variables:

:ref:`tb_config_tc_demo_linux_test_dmesg`.
:ref:`tb_config_tc_demo_linux_test_reg_files`.
:ref:`tb_config_tc_demo_linux_test_basic_cmd`.



https://github.com/hsdenx/tbot/tree/master/src/tc/demo/tc_demo_linux_test.py


.. _src_tc_demo_tc_demo_part1_py:

src/tc/demo/tc_demo_part1.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c smartweb -t tc_demo_part1.py
  # start tc:
  # - call tc_demo_get_ub_code.py
  # - call tc_demo_compile_install_test.py

used Testcases:

:ref:`src_tc_demo_tc_demo_part1_py`.
:ref:`src_tc_demo_tc_demo_get_ub_code_py`.
:ref:`src_tc_demo_tc_demo_compile_install_test_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/demo/tc_demo_part1.py


.. _src_tc_demo_tc_demo_part2_py:

src/tc/demo/tc_demo_part2.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c smartweb -t tc_demo_part2.py
  # start tc:
  # - call tc_demo_get_ub_code.py
  # - call tc_demo_compile_install_test.py

used Testcases:

:ref:`src_tc_demo_tc_demo_part2_py`.
:ref:`src_tc_demo_tc_demo_get_ub_code_py`.
:ref:`src_tc_demo_tc_demo_compile_install_test_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/demo/tc_demo_part2.py


.. _src_tc_demo_tc_demo_part3_py:

src/tc/demo/tc_demo_part3.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c smartweb -t tc_demo_part3.py
  # start tc:

used Testcases:

:ref:`src_tc_demo_tc_demo_part3_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/demo/tc_demo_part3.py


.. _src_tc_demo_tc_demo_uboot_tests_py:

src/tc/demo/tc_demo_uboot_tests.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c smartweb -t tc_demo_uboot_tests.py
  # start all "standard" u-boot testcases

used Testcases:

:ref:`src_tc_demo_tc_demo_uboot_tests_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/demo/tc_demo_uboot_tests.py


src/tc/lab
----------


src/tc/lab/denx
,,,,,,,,,,,,,,,


.. _src_tc_lab_denx_tc_lab_denx_connect_to_board_py:

src/tc/lab/denx/tc_lab_denx_connect_to_board.py
...............................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_denx_connect_to_board.py
  # connect to board with connect

used Testcases:

:ref:`src_tc_lab_denx_tc_lab_denx_connect_to_board_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/lab/denx/tc_lab_denx_connect_to_board.py


.. _src_tc_lab_denx_tc_lab_denx_disconnect_from_board_py:

src/tc/lab/denx/tc_lab_denx_disconnect_from_board.py
....................................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_denx_disconnect_from_board.py
  # disconnect from board in denx vlab

used Testcases:

:ref:`src_tc_lab_denx_tc_lab_denx_disconnect_from_board_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/lab/denx/tc_lab_denx_disconnect_from_board.py


.. _src_tc_lab_denx_tc_lab_denx_get_power_state_py:

src/tc/lab/denx/tc_lab_denx_get_power_state.py
..............................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_denx_get_power_state.py
  # get the power state of the board, and save it in
  # tb.power_state

used Testcases:

:ref:`src_tc_lab_denx_tc_lab_denx_get_power_state_py`.

used config variables:

:ref:`tb_power_state`.



https://github.com/hsdenx/tbot/tree/master/src/tc/lab/denx/tc_lab_denx_get_power_state.py


.. _src_tc_lab_denx_tc_lab_denx_power_py:

src/tc/lab/denx/tc_lab_denx_power.py
....................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_denx_power.py
  # power on/off the board 

used Testcases:

:ref:`src_tc_lab_denx_tc_lab_denx_power_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/lab/denx/tc_lab_denx_power.py


.. _src_tc_lab_denx_tc_lab_interactive_get_power_state_py:

src/tc/lab/denx/tc_lab_interactive_get_power_state.py
.....................................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_denx_get_power_state.py
  # get the power state of the board through user input,
  # and save it in tb.power_state

used Testcases:

:ref:`src_tc_lab_denx_tc_lab_denx_get_power_state_py`.

used config variables:

:ref:`tb_power_state`.



https://github.com/hsdenx/tbot/tree/master/src/tc/lab/denx/tc_lab_interactive_get_power_state.py


.. _src_tc_lab_denx_tc_lab_interactive_power_py:

src/tc/lab/denx/tc_lab_interactive_power.py
...........................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_denx_power.py
  # power on/off the board from hand

used Testcases:

:ref:`src_tc_lab_denx_tc_lab_denx_power_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/lab/denx/tc_lab_interactive_power.py


.. _src_tc_lab_tc_lab_kmtronic_get_power_state_py:

src/tc/lab/tc_lab_kmtronic_get_power_state.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_kmtronic_get_power_state.py
  # power on/off the board
  #
  # get the power state of the board attached to a kmtronic usb relay:
  # 
  # http://info.kmtronic.com/kmtronic-usb-relay-test-software.html
  # 
  # and save it in tb.power_state
  #
  # use testcase "tc_lab_kmtronic_get_variables.py" for setting
  # the serial and the index you need for the specific board.
  #
  # This file is an example for a setup, you need to adapt
  # this to your needs.
  #

used Testcases:

:ref:`src_tc_lab_tc_lab_kmtronic_get_power_state_py`.

used config variables:

:ref:`tb_power_state`.

links:

http://info.kmtronic.com/kmtronic-usb-relay-test-software.html



https://github.com/hsdenx/tbot/tree/master/src/tc/lab/tc_lab_kmtronic_get_power_state.py


.. _src_tc_lab_tc_lab_kmtronic_get_variables_py:

src/tc/lab/tc_lab_kmtronic_get_variables.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_kmtronic_get_variables.py
  # get tty device tb.config.kmtronic_dev and
  # tb.config.kmtronic_addr
  # for the kmtronic usb relay, see:
  # 
  # http://info.kmtronic.com/kmtronic-usb-relay-test-software.html
  #

used Testcases:

:ref:`src_tc_lab_tc_lab_kmtronic_get_variables_py`.

used config variables:

:ref:`tb_config_kmtronic_dev`.
:ref:`tb_config_kmtronic_addr`.

links:

http://info.kmtronic.com/kmtronic-usb-relay-test-software.html



https://github.com/hsdenx/tbot/tree/master/src/tc/lab/tc_lab_kmtronic_get_variables.py


.. _src_tc_lab_tc_lab_kmtronic_set_power_state_py:

src/tc/lab/tc_lab_kmtronic_set_power_state.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_kmtronic_set_power_state.py
  # power on/off the board
  #
  # get the power state of the board attached to a kmtronic usb relay:
  # 
  # http://info.kmtronic.com/kmtronic-usb-relay-test-software.html
  # 
  # and save it in tb.power_state
  #
  # use testcase "tc_lab_kmtronic_get_variables.py" for setting
  # the serial and the index you need for the specific board.
  #
  # This file is an example for a setup, you need to adapt
  # this to your needs.
  #

used Testcases:

:ref:`src_tc_lab_tc_lab_kmtronic_set_power_state_py`.

used config variables:

:ref:`tb_power_state`.

links:

http://info.kmtronic.com/kmtronic-usb-relay-test-software.html



https://github.com/hsdenx/tbot/tree/master/src/tc/lab/tc_lab_kmtronic_set_power_state.py


.. _src_tc_lab_tc_lab_sispmctl_get_power_state_py:

src/tc/lab/tc_lab_sispmctl_get_power_state.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_sispmctl_get_power_state.py
  # get the power state of the board through sispmctl
  # and save it in tb.power_state
  # find more information for the Gembird Silver Shield PM power controller:
  # http://sispmctl.sourceforge.net/
  #
  # use testcase "tc_lab_sispmctl_get_variables.py" for setting
  # the serial and the index you need for the specific board.
  #
  # This file is an example for a setup, you need to adapt
  # this to your needs.
  #

used Testcases:

:ref:`src_tc_lab_tc_lab_sispmctl_get_power_state_py`.

used config variables:

:ref:`tb_power_state`.

links:

http://sispmctl.sourceforge.net/



https://github.com/hsdenx/tbot/tree/master/src/tc/lab/tc_lab_sispmctl_get_power_state.py


.. _src_tc_lab_tc_lab_sispmctl_get_variables_py:

src/tc/lab/tc_lab_sispmctl_get_variables.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_sispmctl_get_variables.py
  # get serial and index for tb.config.boardlabpowername for
  # controlling the Gembird Silver Shield PM power controller
  # and save it in tb.config.gembird_serial and tb.config.gembird_index
  #

used Testcases:

:ref:`src_tc_lab_tc_lab_sispmctl_get_variables_py`.

used config variables:

:ref:`tb_config_boardlabpowername`.
:ref:`tb_config_gembird_serial`.
:ref:`tb_config_gembird_index`.



https://github.com/hsdenx/tbot/tree/master/src/tc/lab/tc_lab_sispmctl_get_variables.py


.. _src_tc_lab_tc_lab_sispmctl_set_power_state_py:

src/tc/lab/tc_lab_sispmctl_set_power_state.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_sispmctl_set_power_state.py
  # power on/off the board
  #
  # get the power state of the board through sispmctl
  # and save it in tb.power_state
  # find more information for the Gembird Silver Shield PM power controller:
  # http://sispmctl.sourceforge.net/
  #
  # use testcase "tc_lab_sispmctl_get_variables.py" for setting
  # the serial and the index you need for the specific board.
  #
  # This file is an example for a setup, you need to adapt
  # this to your needs.
  #

used Testcases:

:ref:`src_tc_lab_tc_lab_sispmctl_set_power_state_py`.

used config variables:

:ref:`tb_power_state`.

links:

http://sispmctl.sourceforge.net/



https://github.com/hsdenx/tbot/tree/master/src/tc/lab/tc_lab_sispmctl_set_power_state.py


src/tc/linux
------------


src/tc/linux/relay
,,,,,,,,,,,,,,,,,,


.. _src_tc_linux_relay_tc_linux_relay_get_config_py:

src/tc/linux/relay/tc_linux_relay_get_config.py
...............................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_linux_relay_get_config.py
  # get relay tbot configuration
  #
  # input:
  # tb.config.tc_linux_relay_set_port
  # tb.config.tc_linux_relay_set_state
  #
  # output:
  # tb.config.tc_linux_relay_set_tc
  #   testcase which gets called for setting relay port  with state state
  # also set the config variables for tb.config.tc_linux_relay_set_tc
  # accordingly.

used Testcases:

:ref:`src_tc_linux_relay_tc_linux_relay_get_config_py`.

used config variables:

:ref:`tb_config_tc_linux_relay_set_port`.
:ref:`tb_config_tc_linux_relay_set_state`.
:ref:`tb_config_tc_linux_relay_set_tc`.
:ref:`tb_config_tc_linux_relay_set_tc`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/relay/tc_linux_relay_get_config.py


.. _src_tc_linux_relay_tc_linux_relay_set_py:

src/tc/linux/relay/tc_linux_relay_set.py
........................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_linux_relay_set.py
  # set relay port tb.config.tc_linux_relay_set_port to state
  # tb.config.tc_linux_relay_set_state.
  #
  # you need to adapt tc_linux_relay_get_config.py, which does
  # the mapping from port/state to your specific lab settings.
  #

used Testcases:

:ref:`src_tc_linux_relay_tc_linux_relay_set_py`.
:ref:`_tc_linux_relay_get_config_py,`.

used config variables:

:ref:`tb_config_tc_linux_relay_set_port`.
:ref:`tb_config_tc_linux_relay_set_state_`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/relay/tc_linux_relay_set.py


.. _src_tc_linux_relay_tc_linux_relay_simple_set_py:

src/tc/linux/relay/tc_linux_relay_simple_set.py
...............................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_linux_relay_set.py
  # set relay port with the simple cmd to state
  # find the c source code for the simple cmd in src/files/relay/simple.c
  #
  # tb.config.tc_linux_relay_simple_set_sudo if 'yes' "sudo" is perpended to
  # tb.config.tc_linux_relay_simple_set_cmd and if password is needed, password
  # is searched in password.py with board = tb.config.ip and user = tb.config.user + '_sudo'
  #

used Testcases:

:ref:`src_tc_linux_relay_tc_linux_relay_set_py`.

used config variables:

:ref:`tb_config_tc_linux_relay_simple_set_sudo`.
:ref:`tb_config_tc_linux_relay_simple_set_cmd`.
:ref:`tb_config_ip`.
:ref:`tb_config_user`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/relay/tc_linux_relay_simple_set.py


src/tc/linux/ubi
,,,,,,,,,,,,,,,,


.. _src_tc_linux_ubi_tc_lx_ubi_attach_py:

src/tc/linux/ubi/tc_lx_ubi_attach.py
....................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_ubi_attach.py

used Testcases:

:ref:`src_tc_linux_ubi_tc_lx_ubi_attach_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/ubi/tc_lx_ubi_attach.py


.. _src_tc_linux_ubi_tc_lx_ubi_detach_py:

src/tc/linux/ubi/tc_lx_ubi_detach.py
....................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_ubi_detach.py
  # detach ubi device tb.config.tc_ubi_mtd_dev

used Testcases:

:ref:`src_tc_linux_ubi_tc_lx_ubi_detach_py`.

used config variables:

:ref:`tb_config_tc_ubi_mtd_dev`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/ubi/tc_lx_ubi_detach.py


.. _src_tc_linux_ubi_tc_lx_ubi_format_py:

src/tc/linux/ubi/tc_lx_ubi_format.py
....................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_ubi_format.py
  # ubiformat tb.config.tc_ubi_mtd_dev with tb.config.tc_lx_ubi_format_filename

used Testcases:

:ref:`src_tc_linux_ubi_tc_lx_ubi_format_py`.

used config variables:

:ref:`tb_config_tc_ubi_mtd_dev`.
:ref:`tb_config_tc_lx_ubi_format_filename`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/ubi/tc_lx_ubi_format.py


.. _src_tc_linux_ubi_tc_lx_ubi_info_py:

src/tc/linux/ubi/tc_lx_ubi_info.py
..................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_ubi_info.py
  # ubinfo tb.config.tc_ubi_ubi_dev

used Testcases:

:ref:`src_tc_linux_ubi_tc_lx_ubi_info_py`.

used config variables:

:ref:`tb_config_tc_ubi_ubi_dev`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/ubi/tc_lx_ubi_info.py


.. _src_tc_linux_ubi_tc_lx_ubi_tests_py:

src/tc/linux/ubi/tc_lx_ubi_tests.py
...................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_ubi_tests.py
  # - install mtd utils if needed with tc_lx_mtdutils_install.py
  # - attach ubi device with tc_lx_ubi_attach.py
  # - get info with tc_lx_ubi_info.py
  # - get parameters with tc_lx_get_ubi_parameters.py

used Testcases:

:ref:`src_tc_linux_ubi_tc_lx_ubi_tests_py`.
:ref:`src_tc_linux_tc_lx_mtdutils_install_py`.
:ref:`src_tc_linux_ubi_tc_lx_ubi_attach_py`.
:ref:`src_tc_linux_ubi_tc_lx_ubi_info_py`.
:ref:`src_tc_linux_tc_lx_get_ubi_parameters_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/ubi/tc_lx_ubi_tests.py


.. _src_tc_linux_tc_lx_bonnie_py:

src/tc/linux/tc_lx_bonnie.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_bonnie.py
  # run a bonnie test, if timer tc_workfd_check_tc_time.py timed out
  # - try to install bonnie if not is installed tc_lx_bonnie_install.py
  # - start bonnie on device tb.config.tc_lx_bonnie_dev with
  #   size tb.config.tc_lx_bonnie_sz

used Testcases:

:ref:`src_tc_linux_tc_lx_bonnie_py`.
:ref:`src_tc_linux_tc_workfd_check_tc_time_py`.
:ref:`src_tc_linux_tc_lx_bonnie_install_py`.

used config variables:

:ref:`tb_config_tc_lx_bonnie_dev`.
:ref:`tb_config_tc_lx_bonnie_sz`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_bonnie.py


.. _src_tc_linux_tc_lx_bonnie_install_py:

src/tc/linux/tc_lx_bonnie_install.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_bonnie_install.py
  # get bonnie source and install it

used Testcases:

:ref:`src_tc_linux_tc_lx_bonnie_install_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_bonnie_install.py


.. _src_tc_linux_tc_lx_check_devmem2_py:

src/tc/linux/tc_lx_check_devmem2.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_check_devmem2.py
  # simply check, if we have the devmem2 cmd
  # if not, try to find it

used Testcases:

:ref:`src_tc_linux_tc_lx_check_devmem2_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_check_devmem2.py


.. _src_tc_linux_tc_lx_check_reg_file_py:

src/tc/linux/tc_lx_check_reg_file.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_check_reg_file.py
  # checks if the default values in reg file tb.config.tc_lx_create_reg_file_name
  # on the tbot host in tb.workdir have the same values, as the
  # registers on the board. Needs devmem2 installed.
  # format of the regfile:
  # regaddr mask type defval
  #
  # If you have to call devmem2 with a "header"
  # set it through tb.config.devmem2_pre
  # so on the bbb with original rootfs -> no devmem2 installed
  # so to use tc which use devmem2 you have to copy devmem2
  # bin to the rootfs, and start it with 'sudo ...'
  #
  # ToDo: use the file from the lab host, not the tbot host

used Testcases:

:ref:`src_tc_linux_tc_lx_check_reg_file_py`.

used config variables:

:ref:`tb_config_tc_lx_create_reg_file_name`.
:ref:`tb_workdir`.
:ref:`tb_config_devmem2_pre`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_check_reg_file.py


.. _src_tc_linux_tc_lx_check_usb_authorized_py:

src/tc/linux/tc_lx_check_usb_authorized.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_check_usb_authorized.py
  # check if usb device tb.config.tc_lx_check_usb_authorized needs authorizing

used Testcases:

:ref:`src_tc_linux_tc_lx_check_usb_authorized_py`.

used config variables:

:ref:`tb_config_tc_lx_check_usb_authorized`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_check_usb_authorized.py


.. _src_tc_linux_tc_lx_cpufreq_py:

src/tc/linux/tc_lx_cpufreq.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_cpufreq.py
  # check if frequencies in tb.config.tc_lx_cpufreq_frequences
  # are possible to set with cpufreq-info

used Testcases:

:ref:`src_tc_linux_tc_lx_cpufreq_py`.

used config variables:

:ref:`tb_config_tc_lx_cpufreq_frequences`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_cpufreq.py


.. _src_tc_linux_tc_lx_create_dummy_file_py:

src/tc/linux/tc_lx_create_dummy_file.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_create_dummy_file.py
  # create a random dummy file tb.tc_lx_dummy_file_tempfile in linux
  # on tb.c_con with bs = tb.tc_lx_dummy_file_bs and
  # count = tb.tc_lx_dummy_file_count

used Testcases:

:ref:`src_tc_linux_tc_lx_create_dummy_file_py`.

used config variables:

:ref:`tb_tc_lx_dummy_file_tempfile`.
:ref:`tb_c_con`.
:ref:`tb_tc_lx_dummy_file_bs`.
:ref:`tb_tc_lx_dummy_file_count`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_create_dummy_file.py


.. _src_tc_linux_tc_lx_create_reg_file_py:

src/tc/linux/tc_lx_create_reg_file.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_create_reg_file.py
  # creates a reg file tb.config.tc_lx_create_reg_file_name on the tbot host
  # in tb.workdir
  # read from tb.config.tc_lx_create_reg_file_start to tb.config.tc_lx_create_reg_file_stop
  # and writes the results in the regfile
  # format of the regfile:
  # regaddr mask type defval
  # This reg file can be used as a default file, how the
  # registers must be setup, check it with testcase
  # tc_lx_check_reg_file.py
  #
  # If you have to call devmem2 with a "header"
  # set it through tb.config.devmem2_pre
  # so on the bbb with original rootfs -> no devmem2 installed
  # so to use tc which use devmem2 you have to copy devmem2
  # bin to the rootfs, and start it with 'sudo ...'
  #
  # ToDo: use the file from the lab host, not the tbot host

used Testcases:

:ref:`src_tc_linux_tc_lx_create_reg_file_py`.
:ref:`src_tc_linux_tc_lx_check_reg_file_py`.

used config variables:

:ref:`tb_config_tc_lx_create_reg_file_name`.
:ref:`tb_workdir`.
:ref:`tb_config_tc_lx_create_reg_file_start`.
:ref:`tb_config_tc_lx_create_reg_file_stop`.
:ref:`tb_config_devmem2_pre`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_create_reg_file.py


.. _src_tc_linux_tc_lx_devmem2_install_py:

src/tc/linux/tc_lx_devmem2_install.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_devmem2_install.py
  # get devmem2 source from www.lartmaker.nl/lartware/port/devmem2.c
  # and install it

used Testcases:

:ref:`src_tc_linux_tc_lx_devmem2_install_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_devmem2_install.py


.. _src_tc_linux_tc_lx_dmesg_grep_py:

src/tc/linux/tc_lx_dmesg_grep.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_dmesg_grep.py
  # check if string tb.config.tc_lx_dmesg_grep_name is in dmesg output.

used Testcases:

:ref:`src_tc_linux_tc_lx_dmesg_grep_py`.

used config variables:

:ref:`tb_config_tc_lx_dmesg_grep_name`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_dmesg_grep.py


.. _src_tc_linux_tc_lx_eeprom_py:

src/tc/linux/tc_lx_eeprom.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_eeprom.py
  # Test an eeprom:
  # - read the content from eeprom @ tb.config.tc_lx_eeprom_tmp_dir
  #   with "cat" into tmpfile
  # - check tb.config.tc_lx_eeprom_wp_gpio != 'none'
  #   if WP pin works
  # - generate random file with tb.config.tc_lx_eeprom_wp_sz size
  # - write it into eeprom
  # - reread it
  # - compare it with original
  # - restore original eeprom content at end

used Testcases:

:ref:`src_tc_linux_tc_lx_eeprom_py`.

used config variables:

:ref:`tb_config_tc_lx_eeprom_tmp_dir`.
:ref:`tb_config_tc_lx_eeprom_wp_gpio`.
:ref:`tb_config_tc_lx_eeprom_wp_sz`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_eeprom.py


.. _src_tc_linux_tc_lx_get_ubi_parameters_py:

src/tc/linux/tc_lx_get_ubi_parameters.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_get_ubi_parameters.py
  # get ubi parameters of ubi device tb.config.tc_ubi_mtd_dev
  # save them into:
  # - tb.config.tc_ubi_max_leb_cnt
  # - tb.config.tc_ubi_min_io_size
  # - tb.config.tc_ubi_leb_size

used Testcases:

:ref:`src_tc_linux_tc_lx_get_ubi_parameters_py`.

used config variables:

:ref:`tb_config_tc_ubi_mtd_dev`.
:ref:`tb_config_tc_ubi_max_leb_cnt`.
:ref:`tb_config_tc_ubi_min_io_size`.
:ref:`tb_config_tc_ubi_leb_size`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_get_ubi_parameters.py


.. _src_tc_linux_tc_lx_get_version_py:

src/tc/linux/tc_lx_get_version.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_get_version.py
  # get the linux version and create event LINUX_VERSION
  # save the linux version in tb.config.tc_return

used Testcases:

:ref:`src_tc_linux_tc_lx_get_version_py`.

used config variables:

:ref:`tb_config_tc_return`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_get_version.py


.. _src_tc_linux_tc_lx_gpio_py:

src/tc/linux/tc_lx_gpio.py
,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_gpio.py
  # set in linux gpio tb.config.tc_lx_gpio_nr to direction tb.config.tc_lx_gpio_dir
  # and value tb.config.tc_lx_gpio_val

used Testcases:

:ref:`src_tc_linux_tc_lx_gpio_py`.

used config variables:

:ref:`tb_config_tc_lx_gpio_nr`.
:ref:`tb_config_tc_lx_gpio_dir`.
:ref:`tb_config_tc_lx_gpio_val`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_gpio.py


.. _src_tc_linux_tc_lx_mount_py:

src/tc/linux/tc_lx_mount.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_mount.py
  # mount device tb.config.tc_lx_mount_dev with fs type tb.config.tc_lx_mount_fs_type
  # to tb.config.tc_lx_mount_dir

used Testcases:

:ref:`src_tc_linux_tc_lx_mount_py`.

used config variables:

:ref:`tb_config_tc_lx_mount_dev`.
:ref:`tb_config_tc_lx_mount_fs_type`.
:ref:`tb_config_tc_lx_mount_dir`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_mount.py


.. _src_tc_linux_tc_lx_mtdutils_install_py:

src/tc/linux/tc_lx_mtdutils_install.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_mtdutils_install.py
  # check if mtdutils are installed. If not, clone the code with
  # git clone git://git.infradead.org/mtd-utils.git mtd-utils
  # and install it

used Testcases:

:ref:`src_tc_linux_tc_lx_mtdutils_install_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_mtdutils_install.py


.. _src_tc_linux_tc_lx_partition_check_py:

src/tc/linux/tc_lx_partition_check.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_partition_check.py
  # cp a dummy file into a partiton umount/mount it and
  # compare it.
  # - Mount tb.config.tc_lx_mount_dir with tc_lx_mount.py

used Testcases:

:ref:`src_tc_linux_tc_lx_partition_check_py`.
:ref:`src_tc_linux_tc_lx_mount_py`.

used config variables:

:ref:`tb_config_tc_lx_mount_dir`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_partition_check.py


.. _src_tc_linux_tc_lx_printenv_py:

src/tc/linux/tc_lx_printenv.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_printenv.py
  # simple printenv linux command

used Testcases:

:ref:`src_tc_linux_tc_lx_printenv_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_printenv.py


.. _src_tc_linux_tc_lx_regulator_py:

src/tc/linux/tc_lx_regulator.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_regulator.py
  # check if regulators in tb.config.tc_lx_regulator_nrs exist, and have
  # the correct microvolts settings.

used Testcases:

:ref:`src_tc_linux_tc_lx_regulator_py`.

used config variables:

:ref:`tb_config_tc_lx_regulator_nrs`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_regulator.py


.. _src_tc_linux_tc_lx_trigger_wdt_py:

src/tc/linux/tc_lx_trigger_wdt.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_trigger_wdt.py
  # simple trigger wdt with command tb.config.tc_lx_trigger_wdt_cmd

used Testcases:

:ref:`src_tc_linux_tc_lx_trigger_wdt_py`.

used config variables:

:ref:`tb_config_tc_lx_trigger_wdt_cmd`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_trigger_wdt.py


.. _src_tc_linux_tc_lx_uname_py:

src/tc/linux/tc_lx_uname.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_uname.py
  # simple linux "uname -a" command

used Testcases:

:ref:`src_tc_linux_tc_lx_uname_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_lx_uname.py


.. _src_tc_linux_tc_workfd_apply_local_patches_py:

src/tc/linux/tc_workfd_apply_local_patches.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_apply_local_patches.py
  # apply patches from directory tb.config.tc_workfd_apply_local_patches_dir
  # with 'git am -3' to the source in current directory.
  # if tb.config.tc_workfd_apply_local_patches_checkpatch_cmd != 'none'
  # check the patches with the checkpatch cmd tb.config.tc_workfd_apply_local_patches_checkpatch_cmd
  # before applying.

used Testcases:

:ref:`src_tc_linux_tc_workfd_apply_local_patches_py`.

used config variables:

:ref:`tb_config_tc_workfd_apply_local_patches_dir`.
:ref:`tb_config_tc_workfd_apply_local_patches_checkpatch_cmd`.
:ref:`tb_config_tc_workfd_apply_local_patches_checkpatch_cmd`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_apply_local_patches.py


.. _src_tc_linux_tc_workfd_apply_patchwork_patches_py:

src/tc/linux/tc_workfd_apply_patchwork_patches.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_apply_patchwork_patches.py
  # apply patchworkpatches from list:
  # tb.config.tc_workfd_apply_patchwork_patches_list:
  # to source in current directory.
  # creates event:
  # - PW_NR: which patchwork number used
  # - PW_CLEAN: is it checkpatch clean
  # - PW_AA: already applied
  # - PW_APPLY: apply it clean to source

used Testcases:

:ref:`src_tc_linux_tc_workfd_apply_patchwork_patches_py`.

used config variables:

:ref:`tb_config_tc_workfd_apply_patchwork_patches_list:`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_apply_patchwork_patches.py


.. _src_tc_linux_tc_workfd_can_py:

src/tc/linux/tc_workfd_can.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_can.py
  #
  # minimal can test:
  # starts a new connection named tb_canm. This connection runs
  # on board/PC which has a can conncetion to the board tbot
  # tests, named CAN PC.
  # If necessary (tb.config.tc_workfd_can_ssh != 'no'), tc connects first
  # to ssh (if the CAN PC is not the lab PC). Also if necessary
  # (tb.config.tc_workfd_can_su != 'no', switch to superuser on the CAN PC.
  #
  # Set on the CAN PC, with the "ip" command the bitrate
  # tb.config.tc_workfd_can_bitrate for the can device tb.config.tc_workfd_can_dev
  # and activate the interface.
  #
  # Now on the board, go into tb.config.tc_workfd_can_iproute_dir
  # (which contains the "ip" command ...
  # Set the bitrate with it and activate the can interface.
  # Goto into tb.config.tc_workfd_can_util_dir which contains canutils
  # Send '123#DEADBEEF' with cansend
  #
  # check if the CAN PC gets this string.
  # End True if this is the case, False else
  #
  # ToDo:
  # - get rid of tb.config.tc_workfd_can_iproute_dir and tb.config.tc_workfd_can_util_dir
  #   (add the commands to rootfs ...)
  # - support different can devices on the CAN PC and board

used Testcases:

:ref:`src_tc_linux_tc_workfd_can_py`.

used config variables:

:ref:`tb_config_tc_workfd_can_bitrate`.
:ref:`tb_config_tc_workfd_can_dev`.
:ref:`tb_config_tc_workfd_can_iproute_dir`.
:ref:`tb_config_tc_workfd_can_util_dir`.
:ref:`tb_config_tc_workfd_can_iproute_dir`.
:ref:`tb_config_tc_workfd_can_util_dir`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_can.py


.. _src_tc_linux_tc_workfd_cd_to_dir_py:

src/tc/linux/tc_workfd_cd_to_dir.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_cd_to_dir.py
  # simple cd into directory tb.config.tc_workfd_cd_name

used Testcases:

:ref:`src_tc_linux_tc_workfd_cd_to_dir_py`.

used config variables:

:ref:`tb_config_tc_workfd_cd_name`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_cd_to_dir.py


.. _src_tc_linux_tc_workfd_check_cmd_success_py:

src/tc/linux/tc_workfd_check_cmd_success.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_check_cmd_success.py
  # simple check if previous shell command was succesful

used Testcases:

:ref:`src_tc_linux_tc_workfd_check_cmd_success_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_check_cmd_success.py


.. _src_tc_linux_tc_workfd_check_if_cmd_exist_py:

src/tc/linux/tc_workfd_check_if_cmd_exist.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_check_if_cmd_exist.py
  # check if a command exists

used Testcases:

:ref:`src_tc_linux_tc_workfd_check_if_cmd_exist_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_check_if_cmd_exist.py


.. _src_tc_linux_tc_workfd_check_if_device_exist_py:

src/tc/linux/tc_workfd_check_if_device_exist.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_check_if_device_exist.py
  # check if a device tb.config.tc_workfd_check_if_device_exists_name exist
  # this tc returns always true, but sets
  # tb.config.tc_return True or False, because we may not
  # want to end testcase failed, if device not exists.

used Testcases:

:ref:`src_tc_linux_tc_workfd_check_if_device_exist_py`.

used config variables:

:ref:`tb_config_tc_workfd_check_if_device_exists_name`.
:ref:`tb_config_tc_return`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_check_if_device_exist.py


.. _src_tc_linux_tc_workfd_check_if_dir_exist_py:

src/tc/linux/tc_workfd_check_if_dir_exist.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_check_if_dir_exist.py
  # check if a dir in tbot workdir exist
  # this tc returns always true, but sets
  # tb.config.tc_return True or False, because we may not
  # want to end testcase failed, if dir not exists.

used Testcases:

:ref:`src_tc_linux_tc_workfd_check_if_dir_exist_py`.

used config variables:

:ref:`tb_config_tc_return`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_check_if_dir_exist.py


.. _src_tc_linux_tc_workfd_check_if_file_exist_py:

src/tc/linux/tc_workfd_check_if_file_exist.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_check_if_file_exist.py
  # check if a file in tbot workdir exist

used Testcases:

:ref:`src_tc_linux_tc_workfd_check_if_file_exist_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_check_if_file_exist.py


.. _src_tc_linux_tc_workfd_check_tar_content_py:

src/tc/linux/tc_workfd_check_tar_content.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_check_tar_content.py
  # check if the strings in the tb.config.tc_workfd_check_tar_content_elements
  # list are in the tar file tb.config.tc_workfd_check_tar_content_path
  #
  # tb.config.tc_workfd_check_tar_content_path path and file name
  # tb.config.tc_workfd_check_tar_content_elements list of elements in the tar file
  # tb.config.tc_workfd_check_tar_content_endtc_onerror end TC when element is not found

used Testcases:

:ref:`src_tc_linux_tc_workfd_check_tar_content_py`.

used config variables:

:ref:`tb_config_tc_workfd_check_tar_content_elements`.
:ref:`tb_config_tc_workfd_check_tar_content_path`.
:ref:`tb_config_tc_workfd_check_tar_content_path`.
:ref:`tb_config_tc_workfd_check_tar_content_elements`.
:ref:`tb_config_tc_workfd_check_tar_content_endtc_onerror`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_check_tar_content.py


.. _src_tc_linux_tc_workfd_check_tc_time_py:

src/tc/linux/tc_workfd_check_tc_time.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_check_tc_time.py
  # check if time for a special testcase is expired.
  # some testcases (like writting in a flash) are not good for
  # execute them every day, so give them a timeout. This testcase
  # checks, if the testcases is ready for a new run.
  # False means time is not expired
  # True means time is expired

used Testcases:

:ref:`src_tc_linux_tc_workfd_check_tc_time_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_check_tc_time.py


.. _src_tc_linux_tc_workfd_compile_linux_py:

src/tc/linux/tc_workfd_compile_linux.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_compile_linux.py
  # compile linux:
  # - set toolchain with tc_lab_set_toolchain.py
  # - if tb.config.tc_workfd_compile_linux_clean == 'yes'
  #   call "make mrproper"
  # - tb.config.tc_workfd_compile_linux_load_addr != 'no'
  #   add LOAD_ADDR=tb.config.tc_workfd_compile_linux_load_addr to make
  # - make tb.config.tc_workfd_compile_linux_boardname defconfig
  # - make tb.config.tc_workfd_compile_linux_makeoptions tb.config.tc_workfd_compile_linux_make_target
  # - if tb.config.tc_workfd_compile_linux_modules != 'none'
  #   compile modules
  # - if tb.config.tc_workfd_compile_linux_dt_name != 'none'
  #   compile DTB from list tb.config.tc_workfd_compile_linux_dt_name
  # - if tb.config.tc_workfd_compile_linux_fit_its_file != 'no'
  #   create FIT image
  #   mkimage path: tb.config.tc_workfd_compile_linux_mkimage
  #   fit description file: tb.config.tc_workfd_compile_linux_fit_its_file
  #   tb.config.tc_workfd_compile_linux_fit_file
  # - if tb.config.tc_workfd_compile_linux_append_dt != 'no'
  #   append dtb to kernel image
  # tb.config.tc_workfd_compile_linux_boardname _defconfig

used Testcases:

:ref:`src_tc_linux_tc_workfd_compile_linux_py`.
:ref:`src_tc_tc_lab_set_toolchain_py`.

used config variables:

:ref:`tb_config_tc_workfd_compile_linux_clean`.
:ref:`tb_config_tc_workfd_compile_linux_load_addr`.
:ref:`tb_config_tc_workfd_compile_linux_boardname`.
:ref:`tb_config_tc_workfd_compile_linux_makeoptions`.
:ref:`tb_config_tc_workfd_compile_linux_make_target`.
:ref:`tb_config_tc_workfd_compile_linux_modules`.
:ref:`tb_config_tc_workfd_compile_linux_dt_name`.
:ref:`tb_config_tc_workfd_compile_linux_dt_name`.
:ref:`tb_config_tc_workfd_compile_linux_fit_its_file`.
:ref:`tb_config_tc_workfd_compile_linux_mkimage`.
:ref:`tb_config_tc_workfd_compile_linux_fit_its_file`.
:ref:`tb_config_tc_workfd_compile_linux_fit_file`.
:ref:`tb_config_tc_workfd_compile_linux_append_dt`.
:ref:`tb_config_tc_workfd_compile_linux_boardname`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_compile_linux.py


.. _src_tc_linux_tc_workfd_connect_with_conmux_py:

src/tc/linux/tc_workfd_connect_with_conmux.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_connect_with_conmux.py
  # connect to console with conmux
  # Never tested !!!

used Testcases:

:ref:`src_tc_linux_tc_workfd_connect_with_conmux_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_connect_with_conmux.py


.. _src_tc_linux_tc_workfd_connect_with_kermit_py:

src/tc/linux/tc_workfd_connect_with_kermit.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_connect_with_kermit.py
  # connect with kermit to serials board console
  # - if tb.config.tc_workfd_connect_with_kermit_ssh != 'none'
  #   connect first with ssh to another PC (where kermit is started)
  # - start kermit
  # - if tb.config.tc_workfd_connect_with_kermit_rlogin == 'none'
  #   connect with command in tb.config.tc_workfd_connect_with_kermit_rlogin
  #   else
  #   set line tb.config.kermit_line and speed tb.config.kermit_speed and
  #   connect to serial line.
  # - if you need sudo rights set tb.config.tc_workfd_connect_with_kermit_sudo = 'yes'
  #   and a sudo is preceded to kermit.
  #   the sudo password is searched with
  #   user:  tb.config.user + '_kermit'
  #   board: tb.config.boardname
  #

used Testcases:

:ref:`src_tc_linux_tc_workfd_connect_with_kermit_py`.

used config variables:

:ref:`tb_config_tc_workfd_connect_with_kermit_ssh`.
:ref:`tb_config_tc_workfd_connect_with_kermit_rlogin`.
:ref:`tb_config_tc_workfd_connect_with_kermit_rlogin`.
:ref:`tb_config_kermit_line`.
:ref:`tb_config_kermit_speed`.
:ref:`tb_config_tc_workfd_connect_with_kermit_sudo`.
:ref:`tb_config_user`.
:ref:`tb_config_boardname`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_connect_with_kermit.py


.. _src_tc_linux_tc_workfd_cp_file_py:

src/tc/linux/tc_workfd_cp_file.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_cp_file.py
  # simple copy file from tb.tc_workfd_cp_file_a to tb.tc_workfd_cp_file_b

used Testcases:

:ref:`src_tc_linux_tc_workfd_cp_file_py`.

used config variables:

:ref:`tb_tc_workfd_cp_file_a`.
:ref:`tb_tc_workfd_cp_file_b`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_cp_file.py


.. _src_tc_linux_tc_workfd_create_ubi_rootfs_py:

src/tc/linux/tc_workfd_create_ubi_rootfs.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_create_ubi_rootfs.py
  # create a ubifs rootfs
  # ubi rootfs path: tb.config.tc_workfd_create_ubi_rootfs_path
  # ubi parameters:
  # tb.config.tc_ubi_min_io_size tb.config.tc_ubi_leb_size tb.config.tc_ubi_max_leb_cnt
  # output path: tb.config.tc_workfd_create_ubi_rootfs_target

used Testcases:

:ref:`src_tc_linux_tc_workfd_create_ubi_rootfs_py`.

used config variables:

:ref:`tb_config_tc_workfd_create_ubi_rootfs_path`.
:ref:`tb_config_tc_ubi_min_io_size`.
:ref:`tb_config_tc_ubi_leb_size`.
:ref:`tb_config_tc_ubi_max_leb_cnt`.
:ref:`tb_config_tc_workfd_create_ubi_rootfs_target`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_create_ubi_rootfs.py


.. _src_tc_linux_tc_workfd_disconnect_with_kermit_py:

src/tc/linux/tc_workfd_disconnect_with_kermit.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_connect_with_kermit.py
  # disconnect from a kermit connection

used Testcases:

:ref:`src_tc_linux_tc_workfd_connect_with_kermit_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_disconnect_with_kermit.py


.. _src_tc_linux_tc_workfd_generate_random_file_py:

src/tc/linux/tc_workfd_generate_random_file.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_generate_random_file.py
  # simple create a random file tb.tc_workfd_generate_random_file_name
  # with tb.tc_workfd_generate_random_file_length length.

used Testcases:

:ref:`src_tc_linux_tc_workfd_generate_random_file_py`.

used config variables:

:ref:`tb_tc_workfd_generate_random_file_name`.
:ref:`tb_tc_workfd_generate_random_file_length`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_generate_random_file.py


.. _src_tc_linux_tc_workfd_get_linux_source_py:

src/tc/linux/tc_workfd_get_linux_source.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_get_linux_source.py
  # get Linux source tb.config.tc_lab_get_linux_source_git_repo with "git clone"
  # and go into the source tree. Apply patches if needed with:
  # tc_lab_apply_patches.py and tc_workfd_apply_local_patches.py

used Testcases:

:ref:`src_tc_linux_tc_workfd_get_linux_source_py`.
:ref:`src_tc_tc_lab_apply_patches_py`.
:ref:`src_tc_linux_tc_workfd_apply_local_patches_py`.

used config variables:

:ref:`tb_config_tc_lab_get_linux_source_git_repo`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_get_linux_source.py


.. _src_tc_linux_tc_workfd_get_list_of_files_in_dir_py:

src/tc/linux/tc_workfd_get_list_of_files_in_dir.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_get_list_of_files_in_dir.py
  # get a list of files from directory tb.tc_workfd_get_list_of_files_dir
  # tb.config.tc_workfd_get_list_of_files_mask

used Testcases:

:ref:`src_tc_linux_tc_workfd_get_list_of_files_in_dir_py`.

used config variables:

:ref:`tb_tc_workfd_get_list_of_files_dir`.
:ref:`tb_config_tc_workfd_get_list_of_files_mask`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_get_list_of_files_in_dir.py


.. _src_tc_linux_tc_workfd_get_patchwork_number_list_py:

src/tc/linux/tc_workfd_get_patchwork_number_list.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_get_patchwork_number_list.py
  # get a list of patchworknumbers
  # which are delegated to specific user
  # tb.config.workfd_get_patchwork_number_user
  # currently, this testcase reads "http://patchwork.ozlabs.org/project/uboot/list/"
  # and filters out the patches, which are for
  # tb.config.workfd_get_patchwork_number_user
  # It would be better to login and look for the users
  # ToDo list, but I did not find out, how to login ...
  # ignore patches on blacklist:
  # tb.config.tc_workfd_apply_patchwork_patches_blacklist
  # also you can set the patch order with:
  # tb.config.tc_workfd_get_patchwork_number_list_order

used Testcases:

:ref:`src_tc_linux_tc_workfd_get_patchwork_number_list_py`.

used config variables:

:ref:`tb_config_workfd_get_patchwork_number_user`.
:ref:`tb_config_workfd_get_patchwork_number_user`.
:ref:`tb_config_tc_workfd_apply_patchwork_patches_blacklist`.
:ref:`tb_config_tc_workfd_get_patchwork_number_list_order`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_get_patchwork_number_list.py


.. _src_tc_linux_tc_workfd_get_uboot_config_hex_py:

src/tc/linux/tc_workfd_get_uboot_config_hex.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_get_uboot_config_hex.py
  # get a hex parameter from U-Boot configuration
  # Input:
  # tb.config.uboot_get_parameter_file_list: list of files, where TC searches
  #   for the define
  # tb.uboot_config_option: config option which get searched
  #
  # return value:
  # TC ends True, if hex value found, else False
  # tb.config_result: founded hex value, else 'undef'

used Testcases:

:ref:`src_tc_linux_tc_workfd_get_uboot_config_hex_py`.

used config variables:

:ref:`tb_config_uboot_get_parameter_file_list:`.
:ref:`tb_uboot_config_option:`.
:ref:`tb_config_result:`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_get_uboot_config_hex.py


.. _src_tc_linux_tc_workfd_get_uboot_config_string_py:

src/tc/linux/tc_workfd_get_uboot_config_string.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_get_uboot_config_string.py
  # get a string parameter from U-Boot configuration
  # Input:
  # tb.config.uboot_get_parameter_file_list: list of files, where TC searches
  #   for the define
  # tb.uboot_config_option: config option which get searched
  #
  # return value:
  # TC ends True, if string value found, else False
  # tb.config_result: founded string value, else 'undef'

used Testcases:

:ref:`src_tc_linux_tc_workfd_get_uboot_config_string_py`.

used config variables:

:ref:`tb_config_uboot_get_parameter_file_list:`.
:ref:`tb_uboot_config_option:`.
:ref:`tb_config_result:`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_get_uboot_config_string.py


.. _src_tc_linux_tc_workfd_goto_lab_source_dir_py:

src/tc/linux/tc_workfd_goto_lab_source_dir.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_goto_lab_source_dir.py
  # switch into lab PC source directory tb.config.tc_lab_source_dir
  # set TBOT_BASEDIR to tb.config.tc_lab_source_dir

used Testcases:

:ref:`src_tc_linux_tc_workfd_goto_lab_source_dir_py`.

used config variables:

:ref:`tb_config_tc_lab_source_dir`.
:ref:`tb_config_tc_lab_source_dir`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_goto_lab_source_dir.py


.. _src_tc_linux_tc_workfd_goto_linux_code_py:

src/tc/linux/tc_workfd_goto_linux_code.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_goto_linux_code.py
  # switch into linux source tb.config.tc_lab_source_dir + "/linux-" + tb.config.boardlabname
  # set tb.config.linux_name to "linux-" + tb.config.boardlabname
  # and tb.config.linux_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.linux_name
  # and set $TBOT_BASEDIR_LINUX to tb.config.linux_fulldir_name

used Testcases:

:ref:`src_tc_linux_tc_workfd_goto_linux_code_py`.

used config variables:

:ref:`tb_config_tc_lab_source_dir`.
:ref:`tb_config_boardlabname`.
:ref:`tb_config_linux_name`.
:ref:`tb_config_boardlabname`.
:ref:`tb_config_linux_fulldir_name`.
:ref:`tb_config_tc_lab_source_dir`.
:ref:`tb_config_linux_name`.
:ref:`tb_config_linux_fulldir_name`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_goto_linux_code.py


.. _src_tc_linux_tc_workfd_goto_tbot_workdir_py:

src/tc/linux/tc_workfd_goto_tbot_workdir.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_goto_tbot_workdir.py
  # go into the tbot work dir tb.config.tc_workfd_work_dir
  # if not exist, create it

used Testcases:

:ref:`src_tc_linux_tc_workfd_goto_tbot_workdir_py`.

used config variables:

:ref:`tb_config_tc_workfd_work_dir`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_goto_tbot_workdir.py


.. _src_tc_linux_tc_workfd_goto_uboot_code_py:

src/tc/linux/tc_workfd_goto_uboot_code.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_goto_uboot_code.py
  # switch into U-Boot source tb.config.tc_lab_source_dir + "/u-boot-" + tb.config.boardlabname
  # set tb.config.uboot_name to "u-boot-" + tb.config.boardlabname
  # and tb.config.uboot_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.uboot_name
  # and set $TBOT_BASEDIR_UBOOT to tb.config.uboot_fulldir_name
  #

used Testcases:

:ref:`src_tc_linux_tc_workfd_goto_uboot_code_py`.

used config variables:

:ref:`tb_config_tc_lab_source_dir`.
:ref:`tb_config_boardlabname`.
:ref:`tb_config_uboot_name`.
:ref:`tb_config_boardlabname`.
:ref:`tb_config_uboot_fulldir_name`.
:ref:`tb_config_tc_lab_source_dir`.
:ref:`tb_config_uboot_name`.
:ref:`tb_config_uboot_fulldir_name`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_goto_uboot_code.py


.. _src_tc_linux_tc_workfd_grep_py:

src/tc/linux/tc_workfd_grep.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_grep.py
  # search string tb.tc_workfd_grep_string in file tb.tc_workfd_grep_file

used Testcases:

:ref:`src_tc_linux_tc_workfd_grep_py`.

used config variables:

:ref:`tb_tc_workfd_grep_string`.
:ref:`tb_tc_workfd_grep_file`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_grep.py


.. _src_tc_linux_tc_workfd_hdparm_py:

src/tc/linux/tc_workfd_hdparm.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_hdparm.py
  # make a minimal hdparm check
  # call hdparm -t tb.config.tc_workfd_hdparm_dev
  # and check if read speed is greater than tb.config.tc_workfd_hdparm_min
  # It is possible to add a PATH tb.config.tc_workfd_hdparm_path
  # where hdparm is installed
  # Testcase fails if readen speed is <= tb.config.tc_workfd_hdparm_min

used Testcases:

:ref:`src_tc_linux_tc_workfd_hdparm_py`.

used config variables:

:ref:`tb_config_tc_workfd_hdparm_dev`.
:ref:`tb_config_tc_workfd_hdparm_min`.
:ref:`tb_config_tc_workfd_hdparm_path`.
:ref:`tb_config_tc_workfd_hdparm_min`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_hdparm.py


.. _src_tc_linux_tc_workfd_insmod_py:

src/tc/linux/tc_workfd_insmod.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_insmod.py
  # insmod module tb.tc_workfd_insmod_module with
  # module path tb.tc_workfd_insmod_mpath and
  # tb.tc_workfd_insmod_module_path
  # check if the strings in list tb.tc_workfd_insmod_module_checks
  # come back when inserting the module.

used Testcases:

:ref:`src_tc_linux_tc_workfd_insmod_py`.

used config variables:

:ref:`tb_tc_workfd_insmod_module`.
:ref:`tb_tc_workfd_insmod_mpath`.
:ref:`tb_tc_workfd_insmod_module_path`.
:ref:`tb_tc_workfd_insmod_module_checks`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_insmod.py


.. _src_tc_linux_tc_workfd_iperf_py:

src/tc/linux/tc_workfd_iperf.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_iperf.py
  # make a minimal iperf check
  # starts an iperf server on tb.tc_workfd_c_sr connection
  #   with ip addr tb.tc_workfd_iperf_sip
  # starts an iperf "slave" on tb.tc_workfd_c_sl
  # waiting for the first result of iperf measure and
  # check if the resulting speed is bigger then
  # tb.tc_workfd_iperf_minval

used Testcases:

:ref:`src_tc_linux_tc_workfd_iperf_py`.

used config variables:

:ref:`tb_tc_workfd_c_sr`.
:ref:`tb_tc_workfd_iperf_sip`.
:ref:`tb_tc_workfd_c_sl`.
:ref:`tb_tc_workfd_iperf_minval`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_iperf.py


.. _src_tc_linux_tc_workfd_linux_get_ifconfig_py:

src/tc/linux/tc_workfd_linux_get_ifconfig.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c cuby -t tc_workfd_linux_get_ifconfig.py
  # read from tb.config.linux_get_ifconfig_dev the current
  # ip addr and save it in tb.config.linux_get_ifconfig_ip
  # broadcast and save it in tb.config.linux_get_ifconfig_broadcast
  # mask and save it in tb.config.linux_get_ifconfig_mask

used Testcases:

:ref:`src_tc_linux_tc_workfd_linux_get_ifconfig_py`.

used config variables:

:ref:`tb_config_linux_get_ifconfig_dev`.
:ref:`tb_config_linux_get_ifconfig_ip`.
:ref:`tb_config_linux_get_ifconfig_broadcast`.
:ref:`tb_config_linux_get_ifconfig_mask`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_linux_get_ifconfig.py


.. _src_tc_linux_tc_workfd_linux_get_uboot_env_py:

src/tc/linux/tc_workfd_linux_get_uboot_env.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c cuby -t tc_workfd_linux_get_uboot_env.py
  # read U-Boot Environment variable from tb.config.linux_get_uboot_env_name
  # from linux with fw_printenv, and save the value in tb.config.linux_get_uboot_env_value

used Testcases:

:ref:`src_tc_linux_tc_workfd_linux_get_uboot_env_py`.

used config variables:

:ref:`tb_config_linux_get_uboot_env_name`.
:ref:`tb_config_linux_get_uboot_env_value`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_linux_get_uboot_env.py


.. _src_tc_linux_tc_workfd_linux_mkdir_py:

src/tc/linux/tc_workfd_linux_mkdir.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_linux_mkdir.py
  # check if the directory tb.config.tc_workfd_linux_mkdir_dir exists.
  # if not, create it

used Testcases:

:ref:`src_tc_linux_tc_workfd_linux_mkdir_py`.

used config variables:

:ref:`tb_config_tc_workfd_linux_mkdir_dir`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_linux_mkdir.py


.. _src_tc_linux_tc_workfd_md5sum_py:

src/tc/linux/tc_workfd_md5sum.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_md5sum.py
  # calculate md5sum of file tb.tc_workfd_md5sum_name , and store it in
  # tb.tc_workfd_md5sum_sum

used Testcases:

:ref:`src_tc_linux_tc_workfd_md5sum_py`.

used config variables:

:ref:`tb_tc_workfd_md5sum_name`.
:ref:`tb_tc_workfd_md5sum_sum`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_md5sum.py


.. _src_tc_linux_tc_workfd_rm_file_py:

src/tc/linux/tc_workfd_rm_file.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_rm_file.py
  # simple rm directory tb.config.tc_workfd_rm_file_name on the lab

used Testcases:

:ref:`src_tc_linux_tc_workfd_rm_file_py`.

used config variables:

:ref:`tb_config_tc_workfd_rm_file_name`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_rm_file.py


.. _src_tc_linux_tc_workfd_rm_linux_code_py:

src/tc/linux/tc_workfd_rm_linux_code.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_rm_linux_code.py
  # rm linux source tb.config.tc_lab_source_dir + '/linux-' + tb.config.boardlabname

used Testcases:

:ref:`src_tc_linux_tc_workfd_rm_linux_code_py`.

used config variables:

:ref:`tb_config_tc_lab_source_dir`.
:ref:`tb_config_boardlabname`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_rm_linux_code.py


.. _src_tc_linux_tc_workfd_rm_uboot_code_py:

src/tc/linux/tc_workfd_rm_uboot_code.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_rm_uboot_code.py
  # rm U-Boot source tb.config.tc_lab_source_dir + '/u-boot-' + tb.config.boardlabname

used Testcases:

:ref:`src_tc_linux_tc_workfd_rm_uboot_code_py`.

used config variables:

:ref:`tb_config_tc_lab_source_dir`.
:ref:`tb_config_boardlabname`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_rm_uboot_code.py


.. _src_tc_linux_tc_workfd_scp_py:

src/tc/linux/tc_workfd_scp.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -s lab_denx -c exceet -t tc_workfd_scp.py
  #
  # start an scp transfer
  # tb.config.tc_workfd_scp_opt: scp options
  # tb.config.tc_workfd_scp_from: from where
  # tb.config.tc_workfd_scp_to
  #

used Testcases:

:ref:`src_tc_linux_tc_workfd_scp_py`.

used config variables:

:ref:`tb_config_tc_workfd_scp_opt:`.
:ref:`tb_config_tc_workfd_scp_from:`.
:ref:`tb_config_tc_workfd_scp_to`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_scp.py


.. _src_tc_linux_tc_workfd_ssh_py:

src/tc/linux/tc_workfd_ssh.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_ssh.py
  # login with ssh to tb.workfd_ssh_cmd and set new ssh prompt
  # tb.config.workfd_ssh_cmd_prompt

used Testcases:

:ref:`src_tc_linux_tc_workfd_ssh_py`.

used config variables:

:ref:`tb_workfd_ssh_cmd`.
:ref:`tb_config_workfd_ssh_cmd_prompt`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_ssh.py


.. _src_tc_linux_tc_workfd_sudo_cp_file_py:

src/tc/linux/tc_workfd_sudo_cp_file.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_sudo_cp_file.py
  # simple copy file from tb.tc_workfd_cp_file_a to tb.tc_workfd_cp_file_b
  # with sudo rights

used Testcases:

:ref:`src_tc_linux_tc_workfd_sudo_cp_file_py`.

used config variables:

:ref:`tb_tc_workfd_cp_file_a`.
:ref:`tb_tc_workfd_cp_file_b`.



https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_sudo_cp_file.py


.. _src_tc_linux_tc_workfd_switch_su_py:

src/tc/linux/tc_workfd_switch_su.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_switch_su.py
  # switch to superuser

used Testcases:

:ref:`src_tc_linux_tc_workfd_switch_su_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/linux/tc_workfd_switch_su.py


src/tc/uboot
------------


src/tc/uboot/duts
,,,,,,,,,,,,,,,,,


.. _src_tc_uboot_duts_tc_ub_basic_py:

src/tc/uboot/duts/tc_ub_basic.py
................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_basic.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/02_UBootBasic.tc;h=5503cc6c716d2748732d30d63b0801e651fe1706;hb=101ddd5dbd547d5046363358d560149d873b238a

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_basic_py`.


links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/02_UBootBasic.tc;h=5503cc6c716d2748732d30d63b0801e651fe1706;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_basic.py


.. _src_tc_uboot_duts_tc_ub_bdinfo_py:

src/tc/uboot/duts/tc_ub_bdinfo.py
.................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_bdinfo.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootBdinfo.tc;h=aa794a93ac5c8d2c3aea4aa5d02433ca2ee0f010;hb=101ddd5dbd547d5046363358d560149d873b238a

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_bdinfo_py`.


links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootBdinfo.tc;h=aa794a93ac5c8d2c3aea4aa5d02433ca2ee0f010;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_bdinfo.py


.. _src_tc_uboot_duts_tc_ub_boot_py:

src/tc/uboot/duts/tc_ub_boot.py
...............................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_boot.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootBoot.tc;h=f679ff09cdb1e1393829c32dc5aa5cf299e9af07;hb=101ddd5dbd547d5046363358d560149d873b238a

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_boot_py`.


links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootBoot.tc;h=f679ff09cdb1e1393829c32dc5aa5cf299e9af07;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_boot.py


.. _src_tc_uboot_duts_tc_ub_coninfo_py:

src/tc/uboot/duts/tc_ub_coninfo.py
..................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_coninfo.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootConinfo.tc;h=2d028f74ba791343b8a70a97885eabe8b5944017;hb=101ddd5dbd547d5046363358d560149d873b238a

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_coninfo_py`.


links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootConinfo.tc;h=2d028f74ba791343b8a70a97885eabe8b5944017;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_coninfo.py


.. _src_tc_uboot_duts_tc_ub_date_py:

src/tc/uboot/duts/tc_ub_date.py
...............................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_date.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootDate.tc;h=03b7d53fd93bd61381db4095a4bff58b1d1efff7;hb=101ddd5dbd547d5046363358d560149d873b238a

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_date_py`.


links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootDate.tc;h=03b7d53fd93bd61381db4095a4bff58b1d1efff7;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_date.py


.. _src_tc_uboot_duts_tc_ub_diskboothelp_py:

src/tc/uboot/duts/tc_ub_diskboothelp.py
.......................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_diskboothelp.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootIde.tc;h=03c2a05b75c6f9f6fc257fa84a2220f965567699;hb=101ddd5dbd547d5046363358d560149d873b238a

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_diskboothelp_py`.


links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootIde.tc;h=03c2a05b75c6f9f6fc257fa84a2220f965567699;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_diskboothelp.py


.. _src_tc_uboot_duts_tc_ub_download_py:

src/tc/uboot/duts/tc_ub_download.py
...................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_download.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootCmdGroupDownload.tc;h=8e58d53add90b680ef7a1300894d2392f90d9824;hb=101ddd5dbd547d5046363358d560149d873b238a

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_download_py`.


links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootCmdGroupDownload.tc;h=8e58d53add90b680ef7a1300894d2392f90d9824;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_download.py


.. _src_tc_uboot_duts_tc_ub_dtt_py:

src/tc/uboot/duts/tc_ub_dtt.py
..............................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_dtt.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootDtt.tc;h=e420c7b45cd73b00465d69f969039222868f4cc7;hb=101ddd5dbd547d5046363358d560149d873b238a

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_dtt_py`.


links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootDtt.tc;h=e420c7b45cd73b00465d69f969039222868f4cc7;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_dtt.py


.. _src_tc_uboot_duts_tc_ub_environment_py:

src/tc/uboot/duts/tc_ub_environment.py
......................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_environment.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootEnvironment.tc;h=18d235f427e3efe9e6a04f870a3c5426d719ec58;hb=101ddd5dbd547d5046363358d560149d873b238a

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_environment_py`.


links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootEnvironment.tc;h=18d235f427e3efe9e6a04f870a3c5426d719ec58;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_environment.py


.. _src_tc_uboot_duts_tc_ub_flash_py:

src/tc/uboot/duts/tc_ub_flash.py
................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_flash.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootFlashTest.tc;h=6eea72c8e9f3f4739a76ff59bb2e9a7c693aedd9;hb=101ddd5dbd547d5046363358d560149d873b238a

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_flash_py`.


links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootFlashTest.tc;h=6eea72c8e9f3f4739a76ff59bb2e9a7c693aedd9;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_flash.py


.. _src_tc_uboot_duts_tc_ub_flinfo_py:

src/tc/uboot/duts/tc_ub_flinfo.py
.................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_flinfo.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootFlinfo.tc;h=f5b728258250211d86dc9c6a9208639d8542b845;hb=101ddd5dbd547d5046363358d560149d873b238a

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_flinfo_py`.


links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootFlinfo.tc;h=f5b728258250211d86dc9c6a9208639d8542b845;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_flinfo.py


.. _src_tc_uboot_duts_tc_ub_i2c_help_py:

src/tc/uboot/duts/tc_ub_i2c_help.py
...................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_i2c_help.py
  # simple prints "help i2c" cmd

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_i2c_help_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_i2c_help.py


.. _src_tc_uboot_duts_tc_ub_ide_py:

src/tc/uboot/duts/tc_ub_ide.py
..............................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ide.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootIde.tc;h=03c2a05b75c6f9f6fc257fa84a2220f965567699;hb=101ddd5dbd547d5046363358d560149d873b238a

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_ide_py`.


links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/15_UBootIde.tc;h=03c2a05b75c6f9f6fc257fa84a2220f965567699;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_ide.py


.. _src_tc_uboot_duts_tc_ub_memory_py:

src/tc/uboot/duts/tc_ub_memory.py
.................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_memory.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootMemory.tc;h=f5fb055499db17c322859215ab489cefb063ac47;hb=101ddd5dbd547d5046363358d560149d873b238a
  #
  # disable "base" only command with
  # tb.config.tc_ub_memory_base = 'no'
  # default: 'yes'

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_memory_py`.

used config variables:

:ref:`tb_config_tc_ub_memory_base`.

links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootMemory.tc;h=f5fb055499db17c322859215ab489cefb063ac47;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_memory.py


.. _src_tc_uboot_duts_tc_ub_run_py:

src/tc/uboot/duts/tc_ub_run.py
..............................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_run.py
  # convert duts tests from:
  # http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootRun.tc;h=44f8a0a0de256afdd95b5ec20d1d4570373aeb7d;hb=101ddd5dbd547d5046363358d560149d873b238a

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_run_py`.


links:

http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootRun.tc;h=44f8a0a0de256afdd95b5ec20d1d4570373aeb7d;hb=101ddd5dbd547d5046363358d560149d873b238a



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_run.py


.. _src_tc_uboot_duts_tc_ub_start_all_duts_py:

src/tc/uboot/duts/tc_ub_start_all_duts.py
.........................................

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_start_all_duts.py
  # start all DUTS tests

used Testcases:

:ref:`src_tc_uboot_duts_tc_ub_start_all_duts_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/duts/tc_ub_start_all_duts.py


.. _src_tc_uboot_tc_ub_aristainetos2_ubi_py:

src/tc/uboot/tc_ub_aristainetos2_ubi.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c aristainetos2 -t tc_ub_aristainetos2_ubi.py
  # ubi testcases for the aristainetos2 board

used Testcases:

:ref:`src_tc_uboot_tc_ub_aristainetos2_ubi_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_aristainetos2_ubi.py


.. _src_tc_uboot_tc_ub_check_reg_file_py:

src/tc/uboot/tc_ub_check_reg_file.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_check_reg_file.py
  # checks if the default values in reg file tb.config.tc_ub_create_reg_file_name
  # on the tbot host in tb.workdir have the same values, as the
  # registers on the board
  # format of the regfile:
  # regaddr mask type defval
  # ToDo: use the file from the lab host, not the tbot host

used Testcases:

:ref:`src_tc_uboot_tc_ub_check_reg_file_py`.

used config variables:

:ref:`tb_config_tc_ub_create_reg_file_name`.
:ref:`tb_workdir`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_check_reg_file.py


.. _src_tc_uboot_tc_ub_check_version_py:

src/tc/uboot/tc_ub_check_version.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_check_version.py
  # check if the current running U-Boot vers == tb.uboot_vers
  # and SPL vers == tb.spl_vers

used Testcases:

:ref:`src_tc_uboot_tc_ub_check_version_py`.

used config variables:

:ref:`tb_uboot_vers`.
:ref:`tb_spl_vers`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_check_version.py


.. _src_tc_uboot_tc_ub_cmp_py:

src/tc/uboot/tc_ub_cmp.py
,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_cmp.py
  # - compare 2 the contents of tb.tc_ub_cmp_addr1 with tb.tc_ub_cmp_addr2
  # bytes tb.tc_ub_cmp_len length

used Testcases:

:ref:`src_tc_uboot_tc_ub_cmp_py`.

used config variables:

:ref:`tb_tc_ub_cmp_addr1`.
:ref:`tb_tc_ub_cmp_addr2`.
:ref:`tb_tc_ub_cmp_len`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_cmp.py


.. _src_tc_uboot_tc_ub_create_am335x_reg_file_py:

src/tc/uboot/tc_ub_create_am335x_reg_file.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -s lab_denx -c tbot.cfg -t tc_ub_create_am335x_reg_file.py
  #
  # creates U-Boot register dump files for an am335x based board.
  # using testcase tc_ub_create_reg_file.py
  #
  # dumps:
  # - pinmux  44e10000 - 44e10004
  # - pinmux  44e10010 - 44e10010 
  # - pinmux  44e10040 - 44e10040
  # - pinmux  44e10110 - 44e10110
  # - pinmux  44e10428 - 44e11440
  # - cm per  44e00000 - 44e00150
  # - cm wkup 44e00400 - 44e004d0
  # - cm dpll 44e00500 - 44e0053c
  # - cm mpu  44e00600 - 44e00604
  # - cm device 44e00700 - 44e00700
  # - emif    4c000000 - 4c000120
  # - ddr     44e12000 - 44e121dc
  #
  # into files found in src/files/
  # create for your board a subdir in the directory,
  # and move the new created files into it, so you have
  # them as a base for comparing further use.
  #

used Testcases:

:ref:`src_tc_uboot_tc_ub_create_am335x_reg_file_py`.
:ref:`src_tc_uboot_tc_ub_create_reg_file_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_create_am335x_reg_file.py


.. _src_tc_uboot_tc_ub_create_imx28_reg_file_py:

src/tc/uboot/tc_ub_create_imx28_reg_file.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -s lab_denx -c tbot.cfg -t tc_ub_create_imx28_reg_file.py
  #
  # creates U-Boot register dump files for an imx28 based board.
  # using testcase tc_ub_create_reg_file.py
  #
  # dumps:
  # - pinmux  80018000 - 80018b40
  # - clkctrl 80044000 - 80044170
  # - emi     800e0000 - 800e02ec
  # - gpmi    8000c000 - 8000c0d4
  # - enet 0  800f0000 - 800f0684
  # - enet 1  800f4000 - 800f4684
  #
  # into files found in src/files/
  # create for your board a subdir in the directory,
  # and move the new created files into it, so you have
  # them as a base for comparing further use.
  #

used Testcases:

:ref:`src_tc_uboot_tc_ub_create_imx28_reg_file_py`.
:ref:`src_tc_uboot_tc_ub_create_reg_file_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_create_imx28_reg_file.py


.. _src_tc_uboot_tc_ub_create_imx6_reg_file_py:

src/tc/uboot/tc_ub_create_imx6_reg_file.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -s lab_denx -c tbot.cfg -t tc_ub_create_imx6_reg_file.py
  #
  # creates U-Boot register dump files for an imx6 based board.
  # using testcase tc_ub_create_reg_file.py
  #
  # dumps:
  # - pinmux  20e0000 - 20e0950
  #
  # into files found in src/files/
  # create for your board a subdir in the directory,
  # and move the new created files into it, so you have
  # them as a base for comparing further use.
  #

used Testcases:

:ref:`src_tc_uboot_tc_ub_create_imx6_reg_file_py`.
:ref:`src_tc_uboot_tc_ub_create_reg_file_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_create_imx6_reg_file.py


.. _src_tc_uboot_tc_ub_create_reg_file_py:

src/tc/uboot/tc_ub_create_reg_file.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_create_reg_file.py
  # creates a reg file tb.tc_ub_create_reg_file_name on the tbot host
  # in tb.workdir
  # read from tb.tc_ub_create_reg_file_start to tb.tc_ub_create_reg_file_stop
  # and writes the results in the regfile tb.tc_ub_create_reg_file_name
  # format of the regfile:
  # regaddr mask type defval
  # This reg file can be used as a default file, how the
  # registers must be setup, check it with testcase
  # tc_ub_check_reg_file.py
  # ToDo: use the file from the lab host, not the tbot host

used Testcases:

:ref:`src_tc_uboot_tc_ub_create_reg_file_py`.
:ref:`src_tc_uboot_tc_ub_check_reg_file_py`.

used config variables:

:ref:`tb_tc_ub_create_reg_file_name`.
:ref:`tb_workdir`.
:ref:`tb_tc_ub_create_reg_file_start`.
:ref:`tb_tc_ub_create_reg_file_stop`.
:ref:`tb_tc_ub_create_reg_file_name`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_create_reg_file.py


.. _src_tc_uboot_tc_ub_dfu_py:

src/tc/uboot/tc_ub_dfu.py
,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_dfu.py
  # test dfu
  # - use dfu-util in tb.config.tc_ub_dfu_dfu_util_path
  # - upload file tb.config.tc_ub_dfu_dfu_util_alt_setting to
  #   tb.config.tc_ub_dfu_dfu_util_downloadfile
  # - download it back to the board
  # - upload it again
  # - and compare the two files

used Testcases:

:ref:`src_tc_uboot_tc_ub_dfu_py`.

used config variables:

:ref:`tb_config_tc_ub_dfu_dfu_util_path`.
:ref:`tb_config_tc_ub_dfu_dfu_util_alt_setting`.
:ref:`tb_config_tc_ub_dfu_dfu_util_downloadfile`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_dfu.py


.. _src_tc_uboot_tc_ub_dfu_random_py:

src/tc/uboot/tc_ub_dfu_random.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_dfu_random.py
  # test a U-Boot dfu alt setting tb.config.tc_ub_dfu_dfu_util_alt_setting
  # Therefore write a random file with size tb.config.tc_ub_dfu_rand_size
  # to it, reread it and compare it. TC fails if files differ
  # (If readen file is longer, this is no error!)
  #
  # If dfu-util is not installed on the lab PC, set
  # tb.config.tc_ub_dfu_dfu_util_ssh for connecting with ssh to a PC
  # which have it installed, and a USB cable connected to the board.
  # Set tb.config.tc_ub_dfu_dfu_util_path to the path of dfu-util, if
  # you have a self compiled version of it.
  # Set tb.config.tc_ub_dfu_rand_ubcmd for the executed command on
  # U-Boot shell for getting into DFU mode

used Testcases:

:ref:`src_tc_uboot_tc_ub_dfu_random_py`.

used config variables:

:ref:`tb_config_tc_ub_dfu_dfu_util_alt_setting`.
:ref:`tb_config_tc_ub_dfu_rand_size`.
:ref:`tb_config_tc_ub_dfu_dfu_util_ssh`.
:ref:`tb_config_tc_ub_dfu_dfu_util_path`.
:ref:`tb_config_tc_ub_dfu_rand_ubcmd`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_dfu_random.py


.. _src_tc_uboot_tc_ub_dfu_random_default_py:

src/tc/uboot/tc_ub_dfu_random_default.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_dfu_random_default.py
  # test a U-Boot dfu alt setting tb.config.tc_ub_dfu_dfu_util_alt_setting
  # with reading / writing different sizes

used Testcases:

:ref:`src_tc_uboot_tc_ub_dfu_random_default_py`.

used config variables:

:ref:`tb_config_tc_ub_dfu_dfu_util_alt_setting`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_dfu_random_default.py


.. _src_tc_uboot_tc_ub_get_filesize_py:

src/tc/uboot/tc_ub_get_filesize.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_get_filesize.py
  # simple get the content of U-Boot env variable filesize
  # and store it in tb.ub_filesize

used Testcases:

:ref:`src_tc_uboot_tc_ub_get_filesize_py`.

used config variables:

:ref:`tb_ub_filesize`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_get_filesize.py


.. _src_tc_uboot_tc_ub_get_version_py:

src/tc/uboot/tc_ub_get_version.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_get_version.py
  # get the U-Boot and/or SPL version from a binary
  # and save it in tb.uboot_vers or tb.spl_vers

used Testcases:

:ref:`src_tc_uboot_tc_ub_get_version_py`.

used config variables:

:ref:`tb_uboot_vers`.
:ref:`tb_spl_vers`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_get_version.py


.. _src_tc_uboot_tc_ub_help_py:

src/tc/uboot/tc_ub_help.py
,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_help.py
  # - test U-Boots help cmd
  #   may we add a list as parameter, so we can adapt it board
  #   specific.

used Testcases:

:ref:`src_tc_uboot_tc_ub_help_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_help.py


.. _src_tc_uboot_tc_ub_load_board_env_py:

src/tc/uboot/tc_ub_load_board_env.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_load_board_env.py
  #
  # task: load U-Boot Environment env.txt file with tftp for the
  # board tb.config.tftpboardname to the addr tb.config.ub_load_board_env_addr
  # from subdir tb.config.ub_load_board_env_subdir
  # and imports the the textfile with 'env import'
  #
  # options:
  # if tb.config.tc_ub_boot_linux_load_env == 'no' than TC does nothing
  #
  # if tb.config.tc_ub_boot_linux_load_env == 'set' or == 'setend'
  # than TC executes the cmds in list tb.config.ub_load_board_env_set
  #
  # if tb.config.tc_ub_boot_linux_load_env == 'setend' TC returns
  # after executing the commands with True
  #
  # else TC executes the steps described in 'task'
  #

used Testcases:

:ref:`src_tc_uboot_tc_ub_load_board_env_py`.

used config variables:

:ref:`tb_config_tftpboardname`.
:ref:`tb_config_ub_load_board_env_addr`.
:ref:`tb_config_ub_load_board_env_subdir`.
:ref:`tb_config_tc_ub_boot_linux_load_env`.
:ref:`tb_config_tc_ub_boot_linux_load_env`.
:ref:`tb_config_ub_load_board_env_set`.
:ref:`tb_config_tc_ub_boot_linux_load_env`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_load_board_env.py


.. _src_tc_uboot_tc_ub_reset_py:

src/tc/uboot/tc_ub_reset.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_reset.py
  # simple U-Boot reset command.

used Testcases:

:ref:`src_tc_uboot_tc_ub_reset_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_reset.py


.. _src_tc_uboot_tc_ub_setenv_py:

src/tc/uboot/tc_ub_setenv.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_setenv.py
  # set U-Boot Environmentvariable tb.config.setenv_name with value
  # tb.config.setenv_value

used Testcases:

:ref:`src_tc_uboot_tc_ub_setenv_py`.

used config variables:

:ref:`tb_config_setenv_name`.
:ref:`tb_config_setenv_value`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_setenv.py


.. _src_tc_uboot_tc_ub_setenv_fkt_py:

src/tc/uboot/tc_ub_setenv_fkt.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -s lab_denx -c beagleboneblack -t tc_ub_setenv_fkt.py
  # set U-Boot Environmentvariable tb.config.setenv_name with value
  # tb.config.setenv_value
  #
  # This is for demonstration how to use functions in tbot only.
  # So, this testcase sets 3 times the U-Boot Envvariable:
  # - The new way with importing the functions from testcase
  #   src/tc/uboot/tc_ub_testfkt.py
  # - The oldstyled way with calling the testcase tc_ub_testfkt.py
  #   with tb.eof_call_tc()
  # - The oldstyled way with calling the testcase tc_ub_testfkt.py
  #   with tb.call_tc() and getting the return value.

used Testcases:

:ref:`src_tc_uboot_tc_ub_setenv_fkt_py`.
:ref:`src_tc_uboot_tc_ub_testfkt_py`.
:ref:`src_tc_uboot_tc_ub_testfkt_py`.

used config variables:

:ref:`tb_config_setenv_name`.
:ref:`tb_config_setenv_value`.
:ref:`tb_eof_call_tc()`.
:ref:`tb_call_tc()`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_setenv_fkt.py


.. _src_tc_uboot_tc_ub_test_py_py:

src/tc/uboot/tc_ub_test_py.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_test_py.py
  # call test/py from u-boot source
  # - disconnect console
  # - call test/py
  # - connect back to console
  # test/py hookscript directory:
  # tb.config.tc_ub_test_py_hook_script_path
  #
  # you can disable this testcase with tb.config.tc_ub_test_py_start = 'no'

used Testcases:

:ref:`src_tc_uboot_tc_ub_test_py_py`.

used config variables:

:ref:`tb_config_tc_ub_test_py_hook_script_path`.
:ref:`tb_config_tc_ub_test_py_start`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_test_py.py


.. _src_tc_uboot_tc_ub_testfkt_py:

src/tc/uboot/tc_ub_testfkt.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_testfkt.py
  #
  # This testcase is for demonstration of using functions in
  # testcases, and use them from other testcases.
  #
  # testcase which calls this function for demo:
  # src/tc/uboot/tc_ub_setenv_fkt.py
  #
  # defines 2 functions:
  # - ub_setenv(tb, c, name, val)
  #   set Environment variable name with value val
  # - ub_checkenv(tb, c, name, val)
  #   checks, if U-Boot Environmentvariable name
  #   has the value val.
  #
  # there are 2 ways from calling this testcase directly
  # from the cmdline:
  #
  # - with arguments:
  #   tbot.py -s lab_denx -c beagleboneblack -t tc_ub_testfkt.py -a "Heiko Schochernew"
  #
  #      name = tb.arguments.split()[0]
  #      val = tb.arguments.split()[1]
  #
  # - without arguments:
  #   tbot.py -s lab_denx -c beagleboneblack -t tc_ub_testfkt.py
  #
  #   in this case 
  #      name = tb.config.setenv_name
  #      val = tb.config.setenv_value
  #

used Testcases:

:ref:`src_tc_uboot_tc_ub_testfkt_py`.
:ref:`src_tc_uboot_tc_ub_testfkt_py`.
:ref:`src_tc_uboot_tc_ub_testfkt_py`.

used config variables:

:ref:`tb_arguments_split()[0]`.
:ref:`tb_arguments_split()[1]`.
:ref:`tb_config_setenv_name`.
:ref:`tb_config_setenv_value`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_testfkt.py


.. _src_tc_uboot_tc_ub_tftp_file_py:

src/tc/uboot/tc_ub_tftp_file.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_tftp_file.py
  # load file tb.config.tc_ub_tftp_file_name to tb.config.tc_ub_tftp_file_addr
  # with tftp command in uboot

used Testcases:

:ref:`src_tc_uboot_tc_ub_tftp_file_py`.

used config variables:

:ref:`tb_config_tc_ub_tftp_file_name`.
:ref:`tb_config_tc_ub_tftp_file_addr`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_tftp_file.py


.. _src_tc_uboot_tc_ub_ubi_check_volume_py:

src/tc/uboot/tc_ub_ubi_check_volume.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubi_check_volume.py
  # - checks if ubi volume tb.config.tc_ub_ubi_load_name exists

used Testcases:

:ref:`src_tc_uboot_tc_ub_ubi_check_volume_py`.

used config variables:

:ref:`tb_config_tc_ub_ubi_load_name`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_ubi_check_volume.py


.. _src_tc_uboot_tc_ub_ubi_create_volume_py:

src/tc/uboot/tc_ub_ubi_create_volume.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubi_create_volume.py
  # - create ubi volume tb.config.tc_ub_ubi_create_vol_name with size
  # tb.config.tc_ub_ubi_create_vol_sz

used Testcases:

:ref:`src_tc_uboot_tc_ub_ubi_create_volume_py`.

used config variables:

:ref:`tb_config_tc_ub_ubi_create_vol_name`.
:ref:`tb_config_tc_ub_ubi_create_vol_sz`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_ubi_create_volume.py


.. _src_tc_uboot_tc_ub_ubi_erase_py:

src/tc/uboot/tc_ub_ubi_erase.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubi_erase.py
  # - erase an ubi device
  #   execute U-Boot Env tbot_ubi_erase

used Testcases:

:ref:`src_tc_uboot_tc_ub_ubi_erase_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_ubi_erase.py


.. _src_tc_uboot_tc_ub_ubi_info_py:

src/tc/uboot/tc_ub_ubi_info.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubi_info.py
  # - simple print ubi info

used Testcases:

:ref:`src_tc_uboot_tc_ub_ubi_info_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_ubi_info.py


.. _src_tc_uboot_tc_ub_ubi_prepare_py:

src/tc/uboot/tc_ub_ubi_prepare.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubi_prepare.py
  # - ubi prepare
  #   execute "ubi part" ith tb.config.tc_ub_ubi_prep_partname
  #   if tb.config.tc_ub_ubi_prep_offset != 'none'
  #   with offset tb.config.tc_ub_ubi_prep_offset

used Testcases:

:ref:`src_tc_uboot_tc_ub_ubi_prepare_py`.

used config variables:

:ref:`tb_config_tc_ub_ubi_prep_partname`.
:ref:`tb_config_tc_ub_ubi_prep_offset`.
:ref:`tb_config_tc_ub_ubi_prep_offset`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_ubi_prepare.py


.. _src_tc_uboot_tc_ub_ubi_read_py:

src/tc/uboot/tc_ub_ubi_read.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubi_read.py
  # - read ubi volume tb.config.tc_ub_ubi_prep_offset to tb.tc_ub_ubi_read_addr
  # with len tb.tc_ub_ubi_read_len

used Testcases:

:ref:`src_tc_uboot_tc_ub_ubi_read_py`.

used config variables:

:ref:`tb_config_tc_ub_ubi_prep_offset`.
:ref:`tb_tc_ub_ubi_read_addr`.
:ref:`tb_tc_ub_ubi_read_len`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_ubi_read.py


.. _src_tc_uboot_tc_ub_ubi_write_py:

src/tc/uboot/tc_ub_ubi_write.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubi_write.py
  # - write image @ tb.config.tc_ub_ubi_write_addr to ubi volume
  #   tb.config.tc_ub_ubi_write_vol_name with len tb.config.tc_ub_ubi_write_len

used Testcases:

:ref:`src_tc_uboot_tc_ub_ubi_write_py`.

used config variables:

:ref:`tb_config_tc_ub_ubi_write_addr`.
:ref:`tb_config_tc_ub_ubi_write_vol_name`.
:ref:`tb_config_tc_ub_ubi_write_len`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_ubi_write.py


.. _src_tc_uboot_tc_ub_ubifs_ls_py:

src/tc/uboot/tc_ub_ubifs_ls.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubifs_ls.py
  # - ls ubifs tb.config.tc_ub_ubifs_ls_dir

used Testcases:

:ref:`src_tc_uboot_tc_ub_ubifs_ls_py`.

used config variables:

:ref:`tb_config_tc_ub_ubifs_ls_dir`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_ubifs_ls.py


.. _src_tc_uboot_tc_ub_ubifs_mount_py:

src/tc/uboot/tc_ub_ubifs_mount.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_ubifs_mount.py
  # - mount ubifs tb.config.tc_ub_ubifs_volume_name

used Testcases:

:ref:`src_tc_uboot_tc_ub_ubifs_mount_py`.

used config variables:

:ref:`tb_config_tc_ub_ubifs_volume_name`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_ubifs_mount.py


.. _src_tc_uboot_tc_ub_upd_spl_py:

src/tc/uboot/tc_ub_upd_spl.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_upd_spl.py
  # update new spl to board
  # steps:
  # - load tbot u-boot env vars
  # - execute "run tbot_upd_spl"
  # - execute "run tbot_cmp_spl"
  # - reset board
  # - get u-boot

used Testcases:

:ref:`src_tc_uboot_tc_ub_upd_spl_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_upd_spl.py


.. _src_tc_uboot_tc_ub_upd_uboot_py:

src/tc/uboot/tc_ub_upd_uboot.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_upd_uboot.py
  # update new uboot to board
  # steps:
  # - load tbot u-boot env vars
  # - execute "run tbot_upd_uboot"
  # - execute "run tbot_cmp_uboot"
  # - reset board
  # - get u-boot

used Testcases:

:ref:`src_tc_uboot_tc_ub_upd_uboot_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_ub_upd_uboot.py


.. _src_tc_uboot_tc_uboot_check_kconfig_py:

src/tc/uboot/tc_uboot_check_kconfig.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -s lab_denx -c uboot_kconfig_check -t tc_uboot_check_kconfig.py
  #
  # check for all boards, if a patch changes the u-boot binary
  # If U-boot binary changed by the patch this testcase fails.
  # use this testcase, if you for example move a config option
  # into Kconfig. As we need reproducable builds, we need to
  # patch U-Boot with tb.config.tc_uboot_check_kconfig_preparepatch
  # find this patch here: src/files/ub-patches/0001-U-Boot-version-fix.patch
  # copy it to the lab pc and adapt tb.config.tc_uboot_check_kconfig_preparepatch
  #
  # Steps from this testcase:
  # - rm U-Boot code with tc_workfd_rm_uboot_code.py
  # - get U-Boot code with tc_lab_get_uboot_source.py
  # - set SOURCE_DATE_EPOCH=0 to get reproducible builds
  # - apply patch from tb.config.tc_uboot_check_kconfig_preparepatch
  #   get rid of local version ToDo: find a way to disable CONFIG_LOCALVERSION_AUTO
  #   so this patch is not longer needed.
  # - if tb.config.tc_uboot_check_kconfig_read_sumfile is != 'none'
  #     read a list of boards and md5sums from the file in
  #     tb.config.tc_uboot_check_kconfig_read_sumfile
  #   else
  #   - create a list of boards (all defconfigs)
  #   - do for all boards:
  #     - get architecture and set toolchain
  #     - compile U-Boot and calculate md5sum
  #       with tc_workfd_compile_uboot.py and tc_workfd_md5sum.py
  #     - if tb.config.tc_uboot_check_kconfig_create_sumfile != 'none'
  #       save the board md5sum lists in the file
  #       tb.config.tc_uboot_check_kconfig_create_sumfile
  #       you can use this now as a reference, so no need
  #       to calculate always for all boards the md5sums
  #       -> saves a lot of time!
  #
  # - apply patch(es) with tc_workfd_apply_patches.py
  # - do for all boards:
  #   - compile U-Boot again (patched version)
  #   - calculate md5sum again
  #   - calculate md5sums
  #   - check if they are the same

used Testcases:

:ref:`src_tc_uboot_tc_uboot_check_kconfig_py`.
:ref:`src_tc_linux_tc_workfd_rm_uboot_code_py`.
:ref:`src_tc_tc_lab_get_uboot_source_py`.
:ref:`src_tc_tc_workfd_compile_uboot_py`.
:ref:`src_tc_linux_tc_workfd_md5sum_py`.
:ref:`src_tc_tc_workfd_apply_patches_py`.

used config variables:

:ref:`tb_config_tc_uboot_check_kconfig_preparepatch`.
:ref:`tb_config_tc_uboot_check_kconfig_preparepatch`.
:ref:`tb_config_tc_uboot_check_kconfig_preparepatch`.
:ref:`tb_config_tc_uboot_check_kconfig_read_sumfile`.
:ref:`tb_config_tc_uboot_check_kconfig_read_sumfile`.
:ref:`tb_config_tc_uboot_check_kconfig_create_sumfile`.
:ref:`tb_config_tc_uboot_check_kconfig_create_sumfile`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_uboot_check_kconfig.py


.. _src_tc_uboot_tc_uboot_ext2load_py:

src/tc/uboot/tc_uboot_ext2load.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_uboot_ext2load.py
  #
  # load a file from ext2 into ram with ext2ls cmd.
  # check if the file has crc32 checksum 0x2144df1c
  #
  # How to create such a file, which has crc32 checksum of 0x2144df1c ?
  #
  # $ dd if=/dev/urandom of=test.bin bs=1M count=1
  # $ crc32 test.bin
  # 4f3fef33
  # $ perl -e 'print pack "H*", "33ef3f4f"' >> test.bin
  # $ crc32 test.bin
  # 2144df1c
  #
  # https://stackoverflow.com/questions/28591991/crc32-of-already-crc32-treated-data-with-the-crc-data-appended
  #
  # !! Don;t forget Big into little endian conversion
  #
  # used vars:
  # tc_uboot_ext2load_interface = 'usb'
  # tc_uboot_ext2load_dev = '0:1'
  # tc_uboot_ext2load_addr = '10000000'
  # tc_uboot_ext2load_file = '/test.bin'
  # tc_uboot_ext2load_check = 'no'
  #   if 'yes' check if the file tc_uboot_ext2load_file
  #   has the checksum 0x2144df1c

used Testcases:

:ref:`src_tc_uboot_tc_uboot_ext2load_py`.
:ref:`_tc_uboot_ext2load_interface`.
:ref:`_tc_uboot_ext2load_dev`.
:ref:`_tc_uboot_ext2load_addr`.
:ref:`_tc_uboot_ext2load_file`.
:ref:`_tc_uboot_ext2load_check`.
:ref:`_tc_uboot_ext2load_file`.


links:

https://stackoverflow.com/questions/28591991/crc32-of-already-crc32-treated-data-with-the-crc-data-appended



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_uboot_ext2load.py


.. _src_tc_uboot_tc_uboot_ext2ls_py:

src/tc/uboot/tc_uboot_ext2ls.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_uboot_ext2ls.py
  #
  # simply call ext2ls
  #
  # used vars:
  # tb.config.tc_uboot_ext2ls_expect = ['lost+found']
  #   strings we expect from the ext2ls command
  # tb.config.tc_uboot_ext2ls_interface = 'usb'
  # tb.config.tc_uboot_ext2ls_dev = '0:1'
  # tb.config.tc_uboot_ext2ls_dir = '/'

used Testcases:

:ref:`src_tc_uboot_tc_uboot_ext2ls_py`.

used config variables:

:ref:`tb_config_tc_uboot_ext2ls_expect`.
:ref:`tb_config_tc_uboot_ext2ls_interface`.
:ref:`tb_config_tc_uboot_ext2ls_dev`.
:ref:`tb_config_tc_uboot_ext2ls_dir`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_uboot_ext2ls.py


.. _src_tc_uboot_tc_uboot_get_arch_py:

src/tc/uboot/tc_uboot_get_arch.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c config/tbot_dxr2_uboot_kconfig_check.cfg -t tc_uboot_get_arch.py
  # get architecture from u-boot config

used Testcases:

:ref:`src_tc_uboot_tc_uboot_get_arch_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_uboot_get_arch.py


.. _src_tc_uboot_tc_uboot_load_bin_with_kermit_py:

src/tc/uboot/tc_uboot_load_bin_with_kermit.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -c -s lab_denx -c nero -t tc_uboot_load_bin_with_kermit.py
  # start tc:
  # load binary into ram with loadb
  #
  # precondition:
  # kermit must be used
  #
  # steps:
  # - loadb tb.config.tc_uboot_load_bin_ram_addr
  # - leave kermit
  # - send tb.config.tc_uboot_load_bin_file
  #   protocol: kermit_protocol='kermit'
  # wait for "C-Kermit>"
  # connect
  # you must get back something like this:
  # ## Total Size      = 0x00050bc0 = 330688 Bytes
  # ## Start Addr      = 0x81000000

used Testcases:

:ref:`src_tc_uboot_tc_uboot_load_bin_with_kermit_py`.

used config variables:

:ref:`tb_config_tc_uboot_load_bin_ram_addr`.
:ref:`tb_config_tc_uboot_load_bin_file`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_uboot_load_bin_with_kermit.py


.. _src_tc_uboot_tc_uboot_usb_info_py:

src/tc/uboot/tc_uboot_usb_info.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_uboot_usb_info.py
  #
  # call "usb info" command
  #
  # used vars:
  # tb.config.tc_uboot_usb_info_expect = ['Hub,  USB Revision 2.0',
  #    'Mass Storage,  USB Revision 2.0']

used Testcases:

:ref:`src_tc_uboot_tc_uboot_usb_info_py`.

used config variables:

:ref:`tb_config_tc_uboot_usb_info_expect`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_uboot_usb_info.py


.. _src_tc_uboot_tc_uboot_usb_start_py:

src/tc/uboot/tc_uboot_usb_start.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -s lab_denx -c fipad -t tc_uboot_usb_start.py
  #
  # call "usb start" command
  #
  # used vars:
  # tb.config.tc_uboot_usb_start_expect = ['Storage Device(s) found']

used Testcases:

:ref:`src_tc_uboot_tc_uboot_usb_start_py`.

used config variables:

:ref:`tb_config_tc_uboot_usb_start_expect`.



https://github.com/hsdenx/tbot/tree/master/src/tc/uboot/tc_uboot_usb_start.py


src/tc/yocto
------------


.. _src_tc_yocto_tc_workfd_bitbake_py:

src/tc/yocto/tc_workfd_bitbake.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_bitbake.py
  # simple call bitbake with tb.config.tc_workfd_bitbake_args

used Testcases:

:ref:`src_tc_yocto_tc_workfd_bitbake_py`.

used config variables:

:ref:`tb_config_tc_workfd_bitbake_args`.



https://github.com/hsdenx/tbot/tree/master/src/tc/yocto/tc_workfd_bitbake.py


.. _src_tc_yocto_tc_workfd_get_yocto_source_py:

src/tc/yocto/tc_workfd_get_yocto_source.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_get_yocto_source.py
  # get yocto source tb.config.tc_workfd_get_yocto_patches_git_repo with "git clone"
  # check out branch:
  # tb.config.tc_workfd_get_yocto_patches_git_branch
  # check out commit ID:
  # tb.config.tc_workfd_get_yocto_git_commit_id
  # apply patches with "git am" from directory:
  # tb.config.tc_workfd_get_yocto_clone_apply_patches_git_am_dir
  # additionally define a reference for cloning:
  # tb.config.tc_workfd_get_yocto_source_git_reference
  # if a user/password for cloning is needed, define the user:
  # tb.config.tc_workfd_get_yocto_source_git_repo_user
  # and set the password in password.py
  #
  # get other layers defined in the list:
  # tb.config.tc_workfd_get_yocto_source_layers
  # one element contains the follwoing list element:
  # ['git repo',
  #  'git branch',
  #  'git commit id',
  #  'apply_patches_dir'
  #  'apply_patches_git_am_dir',
  #  'source_git_reference',
  #  'source_git_repo_user',
  #  'source_git_repo_name'
  # ]
  #
  # at the end overwrite yocto configuration found in
  # tb.config.tc_workfd_get_yocto_source_conf_dir
  #
  # clones into directory tb.config.yocto_name
  # created with tc_workfd_goto_yocto_code.py
  #

used Testcases:

:ref:`src_tc_yocto_tc_workfd_get_yocto_source_py`.
:ref:`src_tc_yocto_tc_workfd_goto_yocto_code_py`.

used config variables:

:ref:`tb_config_tc_workfd_get_yocto_patches_git_repo`.
:ref:`tb_config_tc_workfd_get_yocto_patches_git_branch`.
:ref:`tb_config_tc_workfd_get_yocto_git_commit_id`.
:ref:`tb_config_tc_workfd_get_yocto_clone_apply_patches_git_am_dir`.
:ref:`tb_config_tc_workfd_get_yocto_source_git_reference`.
:ref:`tb_config_tc_workfd_get_yocto_source_git_repo_user`.
:ref:`tb_config_tc_workfd_get_yocto_source_layers`.
:ref:`tb_config_tc_workfd_get_yocto_source_conf_dir`.
:ref:`tb_config_yocto_name`.



https://github.com/hsdenx/tbot/tree/master/src/tc/yocto/tc_workfd_get_yocto_source.py


.. _src_tc_yocto_tc_workfd_goto_yocto_code_py:

src/tc/yocto/tc_workfd_goto_yocto_code.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_goto_yocto_code.py
  # switch into yocto source tb.config.tc_lab_source_dir + "/yocto-" + tb.config.boardlabname
  # set tb.config.yocto_name to "yocto-" + tb.config.boardlabname
  # and tb.config.yocto_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.yocto_name
  # and set $TBOT_BASEDIR_YOCTO to tb.config.yocto_fulldir_name

used Testcases:

:ref:`src_tc_yocto_tc_workfd_goto_yocto_code_py`.

used config variables:

:ref:`tb_config_tc_lab_source_dir`.
:ref:`tb_config_boardlabname`.
:ref:`tb_config_yocto_name`.
:ref:`tb_config_boardlabname`.
:ref:`tb_config_yocto_fulldir_name`.
:ref:`tb_config_tc_lab_source_dir`.
:ref:`tb_config_yocto_name`.
:ref:`tb_config_yocto_fulldir_name`.



https://github.com/hsdenx/tbot/tree/master/src/tc/yocto/tc_workfd_goto_yocto_code.py


.. _src_tc_yocto_tc_workfd_yocto_basic_check_py:

src/tc/yocto/tc_workfd_yocto_basic_check.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c cuby -t tc_workfd_yocto_basic_check.py
  #
  # do basic yocto checks
  #
  # - check rootfs version
  # - check dmesg output
  #   check if strings defined in tb.config.tc_demo_yocto_test_checks
  #   are found in dmesg output
  # - check if devmem2 tool is in rootfs, if so, do register checks
  #

used Testcases:

:ref:`src_tc_yocto_tc_workfd_yocto_basic_check_py`.

used config variables:

:ref:`tb_config_tc_demo_yocto_test_checks`.



https://github.com/hsdenx/tbot/tree/master/src/tc/yocto/tc_workfd_yocto_basic_check.py


.. _src_tc_yocto_tc_workfd_yocto_check_rootfs_version_py:

src/tc/yocto/tc_workfd_yocto_check_rootfs_version.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c cuby -t tc_workfd_yocto_check_rootfs_version.py
  #
  # check if the current /etc/version on the target rootfs is the
  # same as in tb.onfig.tc_yocto_get_rootfs_from_tarball
  #

used Testcases:

:ref:`src_tc_yocto_tc_workfd_yocto_check_rootfs_version_py`.

used config variables:

:ref:`tb_onfig_tc_yocto_get_rootfs_from_tarball`.



https://github.com/hsdenx/tbot/tree/master/src/tc/yocto/tc_workfd_yocto_check_rootfs_version.py


.. _src_tc_yocto_tc_yocto_get_rootfs_from_tarball_py:

src/tc/yocto/tc_yocto_get_rootfs_from_tarball.py
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

::

  # start with
  # tbot.py -s lab_denx -c cuby -t tc_yocto_get_rootfs_from_tarball.py
  #
  # get rootfs version from rootfs tar ball filepath and name stored in
  # tb.config.tc_yocto_get_rootfs_from_tarball
  # and store versionstring in variable:
  # tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version

used Testcases:

:ref:`src_tc_yocto_tc_yocto_get_rootfs_from_tarball_py`.

used config variables:

:ref:`tb_config_tc_yocto_get_rootfs_from_tarball`.
:ref:`tb_config_tc_yocto_get_rootfs_from_tarball_rootfs_version`.



https://github.com/hsdenx/tbot/tree/master/src/tc/yocto/tc_yocto_get_rootfs_from_tarball.py


.. _src_tc_tc_board_git_bisect_py:

src/tc/tc_board_git_bisect.py
-----------------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot_tqm5200s.cfg -t tc_board_git_bisect.py
  # get a source code with tc tb.config.board_git_bisect_get_source_tc
  # and start a "git bisect" session
  # current commit is bad
  # good commit id is defined through tb.config.board_git_bisect_good_commit
  # tc for testing good or bad is tb.config.board_git_bisect_call_tc
  # if you have some local patches, which needs to be applied
  # each git bisect step, set tb.config.board_git_bisect_patches
  #
  # if you need to restore your board after a failure, set the
  # variable tb.config.board_git_bisect_restore to the tc name
  # which restores the board.

used Testcases:

:ref:`src_tc_tc_board_git_bisect_py`.

used config variables:

:ref:`tb_config_board_git_bisect_get_source_tc`.
:ref:`tb_config_board_git_bisect_good_commit`.
:ref:`tb_config_board_git_bisect_call_tc`.
:ref:`tb_config_board_git_bisect_patches`.
:ref:`tb_config_board_git_bisect_restore`.



https://github.com/hsdenx/tbot/tree/master/src/tc/tc_board_git_bisect.py


.. _src_tc_tc_lab_apply_patches_py:

src/tc/tc_lab_apply_patches.py
------------------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_apply_patches.py
  # apply patches to source

used Testcases:

:ref:`src_tc_tc_lab_apply_patches_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/tc_lab_apply_patches.py


.. _src_tc_tc_lab_compile_uboot_py:

src/tc/tc_lab_compile_uboot.py
------------------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_compile_uboot.py
  # compile u-boot

used Testcases:

:ref:`src_tc_tc_lab_compile_uboot_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/tc_lab_compile_uboot.py


.. _src_tc_tc_lab_cp_file_py:

src/tc/tc_lab_cp_file.py
------------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_cp_file.py
  # simple copy  file from arg.get('s')
  # to arg.get('t') on the channel arg.get('ch')

used Testcases:

:ref:`src_tc_tc_lab_cp_file_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/tc_lab_cp_file.py


.. _src_tc_tc_lab_get_uboot_source_py:

src/tc/tc_lab_get_uboot_source.py
---------------------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_get_uboot_source.py
  # get U-Boot source
  # and go into the source tree

used Testcases:

:ref:`src_tc_tc_lab_get_uboot_source_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/tc_lab_get_uboot_source.py


.. _src_tc_tc_lab_poweroff_py:

src/tc/tc_lab_poweroff.py
-------------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_poweroff.py
  # simple power off the board

used Testcases:

:ref:`src_tc_tc_lab_poweroff_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/tc_lab_poweroff.py


.. _src_tc_tc_lab_poweron_py:

src/tc/tc_lab_poweron.py
------------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_poweron.py
  # simple power on the board

used Testcases:

:ref:`src_tc_tc_lab_poweron_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/tc_lab_poweron.py


.. _src_tc_tc_lab_rm_dir_py:

src/tc/tc_lab_rm_dir.py
-----------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_rm_dir.py
  # simple rm a directory on the lab

used Testcases:

:ref:`src_tc_tc_lab_rm_dir_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/tc_lab_rm_dir.py


.. _src_tc_tc_lab_set_toolchain_py:

src/tc/tc_lab_set_toolchain.py
------------------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_set_toolchain.py
  # set the toolchain

used Testcases:

:ref:`src_tc_tc_lab_set_toolchain_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/tc_lab_set_toolchain.py


.. _src_tc_tc_ub_boot_linux_py:

src/tc/tc_ub_boot_linux.py
--------------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_boot_linux.py
  # - load u-boot environment with testcase "tc_ub_load_board_env.py"
  # - execute u-boot cmd tb.config.ub_boot_linux_cmd

used Testcases:

:ref:`src_tc_tc_ub_boot_linux_py`.

used config variables:

:ref:`tb_config_ub_boot_linux_cmd`.



https://github.com/hsdenx/tbot/tree/master/src/tc/tc_ub_boot_linux.py


.. _src_tc_tc_workfd_apply_patches_py:

src/tc/tc_workfd_apply_patches.py
---------------------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_lab_apply_patches.py
  # apply patches to source

used Testcases:

:ref:`src_tc_tc_lab_apply_patches_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/tc_workfd_apply_patches.py


.. _src_tc_tc_workfd_compile_uboot_py:

src/tc/tc_workfd_compile_uboot.py
---------------------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_compile_uboot.py
  # compile u-boot

used Testcases:

:ref:`src_tc_tc_workfd_compile_uboot_py`.




https://github.com/hsdenx/tbot/tree/master/src/tc/tc_workfd_compile_uboot.py


.. _src_tc_tc_workfd_git_clone_source_py:

src/tc/tc_workfd_git_clone_source.py
------------------------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_git_clone_source.py
  # get source from git repo tb.config.tc_lab_git_clone_source_git_repo with "git clone"
  # and go into the source tree. 
  # check out branch tb.config.tc_lab_git_clone_source_git_branch
  # and Apply patches if needed with:
  # tc_lab_apply_patches.py and patches from directory
  # tb.config.tc_lab_git_clone_apply_patches_dir
  # use as reference tb.config.tc_lab_git_clone_source_git_reference
  # if != 'none'
  # You can give the repo a name with setting
  # tb.config.tc_lab_git_clone_source_git_repo_name
  # != 'none'
  # If you need a user/password for clining, you can define
  # the username through:
  # tb.config.tc_lab_git_clone_source_git_repo_user
  # define the password for this in password.py
  # boardname in password.py is used as tb.config.tc_lab_git_clone_source_git_repo

used Testcases:

:ref:`src_tc_tc_workfd_git_clone_source_py`.
:ref:`src_tc_tc_lab_apply_patches_py`.

used config variables:

:ref:`tb_config_tc_lab_git_clone_source_git_repo`.
:ref:`tb_config_tc_lab_git_clone_source_git_branch`.
:ref:`tb_config_tc_lab_git_clone_apply_patches_dir`.
:ref:`tb_config_tc_lab_git_clone_source_git_reference`.
:ref:`tb_config_tc_lab_git_clone_source_git_repo_name`.
:ref:`tb_config_tc_lab_git_clone_source_git_repo_user`.
:ref:`tb_config_tc_lab_git_clone_source_git_repo`.



https://github.com/hsdenx/tbot/tree/master/src/tc/tc_workfd_git_clone_source.py


.. _src_tc_tc_workfd_set_toolchain_py:

src/tc/tc_workfd_set_toolchain.py
---------------------------------

::

  # start with
  # python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_set_toolchain.py
  # set the toolchain, dependend on the architecture setting in
  # tb.config.tc_workfd_set_toolchain_arch
  # supported toolchains defined in
  # tb.config.tc_workfd_set_toolchain_t_p and tb.config.tc_workfd_set_toolchain_cr_co

used Testcases:

:ref:`src_tc_tc_workfd_set_toolchain_py`.

used config variables:

:ref:`tb_config_tc_workfd_set_toolchain_arch`.
:ref:`tb_config_tc_workfd_set_toolchain_t_p`.
:ref:`tb_config_tc_workfd_set_toolchain_cr_co`.



https://github.com/hsdenx/tbot/tree/master/src/tc/tc_workfd_set_toolchain.py


