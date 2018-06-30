# SPDX-License-Identifier: GPL-2.0
#
# Description:
# compile u-boot
#
# used variables
# - tb.config.tc_lab_compile_uboot_export_path
#| if != 'none' add in PATH the string from this variable
#| default: 'none'
#
# - tb.config.tc_lab_compile_uboot_boardname
#| Name used for defconfig
#| default: tb.config.boardname
#
# - tb.config.tc_lab_compile_uboot_makeoptions
#| option string used for calling make
#| default: '-j4'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_lab_compile_uboot_export_path', 'none')
tb.define_variable('tc_lab_compile_uboot_boardname', tb.config.boardname)
tb.define_variable('tc_lab_compile_uboot_makeoptions', '-j4')

tb.eof_call_tc("tc_workfd_goto_uboot_code.py")

if tb.config.tc_lab_compile_uboot_export_path != 'none':
    tb.event.create_event('main', 'tc_lab_compile_uboot.py', 'SET_DOC_FILENAME', 'compile_uboot_set_dtc')
    tmp = "printenv PATH | grep --color=never " + tb.config.tc_lab_compile_uboot_export_path
    ret = tb.write_lx_cmd_check(tb.workfd, tmp, endTC=False)
    if ret == False:
        tmp = "export PATH=" + tb.config.tc_lab_compile_uboot_export_path + ":$PATH"
        tb.write_lx_cmd_check(tb.workfd, tmp)

tb.event.create_event('main', 'tc_lab_compile_uboot.py', 'SET_DOC_FILENAME', 'compile_uboot_mrproper')
tmp = "make mrproper"
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.event.create_event('main', 'tc_lab_compile_uboot.py', 'SET_DOC_FILENAME', 'compile_uboot_config')
defname = tb.config.tc_lab_compile_uboot_boardname + "_defconfig"
tmp = "make " + defname
tb.event.create_event('main', tb.config.boardname, "UBOOT_DEFCONFIG", defname)
tb.write_lx_cmd_check(tb.workfd, tmp)
if tb.workfd.name == 'tb_cpc':
    tb.event.create_event('main', tb.config.boardname, "UBOOT_SRC_PATH", tb.config.tftpdir + '/' + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir)
else:
    tb.event.create_event('main', tb.config.boardname, "UBOOT_SRC_PATH", tb.config.tc_lab_source_dir + "/u-boot-" + tb.config.boardlabname)

tb.event.create_event('main', 'tc_lab_compile_uboot.py', 'SET_DOC_FILENAME', 'compile_uboot_make')
tmp = "make " + self.config.tc_lab_compile_uboot_makeoptions + " all"
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
