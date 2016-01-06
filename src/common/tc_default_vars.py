# This file contains default values for all
# variables testcases use ...

try:
    self.term_line_length
except AttributeError:
    self.term_line_length = '200'
    tmp = 'Set terminal line length to ' + self.term_line_length
    self.debugprint(tmp)

try:
    self.read_line_retry
except AttributeError:
    self.read_line_retry = 1

try:
    self.read_end_state_retry
except AttributeError:
    self.read_end_state_retry = 1

try:
    self.tc_return
except AttributeError:
    self.tc_return = True

try:
    self.tc_workfd_check_if_cmd_exist_cmdname
except NameError:
    self.tc_workfd_check_if_cmd_exist_cmdname = 'none'
except AttributeError:
    self.tc_workfd_check_if_cmd_exist_cmdname = 'none'

#src/tc/tc_ub_setenv.py
try:
    self.setenv_name
except AttributeError:
    self.setenv_name = 'tralala'

try:
    self.setenv_value
except AttributeError:
    self.setenv_value = 'hulalahups'

try:
    self.tc_ub_boot_linux_load_env
except AttributeError:
    self.tc_ub_boot_linux_load_env = 1

#src/tc/tc_tftp_file.py
try:
    self.tc_lx_mount_dev
except AttributeError:
    self.tc_lx_mount_dev = '/dev/sda1'

try:
    self.tc_lx_mount_fs_type
except AttributeError:
    self.tc_lx_mount_fs_type = 'ext4'

try:
    self.tc_lx_mount_dir
except AttributeError:
    self.tc_lx_mount_dir = '/home/hs/mnt'

try:
    self.tc_lx_bonnie_dev
except AttributeError:
    self.tc_lx_bonnie_dev = self.tc_lx_mount_dir

try:
    self.tc_lx_bonnie_sz
except AttributeError:
    self.tc_lx_bonnie_sz = '968'

try:
    self.ub_load_board_env_addr
except AttributeError:
    self.ub_load_board_env_addr = '0x81000000'

try:
    self.ub_load_board_env_subdir
except AttributeError:
    self.ub_load_board_env_subdir = 'tbot'

try:
    self.ub_boot_linux_cmd
except AttributeError:
    self.ub_boot_linux_cmd = 'run tbot_boot_linux'

try:
    self.tc_lab_compile_uboot_boardname
except AttributeError:
    self.tc_lab_compile_uboot_boardname = self.boardname

try:
    self.tftpboardname
except AttributeError:
    self.tftpboardname = self.boardname
except NameError:
    self.tftpboardname = self.boardname

try:
    self.boardlabname
except AttributeError:
    self.boardlabname = self.boardname
except NameError:
    self.boardlabname = self.boardname

try:
    self.boardlabpowername
except AttributeError:
    self.boardlabpowername = self.boardname
except NameError:
    self.boardlabpowername = self.boardname

try:
    self.tc_ub_dfu_dfu_util_path
except AttributeError:
    self.tc_ub_dfu_dfu_util_path = "/home/hs/zug/dfu-util"

try:
    self.tc_ub_dfu_dfu_util_alt_setting
except AttributeError:
    self.tc_ub_dfu_dfu_util_alt_setting = "Linux"

try:
    self.tc_ub_dfu_dfu_util_downloadfile
except AttributeError:
    self.tc_ub_dfu_dfu_util_downloadfile = "/tmp/dfu_file"

try:
    self.tc_lab_source_dir
except AttributeError:
    self.tc_lab_source_dir = "/work/hs/tbot"

try:
    self.tc_lab_get_uboot_source_git_repo
except AttributeError:
    self.tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"

try:
    self.tc_lab_get_uboot_source_git_branch
except AttributeError:
    self.tc_lab_get_uboot_source_git_branch = "master"

try:
    self.tc_lab_end_git_clone_text
except AttributeError:
    self.tc_lab_end_git_clone_text = "done"

try:
    self.tc_lab_end_git_checkout_text
except AttributeError:
    self.tc_lab_end_git_checkout_text = "error"

try:
    self.tc_lab_toolchain_rev
except AttributeError:
    self.tc_lab_toolchain_rev = "5.4"

try:
    self.tc_lab_toolchain_name
except AttributeError:
    self.tc_lab_toolchain_name = "armv5te"

try:
    self.tc_lab_cp_file_a
except AttributeError:
    self.tc_lab_cp_file_a = "/tmp/gnlmpf"

try:
    self.tc_lab_cp_file_b
except AttributeError:
    self.tc_lab_cp_file_b = "/tmp/gnlmpf2"

try:
    self.tc_ub_ubi_prep_partname
