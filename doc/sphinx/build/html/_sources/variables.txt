Documentation of all Variables
==============================


.. _tb_config_debug:

debug 
------

::

  debug = False


.. _tb_config_debugstatus:

debugstatus 
------------

::

  debugstatus = False


.. _tb_config_uboot_strings:

uboot_strings 
--------------

::

  uboot_strings = ['Autobooting in', 'noautoboot',  'autoboot', 'EOF', 'RomBOOT']


.. _tb_config_uboot_autoboot_key:

uboot_autoboot_key 
-------------------

::

  uboot_autoboot_key = ''


.. _tb_power_state:

tb_power_state 
---------------

::

  tb_power_state = 'undef'


.. _tb_config_term_line_length:

term_line_length 
-----------------

::

  term_line_length = '200'


.. _tb_config_wdt_timeout:

wdt_timeout 
------------

::

  wdt_timeout = '120' # wdt timeout after 2 minutes


.. _tb_config_state_linux_timeout:

state_linux_timeout 
--------------------

::

  state_linux_timeout = 4


.. _tb_config_labsshprompt:

labsshprompt 
-------------

::

  labsshprompt = '$ '


.. _tb_config_tc_return:

tc_return 
----------

::

  tc_return = True


.. _tb_config_tc_workfd_check_if_cmd_exist_cmdname:

tc_workfd_check_if_cmd_exist_cmdname 
-------------------------------------

::

  tc_workfd_check_if_cmd_exist_cmdname = 'none'


.. _tb_config_setenv_name:

setenv_name 
------------

::

  setenv_name = 'tralala'


.. _tb_config_setenv_value:

setenv_value 
-------------

::

  setenv_value = 'hulalahups'


.. _tb_config_tc_ub_boot_linux_load_env:

tc_ub_boot_linux_load_env 
--------------------------

::

  tc_ub_boot_linux_load_env = 'load'


.. _tb_config_tc_lx_mount_dev:

tc_lx_mount_dev 
----------------

::

  tc_lx_mount_dev = '/dev/sda1'


.. _tb_config_tc_lx_mount_fs_type:

tc_lx_mount_fs_type 
--------------------

::

  tc_lx_mount_fs_type = 'ext4'


.. _tb_config_tc_lx_mount_dir:

tc_lx_mount_dir 
----------------

::

  tc_lx_mount_dir = '/home/hs/mnt'


.. _tb_config_tc_lx_bonnie_dev:

tc_lx_bonnie_dev 
-----------------

::

  tc_lx_bonnie_dev = tc_lx_mount_dev


.. _tb_config_tc_lx_bonnie_sz:

tc_lx_bonnie_sz 
----------------

::

  tc_lx_bonnie_sz = '968'


.. _tb_config_ub_load_board_env_addr:

ub_load_board_env_addr 
-----------------------

::

  ub_load_board_env_addr = '0x81000000'


.. _tb_config_ub_load_board_env_subdir:

ub_load_board_env_subdir 
-------------------------

::

  ub_load_board_env_subdir = 'tbot'


.. _tb_config_ub_load_board_env_set:

ub_load_board_env_set 
----------------------

::

  ub_load_board_env_set = []


.. _tb_config_ub_boot_linux_cmd:

ub_boot_linux_cmd 
------------------

::

  ub_boot_linux_cmd = 'run tbot_boot_linux'


.. _tb_config_tc_lab_compile_uboot_boardname:

tc_lab_compile_uboot_boardname 
-------------------------------

::

  tc_lab_compile_uboot_boardname = 'config.boardname'


.. _tb_config_tc_lab_compile_uboot_makeoptions:

tc_lab_compile_uboot_makeoptions 
---------------------------------

::

  tc_lab_compile_uboot_makeoptions = '-j4'


.. _tb_config_do_connect_to_board:

do_connect_to_board 
--------------------

::

  do_connect_to_board = True


.. _tb_config_tc_lab_compile_uboot_export_path:

tc_lab_compile_uboot_export_path 
---------------------------------

::

  tc_lab_compile_uboot_export_path = 'none'


.. _tb_config_tftpboardname:

