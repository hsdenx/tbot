# tbot configuration
# for the wivue2 board
boardname = 'wivue2'
debug=False
debugstatus=True
wdt_timeout = '9000'

uboot_prompt = 'U-Boot> '
linux_prompt = '# '

#create_dot = 'yes'
#create_statistic = 'yes'
#create_dashboard = 'yes'
#create_html_log = 'yes'

# set connect testcase (as it is with kermit, not with connect)
tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
tc_workfd_connect_with_kermit_rlogin = 'rlogin ts3 wivue2'
tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'

# variables used in testcases
tc_workfd_work_dir = '/work/hs/tbot'
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x21000000'
tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_compile_uboot_export_path = '/home/hs/dtc'

tc_workfd_apply_local_patches_dir = "/work/hs/tbot/patches/wivue2_uboot_patches"
tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"
tc_workfd_apply_local_patches_checkpatch_cmd = 'scripts/checkpatch.pl'
uboot_get_parameter_file_list = ['.config', 'include/configs/wivue2.h', 'arch/arm/mach-at91/include/mach/at91sam9260.h']