except AttributeError:
    self.tc_ub_ubi_prep_partname = "ubi"

try:
    self.tc_ub_ubi_prep_offset
except AttributeError:
    self.tc_ub_ubi_prep_offset = "none"

try:
    self.tc_ub_ubi_load_addr
except AttributeError:
    self.tc_ub_ubi_load_addr = "14000000"

try:
    self.tc_ub_ubi_load_name
except AttributeError:
    self.tc_ub_ubi_load_name = "kernel"

try:
    self.tc_ub_ubi_create_vol_name
except AttributeError:
    self.tc_ub_ubi_create_vol_name = self.tc_ub_ubi_load_name

try:
    self.tc_ub_ubi_create_vol_sz
except AttributeError:
    self.tc_ub_ubi_create_vol_sz = "600000"

try:
    self.tc_ub_ubi_write_len
except AttributeError:
    self.tc_ub_ubi_write_len = '0xc00000'

try:
    self.tc_ub_ubi_write_addr
except AttributeError:
    self.tc_ub_ubi_write_addr = self.tc_ub_ubi_load_addr

try:
    self.tc_ub_ubi_write_vol_name
except AttributeError:
    self.tc_ub_ubi_write_vol_name = self.tc_ub_ubi_create_vol_name

try:
    self.tc_ub_ubifs_volume_name
except AttributeError:
    self.tc_ub_ubifs_volume_name = 'ubi:rootfs'

try:
    self.tc_ub_ubifs_ls_dir
except AttributeError:
    self.tc_ub_ubifs_ls_dir = '/'

try:
    self.tc_lx_gpio_nr
except AttributeError:
    self.tc_lx_gpio_nr = '69'

try:
    self.tc_lx_gpio_dir
except AttributeError:
    self.tc_lx_gpio_dir = 'out'

try:
    self.tc_lx_gpio_val
except AttributeError:
    self.tc_lx_gpio_val = '1'

try:
    self.tc_lx_eeprom_file
except AttributeError:
    self.tc_lx_eeprom_file = '/sys/class/i2c-dev/i2c-0/device/0-0050/eeprom'

try:
    self.tc_lx_eeprom_tmp_dir
except AttributeError:
    self.tc_lx_eeprom_tmp_dir = "/tmp/"

#has the eeprom a wp gpio
try:
    self.tc_lx_eeprom_wp_gpio
except AttributeError:
    self.tc_lx_eeprom_wp_gpio = 'none'

#with which value is the eeprom wp
try:
    self.tc_lx_eeprom_wp_val
except AttributeError:
    self.tc_lx_eeprom_wp_val = "0"

#size of the eeprom
#ToDo get this from linux
try:
    self.tc_lx_eeprom_wp_sz
except AttributeError:
    self.tc_lx_eeprom_wp_sz = "4096"

try:
    self.tc_lx_eeprom_wp_obs
except AttributeError:
    self.tc_lx_eeprom_wp_obs = "32"

try:
    self.tc_lx_eeprom_wp_wc
except AttributeError:
    self.tc_lx_eeprom_wp_wc = "128"

try:
    self.tc_lx_cpufreq_frequences
except AttributeError:
    self.tc_lx_cpufreq_frequences = ['294']

try:
    self.tc_lx_check_usb_authorized
except AttributeError:
    self.tc_lx_check_usb_authorized = 'usb 1-1'

try:
    self.tc_workfd_work_dir
except AttributeError:
    self.tc_workfd_work_dir = "/work/tbot"

try:
    self.tc_workfd_check_if_file_exists_name
except AttributeError:
    self.tc_workfd_check_if_file_exists_name = "bonnie++-1.03e.tgz"

try:
    self.tc_workfd_check_if_dir_exists_name
except AttributeError:
    self.tc_workfd_check_if_dir_exists_name = "mtd-utils"

try:
    self.tc_lx_dmesg_grep_name
except AttributeError:
    self.tc_lx_dmesg_grep_name = "zigbee"

try:
    self.tc_lx_readreg_addr
except AttributeError:
    self.tc_lx_readreg_addr = "0x44e10800"

try:
    self.tc_lx_readreg_mask
except AttributeError:
    self.tc_lx_readreg_mask = "0x000000ff"

try:
    self.tc_lx_readreg_type
except AttributeError:
    self.tc_lx_readreg_type = "w"

try:
    self.tc_lx_readreg_value
except AttributeError:
    self.tc_lx_readreg_value = "0x31"

try:
    self.tc_lx_create_reg_file_name
except AttributeError:
    self.tc_lx_create_reg_file_name = "pinmux.reg"

try:
    self.tc_lx_create_reg_file_start
except AttributeError:
    self.tc_lx_create_reg_file_start = "0x44e10800"