tftpboardname 
--------------

::

  tftpboardname = 'config.boardname'


.. _tb_config_boardlabname:

boardlabname 
-------------

::

  boardlabname = 'config.boardname'


.. _tb_config_boardlabpowername:

boardlabpowername 
------------------

::

  boardlabpowername = 'config.boardname'


.. _tb_config_tftprootdir:

tftprootdir
-----------

::

  tftprootdir='/tftpboot/'


.. _tb_config_tftpboardrootdir:

tftpboardrootdir
----------------

::

  tftpboardrootdir=''


.. _tb_config_tc_ub_dfu_dfu_util_path:

tc_ub_dfu_dfu_util_path 
------------------------

::

  tc_ub_dfu_dfu_util_path = "/home/hs/zug/dfu-util"


.. _tb_config_tc_ub_dfu_dfu_util_alt_setting:

tc_ub_dfu_dfu_util_alt_setting 
-------------------------------

::

  tc_ub_dfu_dfu_util_alt_setting = "Linux"


.. _tb_config_tc_lab_source_dir:

tc_lab_source_dir 
------------------

::

  tc_lab_source_dir = "/work/hs/tbot"


.. _tb_config_tc_lab_get_uboot_source_git_repo:

tc_lab_get_uboot_source_git_repo 
---------------------------------

::

  tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"


.. _tb_config_tc_lab_get_uboot_source_git_branch:

tc_lab_get_uboot_source_git_branch 
-----------------------------------

::

  tc_lab_get_uboot_source_git_branch = "master"


.. _tb_config_tc_lab_toolchain_rev:

tc_lab_toolchain_rev 
---------------------

::

  tc_lab_toolchain_rev = "5.4"


.. _tb_config_tc_lab_toolchain_name:

tc_lab_toolchain_name 
----------------------

::

  tc_lab_toolchain_name = "armv5te"


.. _tb_config_tc_ub_ubi_load_name:

tc_ub_ubi_load_name 
--------------------

::

  tc_ub_ubi_load_name = "kernel"


.. _tb_config_tc_ub_ubi_prep_partname:

tc_ub_ubi_prep_partname 
------------------------

::

  tc_ub_ubi_prep_partname = "ubi"


.. _tb_config_tc_ub_ubi_prep_offset:

tc_ub_ubi_prep_offset 
----------------------

::

  tc_ub_ubi_prep_offset = "none"


.. _tb_config_tc_ub_ubi_load_addr:

tc_ub_ubi_load_addr 
--------------------

::

  tc_ub_ubi_load_addr = "14000000"


.. _tb_config_tc_ub_ubi_create_vol_name:

tc_ub_ubi_create_vol_name 
--------------------------

::

  tc_ub_ubi_create_vol_name = 'config.tc_ub_ubi_load_name'


.. _tb_config_tc_ub_ubi_create_vol_sz:

tc_ub_ubi_create_vol_sz 
------------------------

::

  tc_ub_ubi_create_vol_sz = "600000"


.. _tb_config_tc_ub_ubi_write_len:

tc_ub_ubi_write_len 
--------------------

::

  tc_ub_ubi_write_len = '0xc00000'


.. _tb_config_tc_ub_ubi_write_addr:

tc_ub_ubi_write_addr 
---------------------

::

  tc_ub_ubi_write_addr = 'config.tc_ub_ubi_load_addr'


.. _tb_config_tc_ub_ubi_write_vol_name:

tc_ub_ubi_write_vol_name 
-------------------------

::

  tc_ub_ubi_write_vol_name = 'config.tc_ub_ubi_create_vol_name'


.. _tb_config_tc_ub_ubifs_volume_name:

tc_ub_ubifs_volume_name 
------------------------

::

  tc_ub_ubifs_volume_name = 'ubi:rootfs'


.. _tb_config_tc_ub_ubifs_ls_dir:

tc_ub_ubifs_ls_dir 
-------------------

::

  tc_ub_ubifs_ls_dir = '/'


.. _tb_config_tc_lx_gpio_nr:

tc_lx_gpio_nr 
--------------

::

  tc_lx_gpio_nr = '69'


