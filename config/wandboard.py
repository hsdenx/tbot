# tbot configuration
# for the smartweb board
boardname = 'wandboard'
tftpboardname = 'wandboard_dl'
boardlabpowername = 'wandboard_dl'
debug = False
debugstatus = True

uboot_prompt = '=> '
linux_prompt = 'ttbott> '

create_dot = 'yes'
create_statistic = 'yes'
create_dashboard = 'yes'
create_html_log = 'yes'

# set connect testcase (as it is with kermit, not with connect)
tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
tc_workfd_connect_with_kermit_rlogin = 'rlogin ts3 wandboard_dl'
tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'

# Toolchain
tc_workfd_set_toolchain_arch = 'arm'
tc_workfd_set_toolchain_t_p = {
'arm' : '/opt/eldk-5.4/armv5te/sysroots/i686-eldk-linux/usr/bin/armv5te-linux-gnueabi',
}

tc_workfd_set_toolchain_cr_co = {
'arm' : 'arm-linux-gnueabi-',
}

# variables used in testcases
tc_ub_boot_linux_load_env = 'no'
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x10000000'
tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_compile_uboot_export_path = '/home/hs/dtc'
tc_demo_compile_install_test_files = ['u-boot.bin', 'u-boot.img', 'SPL', 'spl/u-boot-spl.bin', 'spl/u-boot-spl.map']