try:
    self.tc_lx_create_reg_file_stop
except AttributeError:
    self.tc_lx_create_reg_file_stop = "0x44e10a34"

try:
    self.tc_lx_regulator_nrs
except AttributeError:
    self.tc_lx_regulator_nrs = ['0 regulator-dummy -', '1 hsusb1_vbus 5000000',
		'2 vmmc 3300000', '3 pbias_mmc_omap2430 3000000',
		'4 DCDC1 1200000', '5 DCDC2 3300000', '6 DCDC3 1800000',
		'7 LDO1 1800000', '8 LDO2 3300000']

try:
    self.board_has_debugger
except AttributeError:
    self.board_has_debugger = 0

try:
    self.lab_bdi_upd_uboot_bdi_cmd
except AttributeError:
    self.lab_bdi_upd_uboot_bdi_cmd = 'telnet bdi6'

try:
    self.lab_bdi_upd_uboot_bdi_prompt
except AttributeError:
    self.lab_bdi_upd_uboot_bdi_prompt = 'BDI>'

try:
    self.lab_bdi_upd_uboot_bdi_era
except AttributeError:
    self.lab_bdi_upd_uboot_bdi_era = 'era'

try:
    self.lab_bdi_upd_uboot_bdi_prog
except AttributeError:
    self.lab_bdi_upd_uboot_bdi_prog = 'prog 0xfc000000'

try:
    self.lab_bdi_upd_uboot_bdi_file
except AttributeError:
    self.lab_bdi_upd_uboot_bdi_file = '/tftpboot/tqm5200s/tbot/u-boot.bin'

try:
    self.lab_bdi_upd_uboot_bdi_run
except AttributeError:
    self.lab_bdi_upd_uboot_bdi_run = 'res run'

try:
    self.board_git_bisect_get_source_tc
except AttributeError:
    self.board_git_bisect_get_source_tc = 'tc_lab_get_uboot_source.py'

try:
    self.board_git_bisect_call_tc
except AttributeError:
    self.board_git_bisect_call_tc = 'tc_board_tqm5200s_ub_comp_install.py'

try:
    self.board_git_bisect_good_commit
except AttributeError:
    self.board_git_bisect_good_commit = 'f9860cf'

try:
    self.tc_lab_rm_dir
except AttributeError:
    self.tc_lab_rm_dir =  self.tc_lab_source_dir + '/u-boot-tqm5200'

try:
    self.tc_lab_apply_patches_dir
except AttributeError:
    self.tc_lab_apply_patches_dir =  'none'

try:
    self.tc_ubi_cmd_path
except AttributeError:
    self.tc_ubi_cmd_path = "/work/tbot/mtd-utils"

try:
    self.tc_ubi_mtd_dev
except AttributeError:
    self.tc_ubi_mtd_dev = "/dev/mtd4"

try:
    self.tc_ubi_ubi_dev
except AttributeError:
    self.tc_ubi_ubi_dev = "/dev/ubi0"

try:
    self.tc_ubi_min_io_size
except AttributeError:
    self.tc_ubi_min_io_size = "1024"

try:
    self.tc_ubi_max_leb_cnt
except AttributeError:
    self.tc_ubi_max_leb_cnt = "100"

try:
    self.tc_ubi_leb_size
except AttributeError:
    self.tc_ubi_leb_size = "126976"

try:
    self.tc_ubi_vid_hdr_offset
except AttributeError:
    self.tc_ubi_vid_hdr_offset = "default"

try:
    self.tc_lx_ubi_format_filename
except AttributeError:
    self.tc_lx_ubi_format_filename = "/home/hs/ccu1/ecl-image-usbc.ubi"

try:
    self.tc_workfd_apply_patchwork_patches_list
except AttributeError:
    self.tc_workfd_apply_patchwork_patches_list = []

try:
    self.tc_workfd_apply_patchwork_patches_list_hand
except AttributeError:
    self.tc_workfd_apply_patchwork_patches_list_hand = []

try:
    self.tc_workfd_apply_patchwork_patches_blacklist
except AttributeError:
    self.tc_workfd_apply_patchwork_patches_blacklist = []

try:
    self.tc_workfd_apply_patchwork_patches_checkpatch_cmd
except AttributeError:
    self.tc_workfd_apply_patchwork_patches_checkpatch_cmd = 'none'

try:
    self.tc_workfd_rm_file_name
except AttributeError:
    self.tc_workfd_rm_file_name = 'none'

try:
    self.tc_workfd_cd_name
except AttributeError:
    self.tc_workfd_cd_name = 'none'

try:
    self.tc_lab_get_linux_source_git_repo
