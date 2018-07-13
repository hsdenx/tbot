# SPDX-License-Identifier: GPL-2.0
#
# Description:
# compile linux:
# - set toolchain with tc_lab_set_toolchain.py
# - if tb.config.tc_workfd_compile_linux_clean == 'yes'
#   call "make mrproper"
# - tb.config.tc_workfd_compile_linux_load_addr != 'no'
#   add LOAD_ADDR=tb.config.tc_workfd_compile_linux_load_addr to make
# - make tb.config.tc_workfd_compile_linux_boardname defconfig
# - make tb.config.tc_workfd_compile_linux_makeoptions tb.config.tc_workfd_compile_linux_make_target
# - if tb.config.tc_workfd_compile_linux_modules != 'none'
#   compile modules
# - if tb.config.tc_workfd_compile_linux_dt_name != 'none'
#   compile DTB from list tb.config.tc_workfd_compile_linux_dt_name
# - if tb.config.tc_workfd_compile_linux_fit_its_file != 'no'
#   create FIT image
#   mkimage path: tb.config.tc_workfd_compile_linux_mkimage
#   fit description file: tb.config.tc_workfd_compile_linux_fit_its_file
#   tb.config.tc_workfd_compile_linux_fit_file
# - if tb.config.tc_workfd_compile_linux_append_dt != 'no'
#   append dtb to kernel image
# tb.config.tc_workfd_compile_linux_boardname _defconfig
#
# used variables
#
# - tb.config.tc_workfd_compile_linux_clean
#| if 'yes' call 'make mrproper'
#| default: 'yes'
#
# - tb.config.tc_workfd_compile_linux_load_addr
#| if != 'no' add LOADADDR= before make
#| default: 'no'
#
# - tb.config.tc_workfd_compile_linux_makeoptions
#| string of makeoptions
#| default: 'none'
#
# - tb.config.tc_workfd_compile_linux_make_target
#| make target normally zImage or uImage
#| default: 'uImage'
#
# - tb.config.tc_workfd_compile_linux_fit_its_file
#| if != 'no' create fit image
#| its file is tb.config.tc_workfd_compile_linux_fit_its_file
#| output file is tb.config.tc_workfd_compile_linux_fit_file
#| default: 'no'
#
# - tb.config.tc_workfd_compile_linux_fit_file
#| output file name if creating fit image
#| default: 'no'
#
# - tb.config.tc_workfd_compile_linux_boardname
#| name for the used defconfig (without '_defconfig')
#| default: tb.config.boardname
#
# - tb.config.tc_workfd_compile_linux_modules
#| if != 'none' build modules
#| default: 'none'
#
# - tb.config.tc_workfd_compile_linux_modules_path
#| if != 'none' contains modules path for 'make modules_install' step
#| INSTALL_MOD_PATH=tb.config.tc_workfd_compile_linux_modules_path
#| default: 'none'
#
# - tb.config.tc_workfd_compile_linux_dt_name
#| contains a string or a list of strings of
#| dtb targets
#| default: 'none'
#
# - tb.config.tc_workfd_compile_linux_append_dt
#| if != 'no' append tb.config.tc_workfd_compile_linux_dt_name
#| to 'z' + tb.config.tc_workfd_compile_linux_append_dt
#| default: 'no'
#
# - tb.config.tc_workfd_compile_linux_mkimage
#| path to mkimage tool (incl. mkimage)
#| default: '/home/hs/i2c/u-boot/tools/mkimage'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_compile_linux_clean', 'yes')
tb.define_variable('tc_workfd_compile_linux_load_addr', 'no')
tb.define_variable('tc_workfd_compile_linux_makeoptions', 'none')
tb.define_variable('tc_workfd_compile_linux_make_target', 'uImage')
tb.define_variable('tc_workfd_compile_linux_fit_its_file', 'no')
tb.define_variable('tc_workfd_compile_linux_fit_file', 'no')
tb.define_variable('tc_workfd_compile_linux_boardname', tb.config.boardname)
tb.define_variable('tc_workfd_compile_linux_modules', 'none')
tb.define_variable('tc_workfd_compile_linux_modules_path', 'none')
tb.define_variable('tc_workfd_compile_linux_dt_name', 'none')
tb.define_variable('tc_workfd_compile_linux_append_dt', 'no')
tb.define_variable('tc_workfd_compile_linux_mkimage', '/home/hs/i2c/u-boot/tools/mkimage')
logging.info("args: workdfd: %s", tb.workfd.name)

