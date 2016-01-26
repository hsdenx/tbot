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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_ub_memory.py
# convert duts tests from:
# http://git.denx.de/?p=duts.git;a=blob;f=testsystems/dulg/testcases/10_UBootMemory.tc;h=f5fb055499db17c322859215ab489cefb063ac47;hb=101ddd5dbd547d5046363358d560149d873b238a
from tbotlib import tbot

logging.info("args: %s %s %s", tb.tc_ub_memory_ram_ws_base, tb.tc_ub_memory_ram_ws_base_alt, tb.tc_ub_memory_ram_big)

if (tb.tc_ub_memory_ram_ws_base == 'undef'):
    # Try to get the SDRAM Base
    tb.uboot_config_option = 'CONFIG_SYS_SDRAM_BASE'
    tb.eof_call_tc("tc_workfd_get_uboot_config_hex.py")
    tb.tc_ub_memory_ram_ws_base = tb.config_result

if (tb.tc_ub_memory_ram_ws_base_alt == 'undef'):
    try:
        tmp = int(tb.tc_ub_memory_ram_ws_base, 16)
    except:
        tb.end_tc(False)
    tmp += 1024 * 1024
    tb.tc_ub_memory_ram_ws_base_alt = hex(tmp)

if (tb.tc_ub_memory_ram_big == 'undef'):
    # Try to get CONFIG_SYS_ARCH
    tb.uboot_config_option = 'CONFIG_SYS_ARCH'
    tb.eof_call_tc("tc_workfd_get_uboot_config_string.py")
    if tb.tc_ub_memory_ram_big == 'powerpc':
        tb.tc_ub_memory_ram_big = 'yes'
    else:
        tb.tc_ub_memory_ram_big = 'no'

logging.info("args: %s %s %s", tb.tc_ub_memory_ram_ws_base, tb.tc_ub_memory_ram_ws_base_alt, tb.tc_ub_memory_ram_big)
#set board state for which the tc is valid
tb.set_board_state("u-boot")

basecmdlist = [
"base",
"md 0 0xc",
"base " + tb.tc_ub_memory_ram_ws_base,
"md 0 0xc",
"md 0 0x40",
"base 0",
]

tb.eof_write_cmd(tb.channel_con, "help base")
tb.eof_write_cmd_list(tb.channel_con, basecmdlist)

tmp = int(tb.tc_ub_memory_ram_ws_base, 16)
tmp += 4
tmp = hex(tmp)
tb.eof_write_cmd(tb.channel_con, "crc " + tmp + " 0x3fc")

tb.eof_write_cmd(tb.channel_con, "crc " + tmp + " 0x3fc" + " " + tb.tc_ub_memory_ram_ws_base)
tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 4")
tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 0x40")

# crc check
tb.eof_write_cmd(tb.channel_con, "mw " + tb.tc_ub_memory_ram_ws_base + " 0xc0cac01a 0x100")
tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 0x100")
if tb.tc_ub_memory_ram_big == 'yes': 
    tb.eof_write_cmd_check(tb.channel_con, "crc " + tmp + " 0x3fc", "5db8222f")
else:
    tb.eof_write_cmd_check(tb.channel_con, "crc " + tmp + " 0x3fc", "5caee82a")

tb.eof_write_cmd(tb.channel_con, "mw " + tb.tc_ub_memory_ram_ws_base + " 0x00c0ffee 0x100")
tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 0x100")
if tb.tc_ub_memory_ram_big == 'yes': 
    tb.eof_write_cmd_check(tb.channel_con, "crc " + tmp + " 0x3fc", "de3ac1b8")
else:
    tb.eof_write_cmd_check(tb.channel_con, "crc " + tmp + " 0x3fc", "56a87cac")

# cmp
tb.eof_write_cmd(tb.channel_con, "help cmp")

#generate random file, and tftp it twice
tb.workfd = tb.channel_ctrl
tb.tc_workfd_generate_random_file_name = tb.tc_ub_tftp_path + "random"
tb.tc_workfd_generate_random_file_length = '1048576'
tb.eof_call_tc("tc_workfd_generate_random_file.py")
tb.tc_ub_tftp_file_addr = tb.tc_ub_memory_ram_ws_base
tb.tc_ub_tftp_file_name = tb.tc_workfd_generate_random_file_name
tb.eof_call_tc("tc_ub_tftp_file.py")
tb.tc_ub_tftp_file_addr = tb.tc_ub_memory_ram_ws_base_alt
tb.eof_call_tc("tc_ub_tftp_file.py")

# compare
ret = tb.write_cmd_check(tb.channel_con, "cmp " + tb.tc_ub_memory_ram_ws_base + " " + tb.tc_ub_memory_ram_ws_base_alt + " 40000", "!=")
if ret == True:
    tb.end_tc(False)
tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 0xc")
tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base_alt + " 0xc")
tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 0x40")

ret = tb.write_cmd_check(tb.channel_con, "cmp.l " + tb.tc_ub_memory_ram_ws_base + " " + tb.tc_ub_memory_ram_ws_base_alt + " 40000", "!=")
if ret == True:
    tb.end_tc(False)
ret = tb.write_cmd_check(tb.channel_con, "cmp.w " + tb.tc_ub_memory_ram_ws_base + " " + tb.tc_ub_memory_ram_ws_base_alt + " 80000", "!=")
if ret == True:
    tb.end_tc(False)
ret = tb.write_cmd_check(tb.channel_con, "cmp.b " + tb.tc_ub_memory_ram_ws_base + " " + tb.tc_ub_memory_ram_ws_base_alt + " 100000", "!=")
if ret == True:
    tb.end_tc(False)