.. _tb_config_tc_lx_gpio_dir:

tc_lx_gpio_dir 
---------------

::

  tc_lx_gpio_dir = 'out'


.. _tb_config_tc_lx_gpio_val:

tc_lx_gpio_val 
---------------

::

  tc_lx_gpio_val = '1'


.. _tb_config_tc_lx_eeprom_file:

tc_lx_eeprom_file 
------------------

::

  tc_lx_eeprom_file = '/sys/class/i2c-dev/i2c-0/device/0-0050/eeprom'


.. _tb_config_tc_lx_eeprom_tmp_dir:

tc_lx_eeprom_tmp_dir 
---------------------

::

  tc_lx_eeprom_tmp_dir = 'config.lab_tmp_dir'


.. _tb_config_tc_lx_eeprom_wp_gpio:

tc_lx_eeprom_wp_gpio 
---------------------

::

  tc_lx_eeprom_wp_gpio = 'none'


.. _tb_config_tc_lx_eeprom_wp_val:

tc_lx_eeprom_wp_val 
--------------------

::

  tc_lx_eeprom_wp_val = "0"


.. _tb_config_tc_lx_eeprom_wp_sz:

tc_lx_eeprom_wp_sz 
-------------------

::

  tc_lx_eeprom_wp_sz = "4096"


.. _tb_config_tc_lx_eeprom_wp_obs:

tc_lx_eeprom_wp_obs 
--------------------

::

  tc_lx_eeprom_wp_obs = "32"


.. _tb_config_tc_lx_eeprom_wp_wc:

tc_lx_eeprom_wp_wc 
-------------------

::

  tc_lx_eeprom_wp_wc = "128"


.. _tb_config_tc_lx_cpufreq_frequences:

tc_lx_cpufreq_frequences 
-------------------------

::

  tc_lx_cpufreq_frequences = ['294']


.. _tb_config_tc_lx_check_usb_authorized:

tc_lx_check_usb_authorized 
---------------------------

::

  tc_lx_check_usb_authorized = 'usb 1-1'


.. _tb_config_tc_workfd_work_dir:

tc_workfd_work_dir 
-------------------

::

  tc_workfd_work_dir = "/work/tbot"


.. _tb_config_tc_workfd_check_if_file_exists_name:

tc_workfd_check_if_file_exists_name 
------------------------------------

::

  tc_workfd_check_if_file_exists_name = "bonnie++-1.03e.tgz"


.. _tb_config_tc_workfd_check_if_dir_exists_name:

tc_workfd_check_if_dir_exists_name 
-----------------------------------

::

  tc_workfd_check_if_dir_exists_name = "mtd-utils"


.. _tb_config_tc_lx_dmesg_grep_name:

tc_lx_dmesg_grep_name 
----------------------

::

  tc_lx_dmesg_grep_name = "zigbee"


.. _tb_config_tc_lx_readreg_mask:

tc_lx_readreg_mask 
-------------------

::

  tc_lx_readreg_mask = "0x000000ff"


.. _tb_config_tc_lx_readreg_type:

tc_lx_readreg_type 
-------------------

::

  tc_lx_readreg_type = "w"


.. _tb_config_tc_lx_create_reg_file_name:

tc_lx_create_reg_file_name 
---------------------------

::

  tc_lx_create_reg_file_name = "pinmux.reg"


.. _tb_config_tc_lx_create_reg_file_start:

tc_lx_create_reg_file_start 
----------------------------

::

  tc_lx_create_reg_file_start = "0x44e10800"


.. _tb_config_tc_lx_create_reg_file_stop:

tc_lx_create_reg_file_stop 
---------------------------

::

  tc_lx_create_reg_file_stop = "0x44e10a34"


.. _tb_config_tc_lx_regulator_nrs:

tc_lx_regulator_nrs 
--------------------

::

  tc_lx_regulator_nrs = ['0 regulator-dummy -', '1 hsusb1_vbus 5000000',
  '2 vmmc 3300000', '3 pbias_mmc_omap2430 3000000',
  '4 DCDC1 1200000', '5 DCDC2 3300000', '6 DCDC3 1800000',
  '7 LDO1 1800000', '8 LDO2 3300000']


