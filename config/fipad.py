# tbot configuration
# for the fipad board
boardname = 'fipad'
debug=False
debugstatus=True
loglevel='INFO'

wdt_timeout = '3600'

uboot_prompt = '=> '
linux_prompt = 'ttbott> '

# create_dot = 'yes'
# create_statistic = 'yes'
# create_dashboard = 'yes'
# create_html_log = 'yes'

# set connect testcase (as it is with kermit, not with connect)
#tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
#tc_workfd_connect_with_kermit_rlogin = 'rlogin metis fipad'
#tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'

# variables used in testcases
#board_has_debugger = 1
#lab_bdi_upd_uboot_bdi_prompt = 'fipad-i.MX6>'
#lab_bdi_upd_uboot_bdi_cmd = 'telnet bdi1'

setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x81000000'
tc_ub_download_load = 'no'

tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_compile_uboot_export_path = '/home/hs/dtc'

tc_workfd_set_toolchain_arch = 'arm'
tc_workfd_set_toolchain_t_p = {
'arm' : '/home/hs/toolchain/linaro/gcc-linaro-7.2.1-2017.11-i686_arm-linux-gnueabi/bin',
}
tc_workfd_set_toolchain_cr_co = {
'arm' : 'arm-linux-gnueabi-',
}

ub_load_board_env_addr = '0x12000000'
ub_load_board_env_subdir = 'tbot'

tc_lab_compile_uboot_boardname = 'bosch_mpcxxxxd_sd'

tc_ub_create_reg_file_name = 'src/files/fipad_ub_pinmux.reg'
tc_ub_create_reg_file_comment = 'pinmux'
tc_ub_create_reg_file_start = '20e0000'
tc_ub_create_reg_file_stop = '20e093c'
tc_ub_readreg_mask = '0xffffffff'
tc_ub_create_reg_file_mode = 'w+'
tc_ub_readreg_type = 'l'

tc_ub_create_reg_file_name = 'src/files/fipad_ub_pinmux.reg'
tc_ub_create_reg_file_comment = 'pinmux'
tc_ub_create_reg_file_start = '20e0000'
# for DUTS
tc_ub_memory_ram_ws_base = '0x10000000'
tc_ub_memory_ram_big = 'no'
# uboot_get_parameter_file_list = ['.config', 'include/configs/am335x_shc.h', 'include/configs/ti_armv7_common.h']
tc_ub_i2c_help_with_bus = 'yes'

# Linux
tc_lab_toolchain_rev = '5.4'
tc_lab_toolchain_name = 'armv7a-hf'
tc_workfd_compile_linux_clean = 'yes'
tc_workfd_compile_linux_modules ='no'
tc_workfd_compile_linux_dt_name = ['bosch-mpc1360d.dtb', 'bosch-mpc2460d.dtb', 'bosch-mpc4560d.dtb']
tc_workfd_compile_linux_fit_its_file = 'no'
tc_workfd_compile_linux_append_dt = 'no'
tc_workfd_compile_linux_makeoptions = '-j8'
tc_workfd_compile_linux_make_target = 'zImage'
tc_workfd_compile_linux_modules_path = '/opt/eldk-5.5/armv7a-hf/rootfs-sato-sdk/home/hs/fipad/modules'
tc_lab_get_linux_source_git_reference = '/home/git/linux.git'
tc_lab_get_linux_source_git_repo = 'git@gitlab.denx.de:bosch-st/linux-fipad.git'
tc_lab_get_linux_source_git_branch = 'fipad-devel'
tc_lab_apply_patches_dir = 'none'
tc_workfd_apply_local_patches_dir = 'none'

linux_prompt_default = 'generic-armv7a-hf:~# '
tc_lx_create_reg_file_start = '0x2648000'
tc_lx_create_reg_file_stop = '0x2648178'
tc_lx_readreg_mask = 0xffffffff
tc_lx_readreg_type = 'w'
tc_lx_create_reg_file_name = 'fipad_lx_pinmux.reg'

tc_lx_regulator_nrs = ['0 regulator-dummy -', '1 vdd1p1 1100000',
                '2 vdd3p0 3000000', '3 vdd2p5 2400000',
                '4 vddarm 1150000', '5 vddpu 1175000',
                '6 vddsoc 1175000', '7 usb_otg_vbus 5000000',
		'8 usb_h1_vbus 5000000', '9 IOVDD 1800000',
		'10 DVDD 1800000', '11 AVDD 3300000',
		'12 DRVDD 3300000', '13 3P3V 3300000']

tc_workfd_can_ssh = 'metis'
tc_workfd_can_su = 'metis'

# this is for the uboot usb tests
# adapt this settings, as tehy fit for the usb stick
# attached to the fipad board in the denx lab
tc_uboot_usb_info_expect = [
    'Hub,  USB Revision 2.0',
    'Mass Storage,  USB Revision 2.0',
    'SMI Corporation USB DISK AA04012900007453',
    'Vendor: 0x090c  Product 0x1000 Version 17.0'
]
tc_board_fipad_uboot_ext2load_files = [
    'test.bin',
    'ub_usb_test1.bin',
    'ub_usb_test2.bin'
]