tb.set_term_length(tb.workfd)

# print where we are ...
tb.eof_write_cmd(tb.workfd, 'pwd')

# call set toolchain
tb.statusprint("set toolchain")
tb.eof_call_tc("tc_workfd_set_toolchain.py")

if tb.config.tc_workfd_compile_linux_clean == 'yes':
    tmp = "make mrproper"
    tb.write_lx_cmd_check(tb.workfd, tmp)

# compile kernel
if tb.config.tc_workfd_compile_linux_load_addr != 'no':
    ld = ' LOADADDR=' + tb.config.tc_workfd_compile_linux_load_addr + ' '
else:
    ld = ' '

tmp = "make " + tb.config.tc_workfd_compile_linux_boardname + "_defconfig"
tb.write_lx_cmd_check(tb.workfd, tmp)
tb.event.create_event('main', tb.config.boardname, "LINUX_DEFCONFIG", tb.config.tc_workfd_compile_linux_boardname)
tb.event.create_event('main', tb.config.boardname, "LINUX_SRC_PATH", tb.config.tc_lab_source_dir + "/linux-" + tb.config.boardlabname)

opt = ''
if tb.config.tc_workfd_compile_linux_makeoptions != 'none':
    opt = tb.config.tc_workfd_compile_linux_makeoptions

tmp = "make" + ld + " " + opt + " " + tb.config.tc_workfd_compile_linux_make_target
tb.write_lx_cmd_check(tb.workfd, tmp, triggerlist=['CC'])

# compile modules (if wanted)
if tb.config.tc_workfd_compile_linux_modules != 'none':
    tmp = "make" + ld + " " + opt + " modules"
    tb.write_lx_cmd_check(tb.workfd, tmp, triggerlist=['CC'])
    # install modules (if wanted)
    if tb.config.tc_workfd_compile_linux_modules_path != 'none':
        tmp = "INSTALL_MOD_PATH=" + tb.config.tc_workfd_compile_linux_modules_path + " make modules_install"
        tb.write_lx_cmd_check(tb.workfd, tmp, triggerlist=['CC'])

# compile DT (if wanted)
if tb.config.tc_workfd_compile_linux_dt_name != 'none':
    x=[]
    if isinstance(tb.config.tc_workfd_compile_linux_dt_name, (list, tuple)):
        for i in tb.config.tc_workfd_compile_linux_dt_name:
            if isinstance(i, str):
                x.append(i)
    else:
        x.append(tb.config.tc_workfd_compile_linux_dt_name)

    for i in x:
        tmp = "make " + i
        tb.write_lx_cmd_check(tb.workfd, tmp)

# create FIT image (if wanted)
# $UBPATH/tools/mkimage  -f $FIT_FILE_NAME $BOARD.itb
if tb.config.tc_workfd_compile_linux_fit_its_file != 'no':
    tmp = tb.config.tc_workfd_compile_linux_mkimage + ' -f ' + tb.config.tc_workfd_compile_linux_fit_its_file + ' ' + tb.config.tc_workfd_compile_linux_fit_file
    tb.write_lx_cmd_check(tb.workfd, tmp)

# append DT to linux image (if wanted)
# cat arch/arm/boot/zImage arch/arm/boot/dts/am335x-pxm2-oldboot.dtb > zImage-self-pxm2
if tb.config.tc_workfd_compile_linux_append_dt != 'no':
    tmp = "cat arch/arm/boot/zImage arch/arm/boot/dts/" + tb.config.tc_workfd_compile_linux_dt_name + " > " + 'z' + tb.config.tc_workfd_compile_linux_append_dt
    tb.write_lx_cmd_check(tb.workfd, tmp)
# $UBPATH/tools/mkimage -A arm -O linux -T kernel -C none -a 0x80080000 -e 0x80080000 -d zImage-self-pxm2 uImage-self-pxm2
    tmp = tb.config.tc_workfd_compile_linux_mkimage + ' -A arm -O linux -T kernel -C none -a ' + tb.config.tc_workfd_compile_linux_load_addr + ' -e ' + tb.config.tc_workfd_compile_linux_load_addr + ' -d z' + tb.config.tc_workfd_compile_linux_append_dt + ' u' + tb.config.tc_workfd_compile_linux_append_dt
    tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
