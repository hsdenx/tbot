# tbot configuration
# for the taurus board
boardname = 'taurus'
boardlabname = 'at91_taurus'
boardlabpowername = 'at91_taurus'
tftpboardname = 'at91_taurus'
debug=False
debugstatus=True
loglevel='INFO'
wdt_timeout = '900'

uboot_prompt = 'U-Boot> '
linux_prompt = 'ttbott> '

create_dot = 'yes'
create_statistic = 'yes'
create_dashboard = 'yes'
create_html_log = 'yes'

# set connect testcase (as it is with kermit, not with connect)
tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
tc_workfd_connect_with_kermit_rlogin = 'rlogin ts3 at91_taurus'
tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'

# variables used in testcases
tc_workfd_work_dir = '/work/hs/tbot'
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x21000000'
tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_compile_uboot_export_path = '/home/hs/dtc'

tc_workfd_set_toolchain_arch = 'arm'
tc_workfd_set_toolchain_t_p = {
'arm' : '/home/hs/toolchain/linaro/gcc-linaro-7.2.1-2017.11-i686_arm-linux-gnueabi/bin',
}

tc_workfd_set_toolchain_cr_co = {
'arm' : 'arm-linux-gnueabi-',
}

tc_workfd_apply_local_patches_dir = "/work/hs/tbot/patches/taurus_uboot_patches"
tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"
tc_workfd_apply_local_patches_checkpatch_cmd = 'scripts/checkpatch.pl'
uboot_get_parameter_file_list = ['.config', 'include/configs/taurus.h', 'arch/arm/mach-at91/include/mach/at91sam9260.h']

# set DFU variables for tc_ub_dfu_random.py
tc_ub_dfu_rand_size = '4194304'
tc_ub_dfu_rand_ubcmd = 'dfu 0 nand 0'
tc_ub_dfu_dfu_util_alt_setting = 'Linux_SetB'
tc_ub_dfu_dfu_util_path = "none"
tc_ub_dfu_dfu_util_ssh = "root@ts8"

tc_demo_compile_install_test_files = ['u-boot.bin', 'boot.bin',
	'System.map', 'spl/u-boot-spl.bin', 'spl/u-boot-spl.map']
