# tbot configuration
# for the beagleboneblack
boardname = 'am335x_evm'
tftpboardname = 'beagleboneblack'
boardlabpowername = 'beagleboneblack'
debug = False
debugstatus = True

uboot_prompt = '=> '
linux_prompt = 'ttbott> '
uboot_autoboot_key = ' '
# set timeout to 0.5 seconds
# as bootdelay is 1 second
state_uboot_timeout = 0.5

# create_dot = 'yes'
# create_statistic = 'yes'
# create_dashboard = 'yes'
# create_html_log = 'yes'
# create_documentation = 'yes'

# for DUTS
uboot_get_parameter_file_list = ['.config', 'include/configs/am335x_evm.h', 'include/configs/ti_armv7_common.h']
tc_ub_i2c_help_with_bus = 'yes'

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
tc_lab_get_uboot_source_git_repo = "git://git.denx.de/u-boot"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_compile_uboot_export_path = '/work/hs/tbot/dtc'
tc_demo_compile_install_test_files = ['u-boot.bin', 'u-boot.img', 'MLO', 'u-boot.dtb']
tc_ub_test_py_start = 'no'
tc_lab_compile_uboot_makeoptions = '-s DTC_FLAGS="-S 0xb000"'
tc_ub_upd_uboot_ubvars = 'load_uboot upd_uboot'
tc_ub_upd_spl_ubvars = 'load_mlo upd_mlo'

# Linux
tc_lab_toolchain_rev = '5.8'
tc_lab_toolchain_name = 'armv7a-hf'
tc_workfd_compile_linux_clean = 'yes'
tc_workfd_compile_linux_modules ='no'
tc_workfd_compile_linux_boardname = 'bb.org'
tc_workfd_compile_linux_dt_name = ['am335x-boneblack.dtb', 'am335x-bone.dtb']
tc_workfd_compile_linux_fit_its_file = 'no'
tc_workfd_compile_linux_append_dt = 'no'
tc_workfd_compile_linux_makeoptions = '-j8'
tc_workfd_compile_linux_make_target = 'zImage'
tc_workfd_compile_linux_modules_path = '/opt/eldk-5.8/armv7a-hf/rootfs-qte-sdk/home/hs/bbb/modules'
tc_lab_get_linux_source_git_reference = '/home/git/linux.git'
tc_lab_get_linux_source_git_repo = 'git@github.com:beagleboard/linux.git'
tc_lab_get_linux_source_git_branch = '4.9'
tc_lab_apply_patches_dir = 'none'
tc_workfd_apply_local_patches_dir = 'none'

ub_boot_linux_cmd='run netmmcboot'

linux_prompt_default = 'debian@beaglebone:~$ '
linux_user = 'debian'
devmem2_pre = 'sudo /home/debian/'

tc_demo_linux_test_dmesg = [
	'CPU: ARMv7 Processor \[413fc082\] revision 2 (ARMv7), cr=10c5387d',
	'OF: fdt:Machine model: TI AM335x BeagleBone Black',
	'OMAP clockevent source: timer2 at 24000000 Hz',
	'sched_clock: 32 bits at 24MHz',
	'omap_rtc 44e3e000.rtc: rtc core: registered 44e3e000.rtc as rtc0',
	'omap_wdt: OMAP Watchdog Timer Rev 0x01: initial timeout 60 sec',
	'omap_i2c 4819c000.i2c: bus 2 rev0.11 at 100 kHz',
	'net eth0: initializing cpsw version 1.12',
]

tc_demo_linux_test_reg_files = [
	'src/files/bbb/am335x_pinmux.reg',
	'src/files/bbb/am335x_cm_dpll.reg',
	'src/files/bbb/am335x_cm_mpu.reg',
	'src/files/bbb/am335x_cm_per.reg',
	'src/files/bbb/am335x_cm_wkup.reg',
	'src/files/bbb/am335x_ctrl_module.reg',
]

tc_demo_linux_test_basic_cmd = [
              {"cmd":"cat /proc/cpuinfo", "val":"undef"},
              {"cmd":"cat /proc/meminfo", "val":"undef"},
]