.. _tb_config_board_has_debugger:

board_has_debugger 
-------------------

::

  board_has_debugger = 0


.. _tb_config_lab_bdi_upd_uboot_bdi_cmd:

lab_bdi_upd_uboot_bdi_cmd 
--------------------------

::

  lab_bdi_upd_uboot_bdi_cmd = 'telnet bdi6'


.. _tb_config_lab_bdi_upd_uboot_bdi_prompt:

lab_bdi_upd_uboot_bdi_prompt 
-----------------------------

::

  lab_bdi_upd_uboot_bdi_prompt = 'BDI>'


.. _tb_config_lab_bdi_upd_uboot_bdi_era:

lab_bdi_upd_uboot_bdi_era 
--------------------------

::

  lab_bdi_upd_uboot_bdi_era = 'era'


.. _tb_config_lab_bdi_upd_uboot_bdi_prog:

lab_bdi_upd_uboot_bdi_prog 
---------------------------

::

  lab_bdi_upd_uboot_bdi_prog = 'prog 0xfc000000'


.. _tb_config_lab_bdi_upd_uboot_bdi_file:

lab_bdi_upd_uboot_bdi_file 
---------------------------

::

  lab_bdi_upd_uboot_bdi_file = '/tftpboot/tqm5200s/tbot/u-boot.bin'


.. _tb_config_lab_bdi_upd_uboot_bdi_run:

lab_bdi_upd_uboot_bdi_run 
--------------------------

::

  lab_bdi_upd_uboot_bdi_run = [{'cmd':'res run', 'val':'resetting target passed'}]


.. _tb_config_board_git_bisect_get_source_tc:

board_git_bisect_get_source_tc 
-------------------------------

::

  board_git_bisect_get_source_tc = 'tc_lab_get_uboot_source.py'


.. _tb_config_board_git_bisect_call_tc:

board_git_bisect_call_tc 
-------------------------

::

  board_git_bisect_call_tc = 'tc_board_tqm5200s_ub_comp_install.py'


.. _tb_config_board_git_bisect_good_commit:

board_git_bisect_good_commit 
-----------------------------

::

  board_git_bisect_good_commit = 'f9860cf'


.. _tb_config_board_git_bisect_patches:

board_git_bisect_patches 
-------------------------

::

  board_git_bisect_patches = 'none'


.. _tb_config_tc_lab_apply_patches_dir:

tc_lab_apply_patches_dir 
-------------------------

::

  tc_lab_apply_patches_dir =  'none'


.. _tb_config_tc_ubi_cmd_path:

tc_ubi_cmd_path 
----------------

::

  tc_ubi_cmd_path = "/work/tbot/mtd-utils"


.. _tb_config_tc_ubi_mtd_dev:

tc_ubi_mtd_dev 
---------------

::

  tc_ubi_mtd_dev = "/dev/mtd4"


.. _tb_config_tc_ubi_ubi_dev:

tc_ubi_ubi_dev 
---------------

::

  tc_ubi_ubi_dev = "/dev/ubi0"


.. _tb_config_tc_ubi_min_io_size:

tc_ubi_min_io_size 
-------------------

::

  tc_ubi_min_io_size = "1024"


.. _tb_config_tc_ubi_max_leb_cnt:

tc_ubi_max_leb_cnt 
-------------------

::

  tc_ubi_max_leb_cnt = "100"


.. _tb_config_tc_ubi_leb_size:

tc_ubi_leb_size 
----------------

::

  tc_ubi_leb_size = "126976"


.. _tb_config_tc_ubi_vid_hdr_offset:

tc_ubi_vid_hdr_offset 
----------------------

::

  tc_ubi_vid_hdr_offset = "default"


.. _tb_config_tc_lx_ubi_format_filename:

tc_lx_ubi_format_filename 
--------------------------

::

  tc_lx_ubi_format_filename = "/home/hs/ccu1/ecl-image-usbc.ubi"


.. _tb_config_tc_workfd_apply_patchwork_patches_list:

tc_workfd_apply_patchwork_patches_list 
---------------------------------------

