# tbot configuration
# for the corvus board
# board is called in mainline corvus, but we have
# called it in the VLAB at91sam9g45 ...
#
boardname = 'corvus'
boardlabname = 'at91sam9g45'
boardlabpowername = 'at91sam9g45'
tftpboardname = 'at91sam9g45'
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
tc_workfd_connect_with_kermit_rlogin = 'rlogin ts3 at91sam9g45'
tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'

# variables used in testcases
tc_workfd_work_dir = '/work/hs/tbot'
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x72000000'
tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_compile_uboot_export_path = '/home/hs/dtc'

tc_workfd_apply_local_patches_dir = "/work/hs/tbot/patches/corvus_uboot_patches"
tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"
tc_workfd_apply_local_patches_checkpatch_cmd = 'scripts/checkpatch.pl'

uboot_get_parameter_file_list = ['.config', 'include/configs/corvus.h', 'arch/arm/mach-at91/include/mach/at91sam9g45.h']

# set DFU variables for tc_ub_dfu_random.py
tc_ub_dfu_rand_size = '262144'
tc_ub_dfu_rand_ubcmd = 'dfu 0 nand 0'
tc_ub_dfu_dfu_util_alt_setting = 'spare'
tc_ub_dfu_dfu_util_path = "none"
tc_ub_dfu_dfu_util_ssh = "root@ts8"
