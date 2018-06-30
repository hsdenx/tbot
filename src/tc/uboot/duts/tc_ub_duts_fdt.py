# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_duts_fdt.py
#
# create logfiles used for DULG
# http://www.denx.de/wiki/view/DULG/UBootCmdFDT
#
# End:

from tbotlib import tbot

tb.eof_call_tc("tc_workfd_get_uboot_config_vars.py")

def fdt_cmd_check(tb, cmd):
    tb.eof_write(tb.c_con, cmd)
    ret = tb.tbot_rup_error_on_strings(tb.c_con, ['FDT_ERR'])
    if ret == False:
        tb.end_tc(False)

tb.fdt_cmd_check = fdt_cmd_check

def fdt_cmdlist_check(tb, cmdlist):
    for cmd in cmdlist:
        tb.fdt_cmd_check(tb, cmd)

tb.set_board_state("u-boot")

tb.eof_write_cmd(tb.c_con, "help fdt", create_doc_event=True)

tb.event.create_event('main', 'tc_ub_duts_fdt.py', 'SET_DOC_FILENAME', 'fdt_addr_pre')

save = tb.workfd
tb.workfd = tb.c_ctrl
rem = tb.config.tftpdir + '/' + tb.config.tc_ub_tftp_path + "/u-boot.dtb"
tb.config.tc_workfd_check_if_file_exists_name = rem
ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
if ret == False:
    # if not exist, copy it to labPC
    loc = tb.workdir + '/src/files/duts/u-boot.dtb'
    tb.workfd.copy_file_tolabpc(loc, rem)
tb.workfd = save

tb.eof_write_cmd(tb.c_con, "tftpb " + tb.config.tc_ub_memory_ram_ws_base + " " + tb.config.tc_ub_tftp_path + "/u-boot.dtb")
tb.eof_call_tc("tc_ub_get_filesize.py")
tb.config.tc_ub_duts_fdt_mv_len = tb.ub_filesize
tb.eof_write_cmd(tb.c_con, "mw " + tb.config.tc_ub_memory_ram_ws_base + " 0 " + str(hex(2 * int(tb.ub_filesize, 16))))

tb.event.create_event('main', 'tc_ub_duts_fdt.py', 'SET_DOC_FILENAME', 'fdt_addr_prepare')

tb.eof_write_cmd(tb.c_con, "setenv fdt_addr_r " + tb.config.tc_ub_memory_ram_ws_base)
tb.eof_write_cmd(tb.c_con, "tftpb ${fdt_addr_r} " + tb.config.tc_ub_tftp_path + "/u-boot.dtb")

tb.event.create_event('main', 'tc_ub_duts_fdt.py', 'SET_DOC_FILENAME', 'fdt_addr')
fdt_cmd_check(tb, "fdt addr ${fdt_addr_r}")

tb.event.create_event('main', 'tc_ub_duts_fdt.py', 'SET_DOC_FILENAME', 'fdt_list')
fdt_cmd_check(tb, "fdt list /cpus")
tb.event.create_event('main', 'tc_ub_duts_fdt.py', 'SET_DOC_FILENAME', 'fdt_print')
fdt_cmd_check(tb, "fdt print /cpus")

tb.event.create_event('main', 'tc_ub_duts_fdt.py', 'SET_DOC_FILENAME', 'fdt_mknode')
cmdlist_mknode = [
  "fdt list /",
  "fdt mknode / testnode",
  "fdt list /",
  "fdt list /testnode",
]
fdt_cmdlist_check(tb, cmdlist_mknode)

tb.event.create_event('main', 'tc_ub_duts_fdt.py', 'SET_DOC_FILENAME', 'fdt_setnode')
cmdlist_setnode = [
  "fdt set /testnode testprop",
  "fdt set /testnode testprop testvalue",
  "fdt list /testnode",
]
fdt_cmdlist_check(tb, cmdlist_setnode)

tb.event.create_event('main', 'tc_ub_duts_fdt.py', 'SET_DOC_FILENAME', 'fdt_rmnode')
cmdlist_rmnode = [
  "fdt rm /testnode testprop",
  "fdt list /testnode",
  "fdt rm /testnode",
  "fdt list /",
]
fdt_cmdlist_check(tb, cmdlist_rmnode)

tb.config.tc_ub_duts_fdt_mv_addr = str(hex(int(tb.config.tc_ub_memory_ram_ws_base, 16) + int(tb.config.tc_ub_duts_fdt_mv_len, 16)))
tb.event.create_event('main', 'tc_ub_duts_fdt.py', 'SET_DOC_FILENAME', 'fdt_move_node')
tb.eof_write_cmd(tb.c_con, "fdt move ${fdt_addr_r} " + tb.config.tc_ub_duts_fdt_mv_addr + " " + tb.config.tc_ub_duts_fdt_mv_len)

tb.event.create_event('main', 'tc_ub_duts_fdt.py', 'SET_DOC_FILENAME', 'fdt_move_node_2')
cmdlist_rmnode = [
  "fdt list /",
  "fdt mknod / foobar",
  "fdt list /",
]
fdt_cmdlist_check(tb, cmdlist_rmnode)

tb.event.create_event('main', 'tc_ub_duts_fdt.py', 'SET_DOC_FILENAME', 'fdt_move_node_3')
tb.eof_write_cmd(tb.c_con, "fdt addr ${fdt_addr_r}")
tb.eof_write_cmd(tb.c_con, "fdt list /")

tb.event.create_event('main', 'tc_ub_duts_fdt.py', 'SET_DOC_FILENAME', 'fdt_chosen')
cmdlist_rmnode = [
  "fdt list /",
  "fdt chosen",
  "fdt list /",
  "fdt list /chosen",
]
fdt_cmdlist_check(tb, cmdlist_rmnode)


tb.end_tc(True)