::

  tc_workfd_apply_patchwork_patches_list = []


.. _tb_config_tc_workfd_apply_patchwork_patches_list_hand:

tc_workfd_apply_patchwork_patches_list_hand 
--------------------------------------------

::

  tc_workfd_apply_patchwork_patches_list_hand = []


.. _tb_config_tc_workfd_apply_patchwork_patches_blacklist:

tc_workfd_apply_patchwork_patches_blacklist 
--------------------------------------------

::

  tc_workfd_apply_patchwork_patches_blacklist = []


.. _tb_config_tc_workfd_apply_patchwork_patches_checkpatch_cmd:

tc_workfd_apply_patchwork_patches_checkpatch_cmd 
-------------------------------------------------

::

  tc_workfd_apply_patchwork_patches_checkpatch_cmd = 'none'


.. _tb_config_tc_workfd_apply_patchwork_patches_eof:

tc_workfd_apply_patchwork_patches_eof 
--------------------------------------

::

  tc_workfd_apply_patchwork_patches_eof = 'yes'


.. _tb_config_tc_workfd_get_patchwork_number_list_order:

tc_workfd_get_patchwork_number_list_order 
------------------------------------------

::

  tc_workfd_get_patchwork_number_list_order = '-delegate'


.. _tb_config_tc_workfd_rm_file_name:

tc_workfd_rm_file_name 
-----------------------

::

  tc_workfd_rm_file_name = 'none'


.. _tb_config_tc_workfd_cd_name:

tc_workfd_cd_name 
------------------

::

  tc_workfd_cd_name = 'none'


.. _tb_config_tc_lab_get_linux_source_git_repo:

tc_lab_get_linux_source_git_repo 
---------------------------------

::

  tc_lab_get_linux_source_git_repo = "/home/git/linux.git"


.. _tb_config_tc_lab_get_linux_source_git_repo_user:

tc_lab_get_linux_source_git_repo_user 
--------------------------------------

::

  tc_lab_get_linux_source_git_repo_user = 'anonymous'


.. _tb_config_tc_lab_get_linux_source_git_branch:

tc_lab_get_linux_source_git_branch 
-----------------------------------

::

  tc_lab_get_linux_source_git_branch = "master"


.. _tb_config_tc_lab_get_linux_source_git_reference:

tc_lab_get_linux_source_git_reference 
--------------------------------------

::

  tc_lab_get_linux_source_git_reference = 'none'


.. _tb_config_tc_workfd_apply_local_patches_dir:

tc_workfd_apply_local_patches_dir 
----------------------------------

::

  tc_workfd_apply_local_patches_dir = 'none'


.. _tb_config_tc_workfd_apply_local_patches_checkpatch_cmd:

tc_workfd_apply_local_patches_checkpatch_cmd 
---------------------------------------------

::

  tc_workfd_apply_local_patches_checkpatch_cmd = 'none'


.. _tb_config_tc_workfd_apply_local_patches_checkpatch_cmd_strict:

tc_workfd_apply_local_patches_checkpatch_cmd_strict 
----------------------------------------------------

::

  tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"


.. _tb_config_tc_workfd_get_list_of_files_mask:

tc_workfd_get_list_of_files_mask 
---------------------------------

::

  tc_workfd_get_list_of_files_mask = '*'


.. _tb_config_tc_workfd_compile_linux_boardname:

tc_workfd_compile_linux_boardname 
----------------------------------

::

  tc_workfd_compile_linux_boardname = 'config.boardname'


.. _tb_config_tc_workfd_compile_linux_clean:

tc_workfd_compile_linux_clean 
------------------------------

::

  tc_workfd_compile_linux_clean = 'yes'


.. _tb_config_tc_workfd_compile_linux_modules:

tc_workfd_compile_linux_modules 
--------------------------------

::

  tc_workfd_compile_linux_modules = 'none'


.. _tb_config_tc_workfd_compile_linux_modules_path:

tc_workfd_compile_linux_modules_path 
-------------------------------------

::

  tc_workfd_compile_linux_modules_path = 'none'


.. _tb_config_tc_workfd_compile_linux_dt_name:

