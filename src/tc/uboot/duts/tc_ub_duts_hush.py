# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# create the logfiles needed for the U-Boot documentation
# used in src/documentation/u-boot-script.rst
#
# based on the DULG chapter:
# http://www.denx.de/wiki/view/DULG/CommandLineParsing
#
# End:

from tbotlib import tbot

logging.info("arg: ")

# set board state for which the tc is valid
tb.set_board_state("u-boot")

tb.eof_call_tc("tc_workfd_get_uboot_config_vars.py")

tb.event.create_event('main', 'tc_ub_duts_hush.py', 'SET_DOC_FILENAME', 'hush_example_1')
cmd = "setenv check 'if imi $addr; then echo Image OK; else echo Image corrupted!!; fi'"
tb.eof_write_cmd(tb.c_con, cmd)
tb.eof_write_cmd(tb.c_con, "print check")

cmd = "addr=" + tb.config.tc_ub_memory_ram_ws_base + " ; run check"
tb.eof_write_cmd(tb.c_con, cmd)

tb.event.create_event('main', 'tc_ub_duts_hush.py', 'SET_DOC_FILENAME', 'hush_example_2_prepare')
tb.config.tc_ub_tftp_file_addr = tb.config.tc_ub_memory_ram_ws_base_alt
tb.config.tc_ub_tftp_file_name = tb.config.tc_ub_tftp_path + '/source_example.scr'
tb.eof_call_tc("tc_ub_tftp_file.py")

tb.event.create_event('main', 'tc_ub_duts_hush.py', 'SET_DOC_FILENAME', 'hush_example_2')
cmd = "addr=" + tb.config.tc_ub_memory_ram_ws_base_alt + " ; run check"
tb.eof_write_cmd(tb.c_con, cmd)

tb.event.create_event('main', 'tc_ub_duts_hush.py', 'SET_DOC_FILENAME', 'hush_example_3_prepare')
cmd = 'mw ' + tb.config.tc_ub_memory_ram_ws_base + ' 0 100000'
tb.eof_write_cmd(tb.c_con, cmd)
cmd = 'mw ' + tb.config.tc_ub_memory_ram_ws_base_alt + ' 0 100000'
tb.eof_write_cmd(tb.c_con, cmd)
tb.event.create_event('main', 'tc_ub_duts_hush.py', 'SET_DOC_FILENAME', 'hush_example_3')
cmd = "addr1=" + tb.config.tc_ub_memory_ram_ws_base
tb.eof_write_cmd(tb.c_con, cmd)
cmd = "addr2=" + tb.config.tc_ub_memory_ram_ws_base_alt
tb.eof_write_cmd(tb.c_con, cmd)
cmd = "bootm $addr1 || bootm $addr2 || tftp " + tb.config.tc_ub_memory_ram_ws_base + " " + tb.config.tc_ub_tftp_path + '/source_example.scr' + ' && imi ' + tb.config.tc_ub_memory_ram_ws_base
tb.eof_write_cmd(tb.c_con, cmd)

tb.end_tc(True)
