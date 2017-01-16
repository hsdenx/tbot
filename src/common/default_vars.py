# This file contains default values for all
# variables testcases use ...

debug = False
debugstatus = False
uboot_strings = ['Autobooting in', 'noautoboot',  'autoboot', 'EOF', 'RomBOOT']
uboot_autoboot_key = ''
term_line_length = '200'
wdt_timeout = '120' # wdt timeout after 2 minutes
state_linux_timeout = 4
labsshprompt = '$ '
tc_return = True
tc_workfd_check_if_cmd_exist_cmdname = 'none'
setenv_name = 'tralala'
setenv_value = 'hulalahups'
tc_ub_boot_linux_load_env = 1
tc_lx_mount_dev = '/dev/sda1'
tc_lx_mount_fs_type = 'ext4'
tc_lx_mount_dir = '/home/hs/mnt'
tc_lx_bonnie_dev = tc_lx_mount_dev
tc_lx_bonnie_sz = '968'
ub_load_board_env_addr = '0x81000000'
ub_load_board_env_subdir = 'tbot'
ub_boot_linux_cmd = 'run tbot_boot_linux'
tc_lab_compile_uboot_boardname = 'config.boardname'
tc_lab_compile_uboot_makeoptions = '-j4'
do_connect_to_board = True
tc_lab_compile_uboot_export_path = 'none'
tftpboardname = 'config.boardname'
boardlabname = 'config.boardname'
boardlabpowername = 'config.boardname'
tc_ub_dfu_dfu_util_path = "/home/hs/zug/dfu-util"
tc_ub_dfu_dfu_util_alt_setting = "Linux"
tc_lab_source_dir = "/work/hs/tbot"
tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_toolchain_rev = "5.4"
tc_lab_toolchain_name = "armv5te"
tc_ub_ubi_load_name = "kernel"
tc_ub_ubi_prep_partname = "ubi"
tc_ub_ubi_prep_offset = "none"
tc_ub_ubi_load_addr = "14000000"
tc_ub_ubi_create_vol_name = 'config.tc_ub_ubi_load_name'
tc_ub_ubi_create_vol_sz = "600000"
tc_ub_ubi_write_len = '0xc00000'
tc_ub_ubi_write_addr = 'config.tc_ub_ubi_load_addr'
tc_ub_ubi_write_vol_name = 'config.tc_ub_ubi_create_vol_name'
tc_ub_ubifs_volume_name = 'ubi:rootfs'
tc_ub_ubifs_ls_dir = '/'
tc_lx_gpio_nr = '69'
tc_lx_gpio_dir = 'out'
tc_lx_gpio_val = '1'
tc_lx_eeprom_file = '/sys/class/i2c-dev/i2c-0/device/0-0050/eeprom'
tc_lx_eeprom_tmp_dir = 'config.lab_tmp_dir'
tc_lx_eeprom_wp_gpio = 'none'
tc_lx_eeprom_wp_val = "0"
tc_lx_eeprom_wp_sz = "4096"
tc_lx_eeprom_wp_obs = "32"
tc_lx_eeprom_wp_wc = "128"
tc_lx_cpufreq_frequences = ['294']
tc_lx_check_usb_authorized = 'usb 1-1'
tc_workfd_work_dir = "/work/tbot"
tc_workfd_check_if_file_exists_name = "bonnie++-1.03e.tgz"
tc_workfd_check_if_dir_exists_name = "mtd-utils"
tc_lx_dmesg_grep_name = "zigbee"
tc_lx_readreg_mask = "0x000000ff"
tc_lx_readreg_type = "w"
tc_lx_create_reg_file_name = "pinmux.reg"
tc_lx_create_reg_file_start = "0x44e10800"
tc_lx_create_reg_file_stop = "0x44e10a34"
tc_lx_regulator_nrs = ['0 regulator-dummy -', '1 hsusb1_vbus 5000000',
		'2 vmmc 3300000', '3 pbias_mmc_omap2430 3000000',
		'4 DCDC1 1200000', '5 DCDC2 3300000', '6 DCDC3 1800000',
		'7 LDO1 1800000', '8 LDO2 3300000']
