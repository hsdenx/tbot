# This file is part of tbot.  tbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_compile_linux.py
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
# End:

from tbotlib import tbot

logging.info("args: workdfd: %s %s", tb.workfd.name, tb.config.tc_workfd_compile_linux_clean)
logging.info("args: %s", tb.config.tc_workfd_compile_linux_load_addr)
logging.info("args: %s", tb.config.tc_workfd_compile_linux_makeoptions)
logging.info("args: %s", tb.config.tc_workfd_compile_linux_make_target)
logging.info("args: %s %s", tb.config.tc_workfd_compile_linux_fit_its_file, \
             tb.config.tc_workfd_compile_linux_fit_file)
logging.info("args: %s %s", tb.config.tc_workfd_compile_linux_boardname, \
             tb.config.tc_workfd_compile_linux_modules)
logging.info("args: %s %s", tb.config.tc_workfd_compile_linux_dt_name, \
             tb.config.tc_workfd_compile_linux_modules_path)
logging.info("args: %s %s", tb.config.tc_workfd_compile_linux_append_dt, \
             tb.config.tc_workfd_compile_linux_mkimage)

tb.set_term_length(tb.workfd)

# print where we are ...
tb.eof_write_cmd(tb.workfd, 'pwd')

# call set toolchain
tb.statusprint("set toolchain")
tb.eof_call_tc("tc_lab_set_toolchain.py")

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

tmp = "make" + ld + " " + tb.config.tc_workfd_compile_linux_makeoptions + " " + tb.config.tc_workfd_compile_linux_make_target
tb.write_lx_cmd_check(tb.workfd, tmp)

# compile modules (if wanted)
if tb.config.tc_workfd_compile_linux_modules != 'none':
    tmp = "make" + ld + " " + tb.config.tc_workfd_compile_linux_makeoptions + " modules"
    tb.write_lx_cmd_check(tb.workfd, tmp)
    # install modules (if wanted)
    if tb.config.tc_workfd_compile_linux_modules_path != 'none':
        tmp = "INSTALL_MOD_PATH=" + tb.config.tc_workfd_compile_linux_modules_path + " make modules_install"
        tb.write_lx_cmd_check(tb.workfd, tmp)

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
