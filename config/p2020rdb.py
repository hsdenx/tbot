# tbot configuration
# for the beagleboneblack
boardname = 'p2020rdb_1'
tftpboardname = 'p2020rdb'
boardlabpowername = 'p2020rdb_1'
debug = False
debugstatus = True
wdt_timeout = '360'

ub_load_board_env_subdir = 'tbot'
tc_lab_compile_uboot_boardname = 'P2020RDB-PC_NAND'
tc_ub_test_py_configfile = [
	'env__spl_skipped = True'
]

uboot_prompt = '=> '
linux_prompt = 'ttbott> '
uboot_autoboot_key = ' '
# set timeout to 0.5 seconds
# as bootdelay is 1 second
state_uboot_timeout = '0.5'

create_dot = 'yes'
create_statistic = 'yes'
create_dashboard = 'yes'
create_html_log = 'yes'
#create_documentation = 'yes'
create_junit = 'yes'

tc_demo_compile_install_test_name = 'tc_demo_uboot_tests.py'

# for DUTS
uboot_get_parameter_file_list = ['./u-boot.cfg']
tc_ub_i2c_help_with_bus = 'yes'

# Toolchain
tc_workfd_set_toolchain_source = '/opt/yocto-2.4/generic-powerpc-e500v2/environment-setup-ppce500v2-poky-linux-gnuspe'

# variables used in testcases
tc_ub_boot_linux_load_env = 'setend'
ub_load_board_env_set = [
	'setenv ub_file p2020rdb/tbot/u-boot-with-spl.bin',
	'setenv tbot_upd_uboot tftp 10000000 \${ub_file}\;nand device 0\;nand erase.spread 0 \${filesize}\;nand write 10000000 0 \${filesize}',
	'setenv tbot_cmp_uboot nand read 11000000 0 \${filesize}\;cmp.b 10000000 11000000 \${filesize}'
	]

setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x11000000'
tc_lab_get_uboot_source_git_repo = "git://git.denx.de/u-boot"
tc_lab_get_uboot_source_git_branch = "master"
tc_get_ub_source_reference = '/home/git/u-boot.git'
tc_lab_compile_uboot_export_path = '/work/tbot2go/tbot/dtc'
tc_demo_compile_install_test_ub_vers_file = 'u-boot.bin'
tc_demo_compile_install_test_files = ['u-boot-with-spl.bin', '.config', 'System.map']
tc_ub_upd_spl_withspl = 'no'

ub_boot_linux_cmd='run netmmcboot'