tc_workfd_compile_linux_dt_name 
--------------------------------

::

  tc_workfd_compile_linux_dt_name = 'none'


.. _tb_config_tc_workfd_compile_linux_append_dt:

tc_workfd_compile_linux_append_dt 
----------------------------------

::

  tc_workfd_compile_linux_append_dt = 'no'


.. _tb_config_tc_workfd_compile_linux_load_addr:

tc_workfd_compile_linux_load_addr 
----------------------------------

::

  tc_workfd_compile_linux_load_addr = 'no'


.. _tb_config_tc_workfd_compile_linux_make_target:

tc_workfd_compile_linux_make_target 
------------------------------------

::

  tc_workfd_compile_linux_make_target = 'uImage'


.. _tb_config_tc_workfd_compile_linux_fit_its_file:

tc_workfd_compile_linux_fit_its_file 
-------------------------------------

::

  tc_workfd_compile_linux_fit_its_file = 'no'


.. _tb_config_tc_workfd_compile_linux_fit_file:

tc_workfd_compile_linux_fit_file 
---------------------------------

::

  tc_workfd_compile_linux_fit_file = 'no'


.. _tb_config_tc_workfd_compile_linux_mkimage:

tc_workfd_compile_linux_mkimage 
--------------------------------

::

  tc_workfd_compile_linux_mkimage = '/home/hs/i2c/u-boot/tools/mkimage'


.. _tb_config_tc_workfd_compile_linux_makeoptions:

tc_workfd_compile_linux_makeoptions 
------------------------------------

::

  tc_workfd_compile_linux_makeoptions = ''


.. _tb_config_workfd_get_patchwork_number_user:

workfd_get_patchwork_number_user 
---------------------------------

::

  workfd_get_patchwork_number_user = 'hs'


.. _tb_config_workfd_get_patchwork_number_list_order:

workfd_get_patchwork_number_list_order 
---------------------------------------

::

  workfd_get_patchwork_number_list_order = '-delegate'


.. _tb_config_tc_workfd_connect_with_kermit_ssh:

tc_workfd_connect_with_kermit_ssh 
----------------------------------

::

  tc_workfd_connect_with_kermit_ssh = "none"


.. _tb_config_tc_workfd_connect_with_kermit_rlogin:

tc_workfd_connect_with_kermit_rlogin 
-------------------------------------

::

  tc_workfd_connect_with_kermit_rlogin = "none"


.. _tb_config_kermit_line:

kermit_line 
------------

::

  kermit_line = '/dev/ttyUSB0'


.. _tb_config_kermit_speed:

kermit_speed 
-------------

::

  kermit_speed = '115200'


.. _tb_config_tc_ub_tftp_file_addr:

tc_ub_tftp_file_addr 
---------------------

::

  tc_ub_tftp_file_addr = 'config.ub_load_board_env_addr'


.. _tb_config_tc_lab_denx_power_tc:

tc_lab_denx_power_tc 
---------------------

::

  tc_lab_denx_power_tc = 'tc_lab_denx_power.py'


.. _tb_config_tc_lab_denx_get_power_state_tc:

tc_lab_denx_get_power_state_tc 
-------------------------------

::

  tc_lab_denx_get_power_state_tc = 'tc_lab_denx_get_power_state.py'


.. _tb_config_tc_lab_denx_connect_to_board_tc:

tc_lab_denx_connect_to_board_tc 
--------------------------------

::

  tc_lab_denx_connect_to_board_tc = 'tc_lab_denx_connect_to_board.py'


.. _tb_config_tc_lab_denx_disconnect_from_board_tc:

tc_lab_denx_disconnect_from_board_tc 
-------------------------------------

::

  tc_lab_denx_disconnect_from_board_tc = 'tc_lab_denx_disconnect_from_board.py'


.. _tb_config_tc_ub_memory_ram_ws_base:

tc_ub_memory_ram_ws_base 
-------------------------

::

  tc_ub_memory_ram_ws_base = 'undef'


.. _tb_config_tc_ub_memory_ram_ws_base_alt:

