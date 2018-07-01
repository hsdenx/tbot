# SPDX-License-Identifier: GPL-2.0
#
# Description:
# load binary into ram with loadb
#
# if tb.config.tc_uboot_load_bin_with_kermit_possible != 'yes'
# do nothing return True
# default: 'yes'
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
#
# used variables
#
# - tb.config.tc_uboot_load_bin_with_kermit_possible
#| if != 'yes' return True, do nothing
#| default: 'yes'
#
# - tb.config.tc_uboot_load_bin_ram_addr
#| RAM address to which file get loaded
#| default: '81000000'
#
# - tb.config.tc_uboot_load_bin_file
#| filename which get loaded with kermit
#| default: '/home/alka/tbot/nero-images/u-boot.img'
#
# - tb.config.tc_uboot_load_bin_with_kermit_kermit_settings
#| kermit settings, known to work good
#| default: 
#| [
#|    "set carrier-watch off",
#|     "set handshake none",
#|     "set flow-control none",
#|     "robust",
#|     "set file type bin",
#|     "set file name lit",
#|     "set rec pack 100",
#|     "set send pack 100",
#|     "set window 5",
#| ]'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_uboot_load_bin_with_kermit_possible', 'yes')
tb.define_variable('tc_uboot_load_bin_ram_addr', '81000000')
tb.define_variable('tc_uboot_load_bin_file', '/home/alka/tbot/nero-images/u-boot.img')
tb.define_variable('tc_uboot_load_bin_with_kermit_kermit_settings', '
[
    "set carrier-watch off",
    "set handshake none",
    "set flow-control none",
    "robust",
    "set file type bin",
    "set file name lit",
    "set rec pack 100",
    "set send pack 100",
    "set window 5",
]')

if tb.config.tc_uboot_load_bin_with_kermit_possible != 'yes':
    tb.end_tc(True)

kermit_protocol = 'kermit'

tb.event.create_event('main', 'tc_uboot_load_bin_with_kermit.py', 'SET_DOC_FILENAME', 'loadb_run')

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
c.set_prompt('C-Kermit>', 'linux')
c.expect_prompt()

tb.event.create_event('main', 'tc_uboot_load_bin_with_kermit.py', 'SET_DOC_FILENAME', 'loadb_kermit_settings')
for cmd in tb.config.tc_uboot_load_bin_with_kermit_kermit_settings:
    tb.eof_write_cmd(tb.workfd, cmd, start=False)

# send file
tb.event.create_event('main', 'tc_uboot_load_bin_with_kermit.py', 'SET_DOC_FILENAME', 'loadb_send_file')
cmd = 'send /protocol=' + kermit_protocol + ' ' + tb.config.tc_uboot_load_bin_file
tb.eof_write(c, cmd)

# check error output from kermit:
# 'bertragung nicht abgeschlossen', 'Maximale Wiederholungsanzahl'
# ToDo

# at the end we expect kermit prompt
c.expect_prompt()

# connect to console, and expect U-Boot prompt
tb.eof_write(c, 'connect')
c.set_prompt(tb.config.uboot_prompt, 'u-boot')
tb.eof_expect_string(c, 'Total Size', wait_prompt=False)
tb.eof_expect_string(c, 'Start Addr', wait_prompt=False)
tb.tbot_expect_prompt(c)

tb.end_tc(True)
