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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_memory.py
# convert duts tests from:
# http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootMemory.tc;h=f5fb055499db17c322859215ab489cefb063ac47;hb=101ddd5dbd547d5046363358d560149d873b238a
#
# disable "base" only command with
# tb.config.tc_ub_memory_base = 'no'
# default: 'yes'
# End:

from tbotlib import tbot

tb.eof_call_tc("tc_workfd_get_uboot_config_vars.py")

logging.info("args: %s %s %s", tb.config.tc_ub_memory_ram_ws_base, tb.config.tc_ub_memory_ram_ws_base_alt,
             tb.config.tc_ub_memory_ram_big)
# set board state for which the tc is valid
tb.set_board_state("u-boot")

basecmdlist = [
"base",
"md " + tb.config.tc_ub_memory_ram_ws_base + " 0xc",
]

basecmdlist2 = [
"base 100000",
"md " + tb.config.tc_ub_memory_ram_ws_base + " 0xc",
"md " + tb.config.tc_ub_memory_ram_ws_base + " 0x40",
"base 0",
]

tb.eof_write_cmd(tb.c_con, "help base")
if tb.config.tc_ub_memory_base == 'yes':
    tb.c_con.set_check_error(False)
    tb.eof_write_cmd_list(tb.c_con, basecmdlist, create_doc_event=True)
    tb.c_con.set_check_error(True)

tb.eof_write_cmd_list(tb.c_con, basecmdlist2, create_doc_event=True)


tmp = int(tb.config.tc_ub_memory_ram_ws_base, 16)
tmp += 4
tmp = hex(tmp)
tb.eof_write_cmd(tb.c_con, "crc " + tmp + " 0x3fc", create_doc_event=True)

tb.eof_write_cmd(tb.c_con, "crc " + tmp + " 0x3fc" + " " + tb.config.tc_ub_memory_ram_ws_base, create_doc_event=True)
tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 4")
tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 0x40", create_doc_event=True)

# crc check
tb.eof_write_cmd(tb.c_con, "mw " + tb.config.tc_ub_memory_ram_ws_base + " 0xc0cac01a 0x100")
tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 0x100")
if tb.config.tc_ub_memory_ram_big == 'yes': 
    tb.eof_write_cmd_check(tb.c_con, "crc " + tmp + " 0x3fc", "5db8222f")
else:
    tb.eof_write_cmd_check(tb.c_con, "crc " + tmp + " 0x3fc", "5caee82a")

tb.eof_write_cmd(tb.c_con, "mw " + tb.config.tc_ub_memory_ram_ws_base + " 0x00c0ffee 0x100")
tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 0x100")
if tb.config.tc_ub_memory_ram_big == 'yes': 
    tb.eof_write_cmd_check(tb.c_con, "crc " + tmp + " 0x3fc", "de3ac1b8")
else:
    tb.eof_write_cmd_check(tb.c_con, "crc " + tmp + " 0x3fc", "56a87cac")

# cmp
tb.eof_write_cmd(tb.c_con, "help cmp", create_doc_event=True)

# generate random file, and tftp it twice
tb.workfd = tb.c_ctrl
tb.tc_workfd_generate_random_file_name = tb.config.tftprootdir + tb.config.tc_ub_tftp_path + "random"
tb.tc_workfd_generate_random_file_length = '1048576'
tb.eof_call_tc("tc_workfd_generate_random_file.py")
tb.config.tc_ub_tftp_file_addr = tb.config.tc_ub_memory_ram_ws_base
tb.config.tc_ub_tftp_file_name = tb.config.tc_ub_tftp_path + "random"
tb.eof_call_tc("tc_ub_tftp_file.py")
tb.config.tc_ub_tftp_file_addr = tb.config.tc_ub_memory_ram_ws_base_alt
tb.eof_call_tc("tc_ub_tftp_file.py")

# compare
self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'cmp_fail')
ret = tb.write_cmd_check(tb.c_con, "cmp " + tb.config.tc_ub_memory_ram_ws_base + " "
                         + tb.config.tc_ub_memory_ram_ws_base_alt + " 40000", "!=")
if ret == True:
    tb.end_tc(False)
tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 0xc")
tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base_alt + " 0xc")

self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'cmp_fail_big')
tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 0x40")

self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'cmp_long')
ret = tb.write_cmd_check(tb.c_con, "cmp.l " + tb.config.tc_ub_memory_ram_ws_base +
          " " + tb.config.tc_ub_memory_ram_ws_base_alt + " 40000", "!=")
if ret == True:
    tb.end_tc(False)
ret = tb.write_cmd_check(tb.c_con, "cmp.w " + tb.config.tc_ub_memory_ram_ws_base +
          " " + tb.config.tc_ub_memory_ram_ws_base_alt + " 80000", "!=")
if ret == True:
    tb.end_tc(False)
ret = tb.write_cmd_check(tb.c_con, "cmp.b " + tb.config.tc_ub_memory_ram_ws_base +
          " " + tb.config.tc_ub_memory_ram_ws_base_alt + " 100000", "!=")
if ret == True:
    tb.end_tc(False)

# cp
tb.eof_write_cmd(tb.c_con, "help cp", create_doc_event=True)
self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'cp_basic')
tb.eof_write_cmd(tb.c_con, "cp " + tb.config.tc_ub_memory_ram_ws_base + " " + tb.config.tc_ub_memory_ram_ws_base_alt + " 10000")

