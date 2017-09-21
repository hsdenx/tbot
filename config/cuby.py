# tbot configuration
# for the cuby board
boardname = 'cuby'
debug=False
debugstatus=True
loglevel='INFO'

wdt_timeout = '360'

# uboot_prompt = 'U-Boot# '
uboot_prompt = '=> '
uboot_autoboot_key = 'q'
linux_prompt = 'ttbott> '
# ramdisk
# linux_prompt_default = '/ # '
#linux_prompt_default = 'root@generic-armv7a-hf:~# '
#linux_prompt_default = 'root@generic-armv7a-hf:'
linux_prompt_default = '~# '

term_line_length = '250'
# do_connect_to_board = False

board_has_debugger = 0
#board_has_debugger = 1
#lab_bdi_upd_uboot_bdi_cmd = 'telnet bdi19'
#lab_bdi_upd_uboot_bdi_prompt = 'CUBY>'
#lab_bdi_upd_uboot_bdi_run = [
#{'cmd':'h;MMH  0x402f0400 0xa000;MMH  0x402f0402 0x4700;t 0x402f0400;t;load 0x402f0400 /tftpboot/cuby/20161208/u-boot-spl.bin BIN;t 0x402f0400;g', 'val':'Loading program file passed'},
#{'cmd':'h;MMH  0x807ffffc 0xa000;MMH  0x807ffffe 0x4700;load 0x80800000 /tftpboot/cuby/20161208/u-boot.bin BIN;ti 0x807ffffc;g', 'val':'Loading program file passed'}
#]

create_dot = 'yes'
create_statistic = 'yes'
create_dashboard = 'yes'
create_html_log = 'yes'
create_documentation = 'yes'
event_documentation_strip_list = ['Resolving deltas',
            'Compressing objects',
            'Receiving objects',
            'remote: Counting objects',
            'Parsing recipes',
            'Initialising tasks',
            'Running tasks',
            'Loading cache',
        ]

# set connect testcase (as it is with kermit, not with connect)
# tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'
# tc_workfd_connect_with_kermit_rlogin = 'rlogin metis shc'
# tc_lab_denx_disconnect_from_board_tc = 'tc_workfd_disconnect_with_kermit.py'

# variables used in testcases
setenv_name = 'Heiko'
setenv_value = 'Schocher'
ub_load_board_env_addr = '0x81000000'

tc_lab_get_uboot_source_git_repo = '/home/git/u-boot.git'
tc_lab_get_uboot_source_git_branch = 'master'

tc_lab_toolchain_rev = '5.4'
tc_lab_toolchain_name = 'armv7a'
tc_workfd_compile_linux_clean = 'no'

tc_lab_compile_uboot_boardname = 'am335x_cuby'
tc_board_shc_upd_ub_typ = 'eMMC'
# tc_board_shc_upd_ub_typ = 'SD'

tc_ub_boot_linux_load_env = 'no'
ub_boot_linux_cmd = 'run bootcmd'

tc_ub_create_reg_file_name = 'src/files/cuby/cuby_ub_pinmux.reg'
tc_ub_create_reg_file_comment = 'pinmux'
tc_ub_create_reg_file_start = '44e10800'
tc_ub_create_reg_file_stop = '44e10a34'
tc_ub_readreg_mask = '0xffffffff'
tc_ub_create_reg_file_mode = 'w+'
tc_ub_readreg_type = 'l'

# for DUTS
uboot_get_parameter_file_list = ['.config', 'include/configs/am335x_cuby.h', 'include/configs/ti_armv7_common.h']
tc_ub_i2c_help_with_bus = 'yes'

# linux testcases
tc_lx_create_reg_file_name = 'src/files/cuby/cuby_pinmux.reg'
tc_lx_create_reg_file_start = '44e10800'
tc_lx_create_reg_file_stop = '44e10a38'
tc_lx_readreg_type = 'w'


tc_workfd_compile_linux_boardname = 'cuby'
tc_workfd_compile_linux_load_addr = '0x80008000'
tc_workfd_compile_linux_modules_path ='/opt/eldk-5.5/armv7a-hf/rootfs-sato-sdk/home/hs/cuby/modules'
tc_workfd_compile_linux_dt_name = 'am335x-cuby.dtb'
tc_workfd_compile_linux_fit_its_file = 'no'
tc_workfd_compile_linux_fit_file = 'cuby.itb'
tc_workfd_compile_linux_append_dt = 'no'

# kernel 4.9-rc6
tc_lab_get_linux_source_git_repo = '/home/hs/ssi/linux'
tc_lab_get_linux_source_git_repo_user = 'hsdenx'
tc_lab_get_linux_source_git_branch = 'linux-v4.9-rc6-shc-20161121-3'
tc_lab_get_linux_source_git_reference = '/home/git/linux.git'
tc_lab_apply_patches_dir = 'none'
tc_workfd_compile_linux_modules = 'none'
tc_workfd_apply_local_patches_dir = 'none'
tc_workfd_compile_linux_makeoptions = '-j8'

# hdparm
tc_workfd_hdparm_path = 'none'
tc_workfd_hdparm_dev = '/dev/mmcblk0'
tc_workfd_hdparm_min = '10.0'

# yocto

tc_lx_dmesg_grep_options = ''

#tc_workfd_goto_yocto_code_dirext = '-pyro'

# may we get this from the local.conf file
tc_workfd_bitbake_machine = 'cuby'