tc_ub_memory_ram_ws_base_alt 
-----------------------------

::

  tc_ub_memory_ram_ws_base_alt = 'undef'


.. _tb_config_tc_ub_memory_ram_big:

tc_ub_memory_ram_big 
---------------------

::

  tc_ub_memory_ram_big = 'undef'


.. _tb_config_tc_lx_trigger_wdt_cmd:

tc_lx_trigger_wdt_cmd 
----------------------

::

  tc_lx_trigger_wdt_cmd = '/home/hs/wdt &'


.. _tb_config_tc_workfd_create_ubi_rootfs_path:

tc_workfd_create_ubi_rootfs_path 
---------------------------------

::

  tc_workfd_create_ubi_rootfs_path = '/opt/eldk-5.4/armv7a-hf/rootfs-minimal-mtdutils'


.. _tb_config_tc_workfd_create_ubi_rootfs_target:

tc_workfd_create_ubi_rootfs_target 
-----------------------------------

::

  tc_workfd_create_ubi_rootfs_target = '/tftpboot/dxr2/tbot/rootfs-minimal.ubifs'


.. _tb_config_tc_ub_i2c_help_with_bus:

tc_ub_i2c_help_with_bus 
------------------------

::

  tc_ub_i2c_help_with_bus = 'no'


.. _tb_config_dfu_test_sizes_default:

dfu_test_sizes_default 
-----------------------

::

  dfu_test_sizes_default = [
  64 - 1,
  64,
  64 + 1,
  128 - 1,
  128,
  128 + 1,
  960 - 1,
  960,
  960 + 1,
  4096 - 1,
  4096,
  4096 + 1,
  1024 * 1024 - 1,
  1024 * 1024,
  8 * 1024 * 1024,
  ]


.. _tb_config_workfd_ssh_cmd_prompt:

workfd_ssh_cmd_prompt 
----------------------

::

  workfd_ssh_cmd_prompt = '$'


.. _tb_config_linux_prompt_default:

linux_prompt_default 
---------------------

::

  linux_prompt_default = 'root@generic-armv7a-hf:~# '


.. _tb_config_labprompt:

labprompt 
----------

::

  labprompt = 'config.linux_prompt'


.. _tb_config_linux_user:

linux_user 
-----------

::

  linux_user = 'root'


.. _tb_config_create_dot:

create_dot 
-----------

::

  create_dot = 'no'


.. _tb_config_create_statistic:

create_statistic 
-----------------

::

  create_statistic = 'no'


.. _tb_config_create_dashboard:

create_dashboard 
-----------------

::

  create_dashboard = 'no'


.. _tb_config_create_webpatch:

create_webpatch 
----------------

::

  create_webpatch = 'no'


.. _tb_config_create_html_log:

create_html_log 
----------------

::

  create_html_log = 'no'


.. _tb_config_create_documentation:

create_documentation 
---------------------

::

  create_documentation = 'no'


.. _tb_config_event_documentation_strip_list:

event_documentation_strip_list 
-------------------------------

::

  event_documentation_strip_list = []


.. _tb_config_tc_ub_test_py_hook_script_path:

tc_ub_test_py_hook_script_path 
-------------------------------

::

  tc_ub_test_py_hook_script_path = '$HOME/testframework/hook-scripts'


.. _tb_config_switch_su_board:

switch_su_board 
----------------

::

  switch_su_board = 'lab'


.. _tb_config_tc_workfd_can_ssh:

tc_workfd_can_ssh 
------------------

::

  tc_workfd_can_ssh = 'no'


.. _tb_config_tc_workfd_can_ssh_prompt:

tc_workfd_can_ssh_prompt 
-------------------------

::

  tc_workfd_can_ssh_prompt = '$'


.. _tb_config_tc_workfd_can_su:

tc_workfd_can_su 
-----------------

::

  tc_workfd_can_su = 'no'


.. _tb_config_tc_workfd_can_dev:

tc_workfd_can_dev 
------------------

::

  tc_workfd_can_dev = 'can0'


.. _tb_config_tc_workfd_can_bitrate:

tc_workfd_can_bitrate 
----------------------