self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'cp_extensions')
tb.eof_write_cmd(tb.c_con, "cp.l " + tb.config.tc_ub_memory_ram_ws_base + " " + tb.config.tc_ub_memory_ram_ws_base_alt + " 10000")
tb.eof_write_cmd(tb.c_con, "cp.w " + tb.config.tc_ub_memory_ram_ws_base + " " + tb.config.tc_ub_memory_ram_ws_base_alt + " 20000")
tb.eof_write_cmd(tb.c_con, "cp.b " + tb.config.tc_ub_memory_ram_ws_base + " " + tb.config.tc_ub_memory_ram_ws_base_alt + " 40000")

# md
tb.eof_write_cmd(tb.c_con, "help md", create_doc_event=True)
self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'md_basic')
tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base)

self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'md_extensions')
tb.eof_write_cmd(tb.c_con, "md.w " + tb.config.tc_ub_memory_ram_ws_base)
tb.eof_write_cmd(tb.c_con, "md.b " + tb.config.tc_ub_memory_ram_ws_base)

self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'md_remember')
tb.eof_write_cmd(tb.c_con, "md.b " + tb.config.tc_ub_memory_ram_ws_base + " 0x20")
tb.eof_write_cmd(tb.c_con, "md.w " + tb.config.tc_ub_memory_ram_ws_base)
tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base)

self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'md_reset')
tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 0x40")

# mm
tb.eof_write_cmd(tb.c_con, "help mm", create_doc_event=True)

def tbot_read_write(tb, string, cmd):
    searchlist = [string]
    tmp = True
    cmd_ok = False
    while tmp == True:
        ret = tb.tbot_rup_and_check_strings(tb.c_con, searchlist)
        if ret == '0':
            tb.eof_write_con(cmd, False)
            cmd_ok = True
        elif ret == 'prompt':
            tmp = False
    return cmd_ok

def tbot_send_list(tb, mm_list):
    for cmd in mm_list:
        string = '?'
        searchlist = [string]
        tmp = True
        ret = tb.tbot_rup_and_check_strings(tb.c_con, searchlist)
        if ret == '0':
            tb.eof_write_con(cmd, False)

    tb.c_con.expect_prompt()

mm_list = [
"0", "0xaabbccdd", "0x01234567", "."
]

self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'mm_first')
tb.eof_write_con("mm " +  tb.config.tc_ub_memory_ram_ws_base)

tbot_send_list(tb, mm_list)

tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 10")

mm_list = [
"0x0101", "0x0202", "0x4321", "0x8765", "."
]
self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'mm_second')
tb.eof_write_con("mm.w " +  tb.config.tc_ub_memory_ram_ws_base)
tbot_send_list(tb, mm_list)

tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 10")

mm_list = [
"0x48", "0x65", "0x6c", "0x6c", "0x6f", "0x20", "0x20",  "0x20", "."
]
self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'mm_third')
tb.eof_write_con("mm.b " +  tb.config.tc_ub_memory_ram_ws_base)
tbot_send_list(tb, mm_list)

tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 10")

# mtest
ret = tb.write_cmd_check(tb.c_con, "help mtest", "Unknown command", create_doc_event=True)
if ret == False:
    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'mtest_run')
    sz = int(tb.config.tc_ub_memory_ram_ws_base, 16)
    sz += 1024 * 1024
    sz = hex(sz)
    tb.eof_write(tb.c_con, "mtest " + tb.config.tc_ub_memory_ram_ws_base + " " + sz)
    # check here for "Testing" then for "Pattern 00000000  Writing...  Reading...Iteration"
    # then stop
    tb.send_ctrl_c(tb.c_con)
    tb.c_con.expect_prompt()

# mw
ret = tb.write_cmd_check(tb.c_con, "help mw", "Unknown command", create_doc_event=True)
if ret == False:
    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'mw_run')
    tmp = int(tb.config.tc_ub_memory_ram_ws_base, 16)
    tmp += 4
    tmp = hex(tmp)
    tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 0x10")
    tb.eof_write_cmd(tb.c_con, "mw " + tb.config.tc_ub_memory_ram_ws_base + " 0xaabbccdd")
    tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 0x10")
    tb.eof_write_cmd(tb.c_con, "mw " + tb.config.tc_ub_memory_ram_ws_base + " 0 6")
    tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 0x10")
    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'mw_reset')
    tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 0x40")

    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'mw_run2')
    tb.eof_write_cmd(tb.c_con, "mw.w " + tmp + " 0x1155 6")
    tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 0x10")
    tmp = int(tb.config.tc_ub_memory_ram_ws_base, 16)
    tmp += 7
    tmp = hex(tmp)
    tb.eof_write_cmd(tb.c_con, "mw.b " + tmp + " 0xff 7")
    tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 0x10")

    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'mw_reset')
    tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 0x40")

# nm
ret = tb.write_cmd_check(tb.c_con, "help nm", "Unknown command", create_doc_event=True)
if ret == False:
    self.event.create_event('main', 'tc_ub_memory.py', 'SET_DOC_FILENAME', 'nm_run')
    nm_list = [
    "0x48", "0x65", "0x6c", "0x6c", "0x6f", "."
    ]
    tb.eof_write_con("nm " +  tb.config.tc_ub_memory_ram_ws_base)
    tbot_send_list(tb, nm_list)

    tb.eof_write_cmd(tb.c_con, "md " + tb.config.tc_ub_memory_ram_ws_base + " 10")

ret = tb.write_cmd_check(tb.c_con, "help loop", "Unknown command", create_doc_event=True)

tb.end_tc(True)