tc_workfd_get_yocto_patches_git_repo = 'git@gitlab.denx.de:ssi/poky-patches.git'
tc_workfd_get_yocto_patches_git_branch = 'cuby-devel-denx-pyro'
tc_workfd_get_yocto_patches_git_repo_name = 'patches-cuby'
tc_workfd_get_yocto_patches_git_commit_id = 'e2646d0866311f34cf333251b0a2ca321997cf8a'
tc_workfd_get_yocto_source_git_repo = 'git://git.yoctoproject.org/poky.git'
tc_workfd_get_yocto_source_git_branch = 'pyro'
tc_workfd_get_yocto_git_commit_id = 'none'
tc_workfd_get_yocto_apply_patches_dir = 'none'
tc_workfd_get_yocto_clone_apply_patches_git_am_dir = '$TBOT_BASEDIR/patches-cuby/pyro'
tc_workfd_get_yocto_source_git_reference = 'none'
tc_workfd_get_yocto_source_git_repo_user = ''
tc_workfd_get_yocto_source_conf_dir = '$TBOT_BASEDIR/patches-cuby/conf/'
tc_workfd_get_yocto_source_conf_dl_dir = '$TBOT_BASEDIR/yocto_dl_dir'
tc_workfd_get_yocto_source_conf_sstate_dir = '$TBOT_BASEDIR/yocto_sstate/cuby'

#meta-yocto-bsp    = "pyro:f1cca80620a3718d9a2b3ce4c9dfe428a1e6fed1"
#meta-qt5          = "pyro:c6aa602d0640040b470ee81de39726276ddc0ea3"
#meta-python       = "pyro:5e82995148a2844c6f483ae5ddd1438d87ea9fb7"
#meta-swupdate     = "master:faf9b96599d600d82cb3458578bd878a01933c26"
#meta-cuby         = "cuby-devel-denx-pyro-new:fd96d8e456458d9699bc8b70e80a52604796ad02"


tc_workfd_get_yocto_source_layers = [
['git://git.openembedded.org/meta-openembedded', 'pyro', 'none', 'none', 'none', 'none', '', 'meta-openembedded'],
['https://github.com/meta-qt5/meta-qt5.git', 'pyro', 'none', 'none', 'none', 'none', '', 'meta-qt5'],
['https://github.com/sbabic/meta-swupdate.git', 'master', '222ab9ec6421c466b453cfd16befbb8a78950a65', 'none', '$TBOT_BASEDIR/patches-cuby/swupdate', 'none', '', 'meta-swupdate'],
['git@gitlab.denx.de:ssi/meta-cuby.git', 'cuby-devel-denx-pyro', 'none', 'none', 'none', 'none', '', 'meta-cuby'],
]
# poky f0d128ea0dfc2c403ff53a1ac1db3521854b63d5
# meta-openembbedded 5e82995148a2844c6f483ae5ddd1438d87ea9fb7
# qt5 31761f625d2151e9d94d0d83067f90a5da6508e1

tc_workfd_check_tar_content_endtc_onerror = 'False'
tc_workfd_check_tar_content_path = '$TBOT_BASEDIR_YOCTO/build/tmp/deploy/images/cuby/qt-cuby-cuby.tar.gz'
tc_workfd_check_tar_content_elements = [
# kernel module
#'uio_pruss.ko',
# libs
#'linux-vdso.so.1',
'libQt5Test.so.5',
'libprussdrv.so',
'libQt5Core.so.5',
'libstdc++.so.6',
'libm.so.6',
'libgcc_s.so.1',
'libc.so.6',
'libpthread.so.0',
'/lib/ld-linux-armhf.so.3',
'libz.so.1',
'libicui18n.so.',
'libicuuc.so.',
'libdl.so.2',
'libglib-2.0.so.0',
'librt.so.1',
'libicudata.so',
'libpcre16.so.0',
# libQT5
'libQt5Core.so.5',
'libQt5Network.so.5',
'libQt5SerialBus.so.5',
'libQt5SerialPort.so.5',
'libQt5WebSockets.so.5',
# lib boost 1.62
'/usr/lib/libboost_system.so.1.6',
# tools
'nano',
'vim',
'cansend',
'candump',
'mtd_debug',
'flash_erase',
'printenv',
'check_setup',
'cuby_shuttle_application'
]
linux_get_ifconfig_dev = 'eth0:1'

tc_board_cuby_yocto_result_dir = '/srv/tftpboot/cuby/tbot/yocto_results/'

#get rid of this var
nfs_serverip = '192.168.3.1'
tc_board_cuby_nfs_dir_w = '/work/tbot2go/tbot/nfs/cuby/'
tc_board_cuby_nfs_dir_loc = '/boot/'
tc_board_cuby_sd_image_name = 'cuby-image-cuby-rootfs-cuby-sd.img'
tc_board_cuby_swu_name = 'cuby-image-cuby.swu'
rootfs_tar_file = 'qt-cuby-cuby.tar.gz'
tc_board_cuby_yocto_deploy_files = [
	'images/cuby/cuby-image-cuby.swu',
	'images/cuby/cuby-image-cuby-rootfs-cuby-sd.img',
	'images/cuby/qt-cuby-cuby.tar.gz'
]
tc_yocto_get_rootfs_from_tarball = tc_board_cuby_yocto_result_dir + 'qt-cuby-cuby.tar.gz'
