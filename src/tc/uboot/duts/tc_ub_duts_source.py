# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_duts_source.py
# do the commands needed for:
# http://www.denx.de/wiki/view/DULG/UBootCmdGroupExec#Section_5.9.4.1.
# U-Boots source command
#
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tb.eof_call_tc("tc_workfd_get_uboot_config_vars.py")

cmdlist = [
"help source",
]

tb.eof_write_cmd_list(tb.c_con, cmdlist, create_doc_event=True)

c = tb.c_ctrl
save = tb.workfd
tb.workfd = c
tb.eof_call_tc("tc_workfd_goto_tbot_workdir.py")

rem = tb.config.tc_workfd_work_dir + '/source_example.txt'

# check if file on remote (labPC) exist
tb.config.tc_workfd_check_if_file_exists_name = rem
ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
if ret == False:
    # if not exist, copy it to labPC
    loc = tb.workdir + '/src/files/duts/source_example.txt'
    tb.workfd.copy_file_tolabpc(loc, rem)

tb.eof_write_cmd(c, "pwd", create_doc_event=True)
tb.eof_write_cmd(c, "cat source_example.txt", create_doc_event=True)

cmd = 'mkimage -A ppc -O linux -T script -C none -a 0 -e 0 -n "autoscr example script" -d ' + \
  rem + ' ' + tb.config.tftpdir + '/' + tb.config.tc_ub_tftp_path + '/source_example.scr'

tb.event.create_event('main', 'tc_ub_duts_source.py', 'SET_DOC_FILENAME', 'source_mkimage')
tb.write_lx_cmd_check(c, cmd, split=c.line_length / 2)

tb.workfd = tb.c_con

tb.config.tc_ub_tftp_file_addr = tb.config.tc_ub_memory_ram_ws_base
tb.config.tc_ub_tftp_file_name = tb.config.tc_ub_tftp_path + '/source_example.scr'
tb.eof_call_tc("tc_ub_tftp_file.py")

self.event.create_event('main', 'tc_ub_duts_source.py', 'SET_DOC_FILENAME', 'source_console')
cmd = 'imi ' + tb.config.tc_ub_memory_ram_ws_base
tb.eof_write_cmd(tb.c_con, cmd)

cmd = 'source ' + tb.config.tc_ub_memory_ram_ws_base
tb.eof_write_cmd(tb.c_con, cmd)

tb.workfd= save
tb.end_tc(True)
