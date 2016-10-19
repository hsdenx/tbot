# tbot configuration
# for the dxr2 board
# special usecase, check all U-Boot patches
# at patchwork
boardname = 'etamin'
boardlabname = 'dxr2'
boardlabpowername = 'dxr2'
tftpboardname = 'dxr2'
debug=False
debugstatus=True
loglevel='INFO'
wdt_timeout = '5000'

# set connect testcase (as it is with kermit, not with connect)
tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
# tc_workfd_connect_with_kermit_ssh = 'hs@lena'
tc_workfd_connect_with_kermit_rlogin = 'rlogin lena dxr2'
tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'

uboot_prompt = 'U-Boot# '
linux_prompt = 'ttbott> '

# variables used in testcases
board_has_debugger = 1
lab_bdi_upd_uboot_bdi_prompt = 'AM335x-EVM>'
lab_bdi_upd_uboot_bdi_cmd = 'telnet bdi19'

tc_workfd_work_dir = '/work/hs/tbot'
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x80100000'
tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_compile_uboot_export_path = '/home/hs/dtc'
tc_workfd_apply_local_patches_dir = "/work/hs/tbot/patches/dxr2_uboot_patches"
tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"
tc_workfd_apply_local_patches_checkpatch_cmd = 'scripts/checkpatch.pl'

tc_workfd_get_patchwork_number_list_order = 'date'
workfd_get_patchwork_number_user = 'all'
tc_workfd_apply_patchwork_patches_eof = 'no'
