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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_duts_source.py
# do the commands needed for:
# http://www.denx.de/wiki/view/DULG/UBootCmdGroupExec#Section_5.9.4.1.
# U-Boots source command
#
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("u-boot")

if (tb.config.tc_ub_memory_ram_ws_base == 'undef'):
    # Try to get the SDRAM Base
    tb.uboot_config_option = 'CONFIG_SYS_SDRAM_BASE'
    tb.eof_call_tc("tc_workfd_get_uboot_config_hex.py")
    tb.config.tc_ub_memory_ram_ws_base = tb.config_result

cmdlist = [
"help source",
]

tb.eof_write_cmd_list(tb.c_con, cmdlist, create_doc_event=True)

c = tb.c_ctrl
tb.workfd = c
tb.eof_call_tc("tc_workfd_goto_tbot_workdir.py")
tb.eof_write_cmd(c, "pwd", create_doc_event=True)
tb.eof_write_cmd(c, "cat source_example.txt", create_doc_event=True)

cmd = 'mkimage -A ppc -O linux -T script -C none -a 0 -e 0 -n "autoscr example script" -d ' + \
  tb.config.tc_workfd_work_dir + '/source_example.txt ' + tb.config.tftprootdir + tb.config.tc_ub_tftp_path + '/source.scr'

self.event.create_event('main', 'tc_ub_duts_source.py', 'SET_DOC_FILENAME', 'source_mkimage')
tb.eof_write_cmd(c, cmd)

tb.workfd = tb.c_con

tb.config.tc_ub_tftp_file_addr = tb.config.tc_ub_memory_ram_ws_base
tb.config.tc_ub_tftp_file_name = tb.config.tc_ub_tftp_path + '/source_example.scr'
tb.eof_call_tc("tc_ub_tftp_file.py")

self.event.create_event('main', 'tc_ub_duts_source.py', 'SET_DOC_FILENAME', 'source_console')
cmd = 'imi ' + tb.config.tc_ub_memory_ram_ws_base
tb.eof_write_cmd(tb.c_con, cmd)

cmd = 'source ' + tb.config.tc_ub_memory_ram_ws_base
tb.eof_write_cmd(tb.c_con, cmd)

tb.end_tc(True)