except AttributeError:
    self.tc_lab_get_linux_source_git_repo = "/home/git/linux.git"

try:
    self.tc_lab_get_linux_source_git_repo_user
except AttributeError:
    self.tc_lab_get_linux_source_git_repo_user = 'anonymous'

try:
    self.tc_lab_get_linux_source_git_branch
except AttributeError:
    self.tc_lab_get_linux_source_git_branch = "master"

try:
    self.tc_lab_get_linux_source_git_reference
except AttributeError:
    self.tc_lab_get_linux_source_git_reference = 'none'

try:
    self.tc_workfd_apply_local_patches_dir
except AttributeError:
    self.tc_workfd_apply_local_patches_dir = "/work/hs/tbot/patches/mcx_linux_ml_patches"

try:
    self.tc_workfd_apply_local_patches_checkpatch_cmd
except AttributeError:
    self.tc_workfd_apply_local_patches_checkpatch_cmd = 'none'

try:
    self.tc_workfd_apply_local_patches_checkpatch_cmd_strict
except AttributeError:
    self.tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"

try:
    self.tc_workfd_get_list_of_files_mask
except AttributeError:
    self.tc_workfd_get_list_of_files_mask = '*'

try:
    self.tc_workfd_compile_linux_boardname
except AttributeError:
    self.tc_workfd_compile_linux_boardname = self.boardname

try:
    self.tc_workfd_compile_linux_clean
except AttributeError:
    self.tc_workfd_compile_linux_clean = 'yes'

try:
    self.tc_workfd_compile_linux_modules
except AttributeError:
    self.tc_workfd_compile_linux_modules = 'none'

try:
    self.tc_workfd_compile_linux_modules_path
except AttributeError:
    self.tc_workfd_compile_linux_modules_path = 'none'

try:
    self.tc_workfd_compile_linux_dt_name
except AttributeError:
    self.tc_workfd_compile_linux_dt_name = 'none'

try:
    self.tc_workfd_compile_linux_append_dt
except AttributeError:
    self.tc_workfd_compile_linux_append_dt = 'no'

try:
    self.tc_workfd_compile_linux_load_addr
except AttributeError:
    self.tc_workfd_compile_linux_load_addr = 'no'

try:
    self.tc_workfd_compile_linux_fit_its_file
except AttributeError:
    self.tc_workfd_compile_linux_fit_its_file = 'no'

try:
    self.tc_workfd_compile_linux_mkimage
except AttributeError:
    self.tc_workfd_compile_linux_mkimage = '/home/hs/i2c/u-boot/tools/mkimage'

try:
   self.workfd_get_patchwork_number_user
except AttributeError:
   self.workfd_get_patchwork_number_user = 'hs'

try:
    self.tc_workfd_connect_with_kermit_ssh
except AttributeError:
    self.tc_workfd_connect_with_kermit_ssh = "none"

try:
    self.kermit_line
except AttributeError:
    self.kermit_line = '/dev/ttyUSB0'

try:
    self.kermit_speed
except AttributeError:
    self.kermit_speed = '115200'

try:
    self.tc_ub_tftp_file_addr
except AttributeError:
    self.tc_ub_tftp_file_addr = self.ub_load_board_env_addr

try:
    self.tc_ub_tftp_path
except AttributeError:
    self.tc_ub_tftp_path = '/tftpboot/' + self.tftpboardname + '/' + self.ub_load_board_env_subdir

try:
    self.tc_ub_tftp_file_name
except AttributeError:
    self.tc_ub_tftp_file_name = self.tc_ub_tftp_path + '/env.txt'

try:
    self.tc_ub_boot_linux_retry
except AttributeError:
    self.tc_ub_boot_linux_retry = 30

try:
    self.tc_lab_denx_power_tc
except AttributeError:
    self.tc_lab_denx_power_tc = 'tc_lab_denx_power.py'

try:
    self.tc_lab_denx_get_power_state_tc
except AttributeError:
    self.tc_lab_denx_get_power_state_tc = 'tc_lab_denx_get_power_state.py'

try:
    self.tc_lab_denx_connect_to_board_tc
except AttributeError:
    self.tc_lab_denx_connect_to_board_tc = 'tc_lab_denx_connect_to_board.py'

try:
    self.tc_ub_memory_ram_ws_base
except AttributeError:
    self.tc_ub_memory_ram_ws_base = '0x100000'

try:
    self.tc_ub_memory_ram_ws_base_alt
except AttributeError:
    self.tc_ub_memory_ram_ws_base_alt = '0x200000'

try:
    self.tc_lx_trigger_wdt_cmd
except AttributeError:
    self.tc_lx_trigger_wdt_cmd = '/home/hs/wdt &'
