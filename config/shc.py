# tbot configuration
# for the shc board
boardname = 'shc'
debug=False
debugstatus=True
loglevel='INFO'

wdt_timeout = '3600'

uboot_prompt = 'U-Boot# '
linux_prompt = 'ttbott> '

create_dot = 'yes'
create_statistic = 'yes'
create_dashboard = 'yes'
create_html_log = 'yes'

# set connect testcase (as it is with kermit, not with connect)
tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
tc_workfd_connect_with_kermit_rlogin = 'rlogin metis shc'
tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'

# variables used in testcases
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x81000000'

tc_lab_get_uboot_source_git_repo = '/home/hs/bosch/u-boot-secure/u-boot.git'
tc_lab_get_uboot_source_git_branch = 'shc-devel-20160620'

tc_lab_toolchain_rev = '5.4'
tc_lab_toolchain_name = 'armv7a'

tc_lab_compile_uboot_boardname = 'am335x_shc'
tc_board_shc_upd_ub_typ = 'eMMC'
# tc_board_shc_upd_ub_typ = 'SD'

tc_ub_create_reg_file_name = 'src/files/shc_ub_pinmux.reg'
tc_ub_create_reg_file_comment = 'pinmux'
tc_ub_create_reg_file_start = '44e10800'
tc_ub_create_reg_file_stop = '44e10a34'
tc_ub_readreg_mask = '0xffffffff'
tc_ub_create_reg_file_mode = 'w+'
tc_ub_readreg_type = 'l'

# for DUTS
uboot_get_parameter_file_list = ['.config', 'include/configs/am335x_shc.h', 'include/configs/ti_armv7_common.h']
tc_ub_i2c_help_with_bus = 'yes'

# linux testcases
tc_lx_create_reg_file_name = 'src/files/shc_pinmux.reg'

linux_prompt_default = 'root@generic-armv5te:~# '

# Mainline kernel
tc_lab_get_linux_source_git_repo = '/home/hs/bosch/linux'
tc_lab_get_linux_source_git_repo_user = 'hsdenx'
tc_lab_get_linux_source_git_branch = 'shc_20160216'
tc_lab_get_linux_source_git_reference = '/home/git/linux.git'
tc_lab_apply_patches_dir = 'none'
tc_workfd_apply_local_patches_dir = 'none'

# Stable kernel 4.1
tc_lab_get_linux_source_git_repo = '/home/hs/bosch/linux-stable'
tc_lab_get_linux_source_git_repo_user = 'hsdenx'
tc_lab_get_linux_source_git_branch = '20160216-linux-v4.1-devel'
tc_lab_get_linux_source_git_reference = '/home/git/linux.git'
tc_lab_apply_patches_dir = 'none'
tc_workfd_apply_local_patches_dir = 'none'

# Stable kernel 4.4
tc_lab_get_linux_source_git_repo = '/home/hs/bosch/linux-stable'
tc_lab_get_linux_source_git_repo_user = 'hsdenx'
tc_lab_get_linux_source_git_branch = 'shc-linux-4.4.y-devel'
tc_lab_get_linux_source_git_reference = '/home/git/linux.git'
tc_lab_apply_patches_dir = 'none'
tc_workfd_apply_local_patches_dir = 'none'
tc_workfd_compile_linux_makeoptions = '-j8'
