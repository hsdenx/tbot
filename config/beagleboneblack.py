# tbot configuration
# for the beagleboneblack
boardname = 'am335x_evm'
tftpboardname = 'beagleboneblack'
boardlabpowername = 'beagleboneblack'
debug = False
debugstatus = True

uboot_prompt = '=> '
linux_prompt = 'ttbott> '

#create_dot = 'yes'
#create_statistic = 'yes'
#create_dashboard = 'yes'
#create_html_log = 'yes'
# create_documentation = 'yes'

kermit_line = '/dev/ttyUSB0'

# Toolchain
tc_workfd_set_toolchain_arch = 'arm'
tc_workfd_set_toolchain_t_p = {
'arm' : '/opt/eldk-5.4/armv5te/sysroots/i686-eldk-linux/usr/bin/armv5te-linux-gnueabi',
}

tc_workfd_set_toolchain_cr_co = {
'arm' : 'arm-linux-gnueabi-',
}

# variables used in testcases
tc_ub_boot_linux_load_env = 'set'
ub_load_board_env_set = [
	'setenv serverip 192.168.2.1',
	'setenv netmask 255.255.255.0',
	'setenv ipaddr 192.168.2.11',
	]
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x81000000'
tc_lab_get_uboot_source_git_repo = "/home/hs/git/u-boot"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_compile_uboot_export_path = '/work/hs/tbot/dtc'
tc_demo_compile_install_test_files = ['u-boot.bin', 'u-boot.img', 'MLO']
