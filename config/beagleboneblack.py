# tbot configuration
# for the beagleboneblack
boardname = 'am335x_evm'
tftpboardname = 'beagleboneblack'
boardlabpowername = 'beagleboneblack'
debug = False
debugstatus = True
wdt_timeout = '360'

tb_set_after_linux = 'tc_board_bbb_after_linux_booted.py'
tc_board_bootmode_tc = 'tc_board_bbb_bootmode.py'

ub_load_board_env_subdir = 'tbot'

# TODO set this on startup
# yocto_results_dir = '$TBOT_BASEDIR_YOCTO/build/tmp/deploy/images/beaglebone/'
yocto_results_dir = '$TBOT_BASEDIR_YOCTO/build/tmp/deploy/images/beaglebone/'
# yocto_results_dir_lab = tb.config.tftpdir + '/' + tb.config.tftpboardname + '/tbot/yocto/'
yocto_results_dir_lab = '/srv/tftpboot/beagleboneblack/tbot/yocto/'
nfs_subdir = '/work/tbot2go/tbot/nfs/bbb'

state_linux_timeout = 40

linux_user = 'root'
uboot_prompt = '=> '
#uboot_prompt = 'U-Boot# '
linux_prompt = 'ttbott> '
uboot_autoboot_key = ' '
# set timeout to 0.5 seconds
# as bootdelay is 1 second
state_uboot_timeout = 0.5

create_dot = 'yes'
create_statistic = 'yes'
create_dashboard = 'yes'
create_html_log = 'yes'
create_documentation = 'yes'

# for DUTS
uboot_get_parameter_file_list = ['.config', 'include/configs/am335x_evm.h', 'include/configs/ti_armv7_common.h']
tc_ub_i2c_help_with_bus = 'yes'

# Toolchain
tc_workfd_set_toolchain_arch = 'arm'
tc_workfd_set_toolchain_t_p = {
'arm' : '/home/hs/toolchain/linaro/gcc-linaro-7.2.1-2017.11-i686_arm-linux-gnueabi/bin',
}

tc_workfd_set_toolchain_cr_co = {
'arm' : 'arm-unknown-linux-gnueabi-',
}

# variables used in testcases
tc_ub_boot_linux_load_env = 'setend'
ub_load_board_env_set = [
	'setenv serverip 192.168.3.1',
	'setenv netmask 255.255.255.0',
	'setenv ipaddr 192.168.3.20',
	'setenv load_addr_r 81000000',
	'setenv cmp_addr_r 82000000',
	'setenv mlofile ' + tftpboardname + '/' + ub_load_board_env_subdir +'/MLO',
	'setenv load_mlo tftp \${load_addr_r} \${mlofile}',
	'setenv ubfile ' + tftpboardname + '/' + ub_load_board_env_subdir +'/u-boot.img',
	'setenv load_uboot tftp \${load_addr_r} \${ubfile}',
	'setenv upd_mlo mmc dev 0\;fatwrite mmc 0:1 \${load_addr_r} MLO \${filesize}',
	'setenv upd_uboot mmc dev 0\;fatwrite mmc 0:1 \${load_addr_r} u-boot.img \${filesize}',
	'setenv cmp_mlo fatload mmc 0:1 \${load_addr_r} MLO \${filesize}\;tftp \${cmp_addr_r} \${mlofile}\;cmp.b \${load_addr_r} \${cmp_addr_r} \${filesize}',
	'setenv cmp_uboot fatload mmc 0:1 \${load_addr_r} u-boot.img\;tftp \${cmp_addr_r} \${ubfile}\;cmp.b \${load_addr_r} \${cmp_addr_r} \${filesize}',
	'setenv tbot_upd_uboot run load_uboot\;run upd_uboot_emmc',
	'setenv tbot_cmp_uboot run cmp_uboot_emmc',
	'setenv tbot_upd_spl run load_mlo\;run upd_mlo_emmc',
	'setenv tbot_cmp_spl run cmp_mlo_emmc',
	'setenv upd_mlo_emmc mmc dev 1\;mmc write \${load_addr_r} 100 100',
	'setenv upd_uboot_emmc mmc dev 1\;mmc erase 400 400\;mmc write \${load_addr_r} 300 600',
	'setenv cmp_mlo_emmc mmc read \${cmp_addr_r} 100 100\;cmp.b \${load_addr_r} \${cmp_addr_r} \${filesize}',
	'setenv cmp_uboot_emmc mmc read \${cmp_addr_r} 300 600\;cmp.b \${load_addr_r} \${cmp_addr_r} \${filesize}',
	'setenv console ttyS0,115200n8',
	'setenv bootfile ' + tftpboardname + '/' + ub_load_board_env_subdir +'/zImage',
	'setenv fdtfile ' + tftpboardname + '/' + ub_load_board_env_subdir +'/am335x-boneblack.dtb',
	'setenv netmmcboot echo Booting from network ... with mmcargs ...\; setenv autoload no\; run netloadimage\; run netloadfdt\; run args_mmc\; bootz \${loadaddr} - \${fdtaddr}',
	'setenv netdev eth0',
	'setenv hostname bbb',
	'setenv addip setenv bootargs \${bootargs} ip=\${ipaddr}:\${serverip}:\${gatewayip}:\${netmask}:\${hostname}:\${netdev}::off panic=1',
	'setenv addcon setenv bootargs \${bootargs} console=\${console}',
	'setenv addmisc setenv bootargs \${bootargs} loglevel=8',
	'setenv addmtd setenv bootargs \${bootargs} \${mtdparts}',
	'setenv rootpath '+ nfs_subdir,
	'setenv nfsopts nfsvers=3 nolock rw',
	'setenv nfsargs setenv bootargs \${bootargs} root=/dev/nfs rw nfsroot=\${serverip}:\${rootpath},\${nfsopts}',
	'setenv net_nfs run netloadimage\; run netloadfdt\;run nfsargs addcon addip addmtd addmisc\;bootz \${loadaddr} - \${fdtaddr}',
	'setenv sdloadk ext2load mmc 0:2 \${loadaddr} /boot/zImage',
	'setenv sdloadfdt ext2load mmc 0:2 \${fdtaddr} /boot/am335x-boneblack.dtb',
	'setenv sd_sd run sdloadk\; run sdloadfdt\;run args_mmc\;bootz \${loadaddr} - \${fdtaddr}',
	]

setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x81000000'
tc_lab_get_uboot_source_git_repo = "git://git.denx.de/u-boot"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_compile_uboot_export_path = '/work/tbot2go/tbot/dtc'
tc_demo_compile_install_test_ub_vers_file = 'u-boot.bin'
tc_demo_compile_install_test_spl_vers_file = 'MLO'
tc_demo_compile_install_test_files = ['u-boot.bin', 'u-boot.img', 'MLO', 'u-boot.dtb', '.config']
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
tc_workfd_compile_linux_modules_path = 'none'
tc_lab_get_linux_source_git_reference = '/work/tbot2go/linux'
tc_lab_get_linux_source_git_repo = 'git@github.com:beagleboard/linux.git'
tc_lab_get_linux_source_git_branch = '4.9'
tc_lab_apply_patches_dir = 'none'
tc_workfd_apply_local_patches_dir = 'none'

ub_boot_linux_cmd='run netmmcboot'

tc_demo_compile_install_test_name = 'tc_demo_uboot_tests.py'

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

tc_demo_uboot_test_deploy = 'tc_board_deploy_beagleboneblack.py'
tc_demo_linux_test_deploy = 'tc_board_deploy_lx_beagleboneblack.py'

# yocto
#tc_workfd_goto_yocto_code_dirext = '-pyro'

# may we get this from the local.conf file
tc_workfd_bitbake_machine = 'beaglebone'

tc_workfd_get_yocto_patches_git_repo = 'ssh://pi@192.168.3.1:/home/pi/tbot2go/poky-patches'
tc_workfd_get_yocto_patches_git_branch = 'bbb-pyro'
tc_workfd_get_yocto_patches_git_repo_name = 'patches-bbb'
tc_workfd_get_yocto_source_git_repo = 'git://git.yoctoproject.org/poky.git'
tc_workfd_get_yocto_source_git_branch = 'pyro'
tc_workfd_get_yocto_git_commit_id = 'none'
tc_workfd_get_yocto_apply_patches_dir = 'none'
tc_workfd_get_yocto_clone_apply_patches_git_am_dir = '$TBOT_BASEDIR/patches-bbb/bbb-pyro'
tc_workfd_get_yocto_source_git_reference = 'none'
tc_workfd_get_yocto_source_git_repo_user = ''
tc_workfd_get_yocto_source_conf_dir = '$TBOT_BASEDIR/patches-bbb/conf/'
tc_workfd_get_yocto_source_conf_dl_dir = '$TBOT_BASEDIR/yocto_dl_dir'
tc_workfd_get_yocto_source_conf_sstate_dir = '$TBOT_BASEDIR/yocto_sstate/bbb'

tc_workfd_get_yocto_source_layers = [
['git://git.openembedded.org/meta-openembedded', 'pyro', 'none', 'none', 'none', 'none', '', 'meta-openembedded'],
]

tc_workfd_check_tar_content_endtc_onerror = 'False'
rootfs_tar_file = 'core-image-minimal-beaglebone.tar.bz2'
rootfs_sdcard_file = 'core-image-minimal-beaglebone.wic'
tc_workfd_check_tar_content_path = yocto_results_dir + rootfs_tar_file
tc_workfd_check_tar_content_elements = [
# tools
'devmem2',
'nano',
#'vim',
'mtd_debug',
'flash_erase',
#'printenv',
]

yocto_check_result_files = [
	yocto_results_dir + '/MLO',
	yocto_results_dir + '/u-boot.img',
	yocto_results_dir + '/zImage',
	yocto_results_dir + '/zImage-am335x-boneblack.dtb',
	yocto_results_dir + rootfs_tar_file,
	yocto_results_dir + rootfs_sdcard_file,
]

linux_get_ifconfig_dev = 'eth0'

# TODO get rid of this var
nfs_serverip = '192.168.3.1'
tc_board_yocto_deploy_files = yocto_check_result_files
tc_yocto_get_rootfs_from_tarball = tc_workfd_check_tar_content_path
