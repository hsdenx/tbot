# tbot configuration
# for the thuban board
# board is called in mainline thuban, but we have
# called it in the VLAB dxr2 ...
#
boardname = 'thuban'
boardlabname = 'dxr2'
boardlabpowername = 'dxr2'
tftpboardname = 'dxr2'
debug=False
debugstatus=True
loglevel='INFO'
wdt_timeout = '900'

uboot_prompt = 'U-Boot# '
linux_prompt = 'ttbott> '

create_dot = 'yes'
create_statistic = 'yes'
create_dashboard = 'yes'
create_html_log = 'yes'
create_junit = 'yes'

# set connect testcase (as it is with kermit, not with connect)
tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
workfd_ssh_do_first = 'no'
tc_workfd_connect_with_kermit_ssh = 'hs@lena'
tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'

# variables used in testcases
tc_workfd_work_dir = '/work/hs/tbot'
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x80000000'
ub_load_board_env_subdir = '20171213'
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

tc_workfd_apply_local_patches_dir = "/work/hs/tbot/patches/thuban_uboot_patches"
tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"
tc_workfd_apply_local_patches_checkpatch_cmd = 'scripts/checkpatch.pl'

tc_demo_compile_install_test_files = ['u-boot.bin', 'MLO', 'u-boot.img',
	'System.map', 'spl/u-boot-spl.bin', 'spl/u-boot-spl.map']
tc_demo_compile_install_test_ub_vers_file = 'u-boot.bin'
tc_demo_compile_install_test_spl_vers_file = 'MLO'

tc_demo_compile_install_test_name = 'tc_board_thuban_test_uboot.py'

uboot_get_parameter_file_list = ['.config', 'include/configs/thuban.h', 'include/configs/siemens-am33x-common.h']

tc_ub_i2c_help_with_bus = 'yes'

# uboot ubi testcase variables
tc_ub_ubi_prep_offset = '2048'
tc_ub_ubi_prep_partname = 'rootfs'
tc_ub_ubi_load_name = 'rootfs_a'
tc_ub_ubi_create_vol_sz = 'a000000'

tc_workfd_generate_random_file_name = '/tftpboot/thuban/tbot/ubi_random'
tc_workfd_generate_random_file_length = '2M'

# fix nand params
#tc_ubi_min_io_size = '4096'
#tc_ubi_max_leb_cnt = '5000'
#tc_ubi_leb_size = '516096'
#tc_ub_ubi_write_addr = '80100000'
#tc_ub_ubi_read_addr = '85000000'

# set DFU variables for tc_ub_dfu_random.py
#tc_ub_dfu_rand_size = '31457280'
#tc_ub_dfu_rand_ubcmd = 'dfu 0 mtd 0'
#tc_ub_dfu_dfu_util_alt_setting = 'over_border'
#tc_ub_dfu_dfu_util_path = "none"
#tc_ub_dfu_dfu_util_ssh = "root@ts8"

# must be the same as the rootfs nfs path
tc_board_dxr2_ub_ubi_rootfs_randomfile_path = '/opt/eldk-5.5/armv7a-hf/rootfs-sato-sdk/home/hs/thuban/ubi_random'

# tc_workfd_get_patchwork_number_list_order = '-date'
# workfd_get_patchwork_number_user = 'all'