# cp
tb.eof_write_cmd(tb.channel_con, "help cp")
tb.eof_write_cmd(tb.channel_con, "cp " + tb.tc_ub_memory_ram_ws_base + " " + tb.tc_ub_memory_ram_ws_base_alt + " 10000")

tb.eof_write_cmd(tb.channel_con, "cp.l " + tb.tc_ub_memory_ram_ws_base + " " + tb.tc_ub_memory_ram_ws_base_alt + " 10000")
tb.eof_write_cmd(tb.channel_con, "cp.w " + tb.tc_ub_memory_ram_ws_base + " " + tb.tc_ub_memory_ram_ws_base_alt + " 20000")
tb.eof_write_cmd(tb.channel_con, "cp.b " + tb.tc_ub_memory_ram_ws_base + " " + tb.tc_ub_memory_ram_ws_base_alt + " 40000")

# md
tb.eof_write_cmd(tb.channel_con, "help md")
tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base)

tb.eof_write_cmd(tb.channel_con, "md.w " + tb.tc_ub_memory_ram_ws_base)
tb.eof_write_cmd(tb.channel_con, "md.b " + tb.tc_ub_memory_ram_ws_base)

tb.eof_write_cmd(tb.channel_con, "md.b " + tb.tc_ub_memory_ram_ws_base + " 0x20")
tb.eof_write_cmd(tb.channel_con, "md.w " + tb.tc_ub_memory_ram_ws_base)
tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base)

tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 0x40")

# mm
tb.eof_write_cmd(tb.channel_con, "help mm")

def tbot_read_write(tb, string, cmd):
    searchlist = [string]
    tmp = True
    cmd_ok = False
    while tmp == True:
        tmp = tb.readline_and_search_strings(tb.channel_con, searchlist)
        if tmp == 0:
            tb.eof_write_con(cmd)
            cmd_ok = True
            tmp = False
        elif tmp == 'prompt':
            tmp = False
        else:
            #endless loop
            tmp = True
    return cmd_ok

def tbot_send_list(tb, mm_list):
    for cmd in mm_list:
        string = raw("?")
        searchlist = [string]
        tmp = True
        cmd_ok = False
        while tmp == True:
            tmp = tb.readline_and_search_strings(tb.channel_con, searchlist)
            if tmp == 0:
                tb.eof_write_con(cmd)
                cmd_ok = True
                tmp = False
            elif tmp == 'prompt':
                tmp = False
            else:
                #endless loop
                tmp = True
        if cmd_ok != True:
            tb.send_ctrl_c(tb.channel_con)
            tb.eof_read_end_state_con(1)
            tb.end_tc(False)

mm_list = [
"0", "0xaabbccdd", "0x01234567"
]
tb.eof_write_con("mm " +  tb.tc_ub_memory_ram_ws_base)
tbot_send_list(tb, mm_list)
tb.send_ctrl_c(tb.channel_con)
tb.eof_read_end_state_con(1)
tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 10")

mm_list = [
"0x0101", "0x0202", "0x4321", "0x8765"
]
tb.eof_write_con("mm.w " +  tb.tc_ub_memory_ram_ws_base)
tbot_send_list(tb, mm_list)
tb.send_ctrl_c(tb.channel_con)
tb.eof_read_end_state_con(1)

tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 10")

mm_list = [
"0x48", "0x65", "0x6c", "0x6c", "0x6f", "0x20", "0x20",  "0x20",
]
tb.eof_write_con("mm.b " +  tb.tc_ub_memory_ram_ws_base)
tbot_send_list(tb, mm_list)
tb.send_ctrl_c(tb.channel_con)
tb.eof_read_end_state_con(1)

tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 10")

#mtest
ret = tb.write_cmd_check(tb.channel_con, "help mtest", "Unknown command")
if ret == False:
    sz = int(tb.tc_ub_memory_ram_ws_base, 16)
    sz += 1024 * 1024
    sz = hex(sz)
    tb.eof_write_cmd_check(tb.channel_con, "mtest " + tb.tc_ub_memory_ram_ws_base + " " + sz, "0000000f")
    tb.send_ctrl_c(tb.channel_con)
    tb.eof_read_end_state_con(1)

# mw
ret = tb.write_cmd_check(tb.channel_con, "help mw", "Unknown command")
if ret == False:
    tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 0x10")
    tb.eof_write_cmd(tb.channel_con, "mw " + tb.tc_ub_memory_ram_ws_base + " 0xaabbccdd")
    tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 0x10")
    tb.eof_write_cmd(tb.channel_con, "mw " + tb.tc_ub_memory_ram_ws_base + " 0 6")
    tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 0x10")
    tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 0x40")

    tb.eof_write_cmd(tb.channel_con, "mw.w " + tmp + " 0x1155 6")
    tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 0x10")
    tmp = int(tb.tc_ub_memory_ram_ws_base, 16)
    tmp += 7
    tmp = hex(tmp)
    tb.eof_write_cmd(tb.channel_con, "mw.b " + tmp + " 0xff 7")
    tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 0x10")

    tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 0x40")

#nm
ret = tb.write_cmd_check(tb.channel_con, "help nm", "Unknown command")
if ret == False:
    nm_list = [
    "0x48", "0x65", "0x6c", "0x6c", "0x6f"
    ]
    tb.eof_write_con("nm " +  tb.tc_ub_memory_ram_ws_base)
    tbot_send_list(tb, nm_list)
    tb.send_ctrl_c(tb.channel_con)
    tb.eof_read_end_state_con(1)

    tb.eof_write_cmd(tb.channel_con, "md " + tb.tc_ub_memory_ram_ws_base + " 10")

ret = tb.write_cmd_check(tb.channel_con, "help loop", "Unknown command")

tb.end_tc(True)
