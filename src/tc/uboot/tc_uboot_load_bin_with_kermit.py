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
# tbot.py -c -s lab_denx -c nero -t tc_uboot_load_bin_with_kermit.py
# start tc:
# load binary into ram with loadb
#
# precondition:
# kermit must be used
#
# steps:
# - loadb tb.config.tc_uboot_load_bin_ram_addr
# - leave kermit
# - send tb.config.tc_uboot_load_bin_file
#   protocol: kermit_protocol='kermit'
# wait for "C-Kermit>"
# connect
# you must get back something like this:
# ## Total Size      = 0x00050bc0 = 330688 Bytes
# ## Start Addr      = 0x81000000
# End:

from tbotlib import tbot

try:
    tb.config.tc_uboot_load_bin_ram_addr
except:
    tb.config.tc_uboot_load_bin_ram_addr = '81000000'

try:
    tb.config.tc_uboot_load_bin_file
except:
    tb.config.tc_uboot_load_bin_file = '/home/alka/tbot/nero-images/u-boot.img '

logging.info("args: %s", tb.config.tc_uboot_load_bin_ram_addr)
logging.info("args: %s", tb.config.tc_uboot_load_bin_file)

kermit_protocol = 'kermit'

# set workfd to the connection we want to work on
tb.workfd = tb.c_con
c = tb.workfd

cmd = 'loadb ' + tb.config.tc_uboot_load_bin_ram_addr
tb.eof_write(c, cmd)
tmp = 'Ready for binary (kermit) download to 0x' + tb.config.tc_uboot_load_bin_ram_addr
tb.tbot_expect_string(c, tmp)

# enter kermit
string = pack('h', 28)
string = string[:1]
c.send_raw(string)
c.send_raw('C')
c.set_prompt('C-Kermit>')
c.expect_prompt()

# send file
cmd = 'send /protocol=' + kermit_protocol + ' ' + tb.config.tc_uboot_load_bin_file
tb.eof_write(c, cmd)

# check error output from kermit:
# 'bertragung nicht abgeschlossen', 'Maximale Wiederholungsanzahl'
# ToDo

# at the end we expect kermit prompt
c.expect_prompt()

# connect to console, and expect U-Boot prompt
tb.eof_write(c, 'connect')
c.set_prompt(tb.config.uboot_prompt)
tb.eof_expect_string(c, 'Total Size', wait_prompt=False)
tb.eof_expect_string(c, 'Start Addr', wait_prompt=False)
tb.tbot_expect_prompt(c)

tb.end_tc(True)
