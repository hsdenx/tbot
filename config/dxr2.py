# tbot configuration
# for the dxr2 board
boardname = 'etamin'
boardlabname = 'dxr2'
boardlabpowername = 'dxr2'
tftpboardname = 'dxr2'
loglevel='INFO'
wdt_timeout = '5000'

# set connect testcase (as it is with kermit, not with connect)
# tc_workfd_connect_with_kermit_ssh = 'hs@lena'
tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
tc_workfd_connect_with_kermit_rlogin = 'rlogin lena dxr2'
tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'

uboot_prompt = 'U-Boot# '
linux_prompt = 'ttbott> '

create_dot = 'yes'
create_statistic = 'yes'
create_dashboard = 'yes'
create_html_log = 'yes'

# variables used in testcases
# board_has_debugger = 'yes'
# lab_bdi_upd_uboot_bdi_prompt = 'AM335x-EVM>'
# lab_bdi_upd_uboot_bdi_cmd = 'telnet bdi19'

tc_workfd_work_dir = '/work/hs/tbot'
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x80100000'
tc_lab_get_uboot_source_git_repo = "/home/hs/zug/u-boot-ccp"
tc_lab_get_uboot_source_git_repo = "/home/hs/zug/u-boot"
tc_lab_get_uboot_source_git_branch = "20160212-denx-uboot-etamin-devel"
tc_lab_get_uboot_source_git_branch = "denx-uboot-etamin-devel"
tc_lab_get_uboot_source_git_branch = "20160422-dm"
tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_compile_uboot_export_path = '/home/hs/dtc'
tc_workfd_apply_local_patches_dir = "/work/hs/tbot/patches/dxr2_uboot_patches"
tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"
tc_workfd_apply_local_patches_checkpatch_cmd = 'scripts/checkpatch.pl'

# uboot DUTS variables
uboot_get_parameter_file_list = ['.config', 'include/configs/etamin.h', 'include/configs/siemens-am33x-common.h']
tc_ub_i2c_help_with_bus = 'yes'

# uboot ubi testcase variables
tc_ub_ubi_prep_offset = '4096'
tc_ub_ubi_prep_partname = 'rootfs'
tc_ub_ubi_load_name = 'rootfs_a'
tc_ub_ubi_create_vol_sz = 'a000000'

tc_workfd_generate_random_file_name = '/tftpboot/dxr2/tbot/ubi_random'
tc_workfd_generate_random_file_length = '2M'
# fix nand params
tc_ubi_min_io_size = '4096'
tc_ubi_max_leb_cnt = '5000'
tc_ubi_leb_size = '516096'
tc_ub_ubi_write_addr = '80100000'
tc_ub_ubi_read_addr = '85000000'

# set DFU variables for tc_ub_dfu_random.py
tc_ub_dfu_rand_size = '31457280'
tc_ub_dfu_rand_ubcmd = 'dfu 0 mtd 0'
tc_ub_dfu_dfu_util_alt_setting = 'over_border'
tc_ub_dfu_dfu_util_path = "none"
tc_ub_dfu_dfu_util_ssh = "root@ts8"

# must be the same as the rootfs nfs path
tc_board_dxr2_ub_ubi_rootfs_randomfile_path = '/opt/eldk-5.5/armv7a-hf/rootfs-sato-sdk/home/hs/ubi_random'

# tc_workfd_get_patchwork_number_list_order = '-date'
# workfd_get_patchwork_number_user = 'all'

# linux testcases
tc_lab_get_linux_source_git_repo = 'https://hsdenx@github.com/siemens/linux-ccp.git'
tc_lab_get_linux_source_git_repo_user = 'hsdenx'
tc_lab_get_linux_source_git_branch = 'ccp-v3.18.10-draco'
tc_lab_get_linux_source_git_branch = 'denx-20160113-ccp-v3.18.10-draco-devel'
tc_lab_get_linux_source_git_branch = 'denx-v4.4-stable-draco-devel'
tc_lab_get_linux_source_git_reference = '/home/git/linux.git'
tc_lab_apply_patches_dir = 'none'
tc_workfd_apply_local_patches_dir = '/work/hs/tbot/patches/dxr2_linux_patches'

tc_lab_get_linux_source_git_repo = '/home/hs/zug/dxr2/linux-stable'
tc_lab_get_linux_source_git_repo_user = 'hsdenx'
tc_lab_get_linux_source_git_branch = 'denx-v4.4-stable-draco-devel'
tc_lab_get_linux_source_git_reference = '/home/git/linux.git'
tc_lab_apply_patches_dir = 'none'
tc_workfd_apply_local_patches_dir = '/work/hs/tbot/patches/dxr2_linux_patches'

tc_lx_create_reg_file_name = 'src/files/dxr2_etamin_pinmux.reg'
tc_lx_create_reg_file_start = '0x44e10000'
tc_lx_create_reg_file_stop = '0x44e11444'
tc_lx_readreg_mask = 0xffffffff

tc_ubi_mtd_dev = '/dev/mtd13'
tc_ubi_vid_hdr_offset = '4096'