::

  tc_workfd_can_bitrate = '500000'


.. _tb_config_tc_workfd_can_iproute_dir:

tc_workfd_can_iproute_dir 
--------------------------

::

  tc_workfd_can_iproute_dir = '/home/hs/iproute2'


.. _tb_config_tc_workfd_can_util_dir:

tc_workfd_can_util_dir 
-----------------------

::

  tc_workfd_can_util_dir = '/home/hs/can-utils'


.. _tb_config_tc_workfd_hdparm_path:

tc_workfd_hdparm_path 
----------------------

::

  tc_workfd_hdparm_path = '/home/hs/shc/hdparm-9.50/'


.. _tb_config_tc_workfd_hdparm_dev:

tc_workfd_hdparm_dev 
---------------------

::

  tc_workfd_hdparm_dev = '/dev/mmcblk1'


.. _tb_config_tc_workfd_hdparm_min:

tc_workfd_hdparm_min 
---------------------

::

  tc_workfd_hdparm_min = '12.0'


.. _tb_config_tc_lab_git_clone_source_git_repo:

tc_lab_git_clone_source_git_repo 
---------------------------------

::

  tc_lab_git_clone_source_git_repo = 'git://git.yoctoproject.org/poky.git'


.. _tb_config_tc_lab_git_clone_source_git_branch:

tc_lab_git_clone_source_git_branch 
-----------------------------------

::

  tc_lab_git_clone_source_git_branch = 'morty'


.. _tb_config_tc_lab_git_clone_source_git_commit_id:

tc_lab_git_clone_source_git_commit_id 
--------------------------------------

::

  tc_lab_git_clone_source_git_commit_id = '73454473d7c286c41ee697f74052fed03c79f9f5'


.. _tb_config_tc_lab_git_clone_apply_patches_dir:

tc_lab_git_clone_apply_patches_dir 
-----------------------------------

::

  tc_lab_git_clone_apply_patches_dir = 'none'


.. _tb_config_tc_lab_git_clone_apply_patches_git_am_dir:

tc_lab_git_clone_apply_patches_git_am_dir 
------------------------------------------

::

  tc_lab_git_clone_apply_patches_git_am_dir = '/work/hs/ssi/patches/20161220/morty'


.. _tb_config_tc_lab_git_clone_source_git_reference:

tc_lab_git_clone_source_git_reference 
--------------------------------------

::

  tc_lab_git_clone_source_git_reference = 'none'


.. _tb_config_tc_lab_git_clone_source_git_repo_user:

tc_lab_git_clone_source_git_repo_user 
--------------------------------------

::

  tc_lab_git_clone_source_git_repo_user = ''


.. _tb_config_tc_lab_git_clone_source_git_repo_name:

tc_lab_git_clone_source_git_repo_name 
--------------------------------------

::

  tc_lab_git_clone_source_git_repo_name = 'none'


.. _tb_config_tc_workfd_get_yocto_source_layers:

tc_workfd_get_yocto_source_layers 
----------------------------------

::

  tc_workfd_get_yocto_source_layers = [
  ['git://git.openembedded.org/meta-openembedded', 'morty', '659d9d3f52bad33d7aa1c63e25681d193416d76e', 'none', 'none', 'none', '', 'meta-openembedded'],
  ['https://github.com/meta-qt5/meta-qt5.git', 'morty', '9aa870eecf6dc7a87678393bd55b97e21033ab48', 'none', '/work/hs/ssi/patches/20161220/qt5', 'none', '', 'meta-qt5'],
  ['https://github.com/sbabic/meta-swupdate.git', 'master', 'b3abfa78d04b88b88bcef6f5be9f2adff1293544', 'none', 'none', 'none', '', 'meta-swupdate'],
  ['git@gitlab.denx.de:ssi/meta-cuby.git', '20161220', 'none', 'none', 'none', 'none', '', 'meta-cuby'],
  ]


.. _tb_config_tc_workfd_get_yocto_source_conf_dl_dir:

tc_workfd_get_yocto_source_conf_dl_dir 
---------------------------------------

::

  tc_workfd_get_yocto_source_conf_dl_dir = 'none'


