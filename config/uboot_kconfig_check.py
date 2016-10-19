# tbot configuration for testing U-Boot patches found in
# tc_workfd_apply_local_patches_dir
# if they do not change the resulting binaries with the
# testcase tc_uboot_check_kconfig.py

# some default settings, not really needed, as we
# do not connect to a boards console
boardname = 'none'
# disable debug output
debug = False
debugstatus = True
# may you set here another loglevel for the logfile
loglevel='INFO'
# may tc_uboot_check_kconfig.py takes long...
# depends on your machine where you compile
# so adapt this value here
wdt_timeout = '120'
# we do not need to connect to a board, so disable this step
do_connect_to_board = False

uboot_prompt = 'U-Boot# '
linux_prompt = 'ttbott> '

# disable event backends
#create_dot = 'yes'
#create_statistic = 'yes'
#create_dashboard = 'yes'
#create_html_log = 'yes'

# variables used in testcases, adapt to your local settings
tc_workfd_work_dir = '/work/hs/tbot'
tc_lab_source_dir = '/work/hs/tbot'
tc_lab_get_uboot_source_git_repo = "/home/git/u-boot.git"
tc_lab_get_uboot_source_git_branch = "master"
tc_lab_compile_uboot_export_path = '/home/hs/dtc'
# adapt here to your local setting, where you have the patch(es)
# on your lab PC you want to test
tc_lab_apply_patches_dir = '/work/hs/tbot/patches/kconfig_move'
tc_workfd_apply_local_patches_checkpatch_cmd_strict = "no"
tc_workfd_apply_local_patches_checkpatch_cmd = 'scripts/checkpatch.pl'
tc_lab_compile_uboot_makeoptions = '-s -j8'

# to get a fix U-Boot version string, we need a patch ...
# may we import in U-Boot from linux the "scripts/config" script
# so we can edit a .config with tbot (we need to disable
# CONFIG_LOCALVERSION_AUTO to get a constant version string)
# ToDo
# ... you find this patch in tbot:/src/patches/check_kconfig
# move it to your lab PC and say tbot here, where it will find it
tc_uboot_check_kconfig_preparepatch = '/work/hs/tbot/patches/check_kconfig'

# setup here, where you have your toolchains
# if you do not have a toolchain for an architecture
# remove the line for it, but the boards from this arch get
# then not tested ... the name of the not tested boards are
# printed at the end of tbot on stdout
tc_workfd_set_toolchain_t_p = {
'arc' : '/home/hs/toolchain/arc_gnu_2015.12_prebuilt_uclibc_le_archs_linux_install/bin',
'arm64' : '/home/hs/.buildman-toolchains/gcc-4.9.0-nolibc/aarch64-linux/bin',
'arm' : '/opt/eldk-5.4/armv5te/sysroots/i686-eldk-linux/usr/bin/armv5te-linux-gnueabi',
'avr32' : '/home/hs/.buildman-toolchains/gcc-4.2.4-nolibc/avr32-linux/bin',
'blackfin' : '/home/hs/toolchain/opt/uClinux/bfin-elf/bin',
'm68k' : '/home/hs/.buildman-toolchains/gcc-4.6.3-nolibc/m68k-linux/bin',
'mips' : '/opt/eldk-5.4/mips/sysroots/i686-eldk-linux/usr/bin/mips32-linux',
'microblaze' : '/home/hs/.buildman-toolchains/gcc-4.9.0-nolibc/microblaze-linux/bin',
'nds32' : '/home/hs/toolchain/nds32le-linux-glibc-v1/bin',
'nios2' : '/home/hs/toolchain/sourceryg++-2015.11/bin',
'openrisc' : '/home/hs/.buildman-toolchains/gcc-4.5.1-nolibc/or32-linux/bin',
'powerpc' : '/opt/eldk-5.4/powerpc/sysroots/i686-eldk-linux/usr/bin/powerpc-linux',
'sandbox' : '/bin',
'sh' : '/home/hs/toolchain/renesas-4.4/bin',
'sparc' : '/home/hs/.buildman-toolchains/gcc-4.9.0-nolibc/sparc-linux/bin',
'x86' : '/home/hs/.buildman-toolchains/gcc-4.6.3-nolibc/i386-linux/bin',
'xtensa' : '/home/hs/.buildman-toolchains/gcc-4.9.0-nolibc/xtensa-linux/bin',
}

tc_workfd_set_toolchain_cr_co = {
'arc' : 'arc-linux-uclibc-',
'arm' : 'arm-linux-gnueabi-',
'arm64' : 'aarch64-linux-',
'avr32' : 'avr32-linux-',
'blackfin' : 'bfin-elf-',
'm68k' : 'm68k-linux-',
'mips' : 'mips-linux-',
'microblaze' : 'microblaze-linux-',
'nds32' : 'nds32le-linux-',
'nios2' : 'nios2-linux-gnu-',
'openrisc' : 'or32-linux-',
'powerpc' : 'powerpc-linux-',
'sandbox' : '',
'sh' : 'sh-linux-gnu-',
'sparc' : 'sparc-linux-',
'x86' : 'i386-linux-',
'xtensa' : 'xtensa-linux-',
}