board_has_debugger = 0
lab_bdi_upd_uboot_bdi_cmd = 'telnet bdi6'
lab_bdi_upd_uboot_bdi_prompt = 'BDI>'
lab_bdi_upd_uboot_bdi_era = 'era'
lab_bdi_upd_uboot_bdi_prog = 'prog 0xfc000000'
lab_bdi_upd_uboot_bdi_file = '/tftpboot/tqm5200s/tbot/u-boot.bin'
lab_bdi_upd_uboot_bdi_run = [{'cmd':'res run', 'val':'resetting target passed'}]
board_git_bisect_get_source_tc = 'tc_lab_get_uboot_source.py'
board_git_bisect_call_tc = 'tc_board_tqm5200s_ub_comp_install.py'
board_git_bisect_good_commit = 'f9860cf'
board_git_bisect_patches = 'none'
tc_lab_apply_patches_dir =  'none'
tc_ubi_cmd_path = "/work/tbot/mtd-utils"
tc_ubi_mtd_dev = "/dev/mtd4"
tc_ubi_ubi_dev = "/dev/ubi0"
tc_ubi_min_io_size = "1024"
tc_ubi_max_leb_cnt = "100"
tc_ubi_leb_size = "126976"
tc_ubi_vid_hdr_offset = "default"
tc_lx_ubi_format_filename = "/home/hs/ccu1/ecl-image-usbc.ubi"
tc_workfd_apply_patchwork_patches_list = []
tc_workfd_apply_patchwork_patches_list_hand = []
tc_workfd_apply_patchwork_patches_blacklist = []
tc_workfd_apply_patchwork_patches_checkpatch_cmd = 'none'
tc_workfd_apply_patchwork_patches_eof = 'yes'
tc_workfd_get_patchwork_number_list_order = '-delegate'
tc_workfd_rm_file_name = 'none'
tc_workfd_cd_name = 'none'
tc_lab_get_linux_source_git_repo = "/home/git/linux.git"
tc_lab_get_linux_source_git_repo_user = 'anonymous'
tc_lab_get_linux_source_git_branch = "master"
tc_lab_get_linux_source_git_reference = 'none'
tc_workfd_apply_local_patches_dir = 'none'
tc_workfd_apply_local_patches_checkpatch_cmd = 'none'
tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"
tc_workfd_get_list_of_files_mask = '*'
tc_workfd_compile_linux_boardname = 'config.boardname'
tc_workfd_compile_linux_clean = 'yes'
tc_workfd_compile_linux_modules = 'none'
tc_workfd_compile_linux_modules_path = 'none'
tc_workfd_compile_linux_dt_name = 'none'
tc_workfd_compile_linux_append_dt = 'no'
tc_workfd_compile_linux_load_addr = 'no'
tc_workfd_compile_linux_make_target = 'uImage'
tc_workfd_compile_linux_fit_its_file = 'no'
tc_workfd_compile_linux_fit_file = 'no'
tc_workfd_compile_linux_mkimage = '/home/hs/i2c/u-boot/tools/mkimage'
tc_workfd_compile_linux_makeoptions = ''
workfd_get_patchwork_number_user = 'hs'
workfd_get_patchwork_number_list_order = '-delegate'
tc_workfd_connect_with_kermit_ssh = "none"
tc_workfd_connect_with_kermit_rlogin = "none"
kermit_line = '/dev/ttyUSB0'
kermit_speed = '115200'
tc_ub_tftp_file_addr = 'config.ub_load_board_env_addr'
tc_lab_denx_power_tc = 'tc_lab_denx_power.py'
tc_lab_denx_get_power_state_tc = 'tc_lab_denx_get_power_state.py'
tc_lab_denx_connect_to_board_tc = 'tc_lab_denx_connect_to_board.py'
tc_lab_denx_disconnect_from_board_tc = 'tc_lab_denx_disconnect_from_board.py'
tc_ub_memory_ram_ws_base = 'undef'
tc_ub_memory_ram_ws_base_alt = 'undef'
tc_ub_memory_ram_big = 'undef'
tc_lx_trigger_wdt_cmd = '/home/hs/wdt &'
tc_workfd_create_ubi_rootfs_path = '/opt/eldk-5.4/armv7a-hf/rootfs-minimal-mtdutils'
tc_workfd_create_ubi_rootfs_target = '/tftpboot/dxr2/tbot/rootfs-minimal.ubifs'
tc_ub_i2c_help_with_bus = 'no'
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
workfd_ssh_cmd_prompt = '$'
linux_prompt_default = 'root@generic-armv7a-hf:~# '
labprompt = 'config.linux_prompt'
linux_user = 'root'
create_dot = 'no'
create_statistic = 'no'
create_dashboard = 'no'
create_webpatch = 'no'
create_html_log = 'no'
create_documentation = 'no'
event_documentation_strip_list = []
tc_ub_test_py_hook_script_path = '$HOME/testframework/hook-scripts'
switch_su_board = 'lab'
tc_workfd_can_ssh = 'no'
tc_workfd_can_ssh_prompt = '$'
tc_workfd_can_su = 'no'
tc_workfd_can_dev = 'can0'
tc_workfd_can_bitrate = '500000'
tc_workfd_can_iproute_dir = '/home/hs/iproute2'
tc_workfd_can_util_dir = '/home/hs/can-utils'
tc_workfd_hdparm_path = '/home/hs/shc/hdparm-9.50/'
tc_workfd_hdparm_dev = '/dev/mmcblk1'
tc_workfd_hdparm_min = '12.0'
tc_lab_git_clone_source_git_repo = 'git://git.yoctoproject.org/poky.git'
tc_lab_git_clone_source_git_branch = 'morty'
tc_lab_git_clone_source_git_commit_id = '73454473d7c286c41ee697f74052fed03c79f9f5'
tc_lab_git_clone_apply_patches_dir = 'none'
tc_lab_git_clone_apply_patches_git_am_dir = '/work/hs/ssi/patches/20161220/morty'
tc_lab_git_clone_source_git_reference = 'none'
tc_lab_git_clone_source_git_repo_user = ''
tc_lab_git_clone_source_git_repo_name = 'none'
tc_workfd_get_yocto_source_layers = [
['git://git.openembedded.org/meta-openembedded', 'morty', '659d9d3f52bad33d7aa1c63e25681d193416d76e', 'none', 'none', 'none', '', 'meta-openembedded'],
['https://github.com/meta-qt5/meta-qt5.git', 'morty', '9aa870eecf6dc7a87678393bd55b97e21033ab48', 'none', '/work/hs/ssi/patches/20161220/qt5', 'none', '', 'meta-qt5'],
['https://github.com/sbabic/meta-swupdate.git', 'master', 'b3abfa78d04b88b88bcef6f5be9f2adff1293544', 'none', 'none', 'none', '', 'meta-swupdate'],
['git@gitlab.denx.de:ssi/meta-cuby.git', '20161220', 'none', 'none', 'none', 'none', '', 'meta-cuby'],
]
tc_workfd_get_yocto_source_conf_dl_dir = 'none'
tc_workfd_get_yocto_source_conf_sstate_dir = 'none'
