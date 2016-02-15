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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_eeprom.py
from tbotlib import tbot

#here starts the real test
logging.info("args: %s %s %s", tb.tc_lx_eeprom_file, tb.tc_lx_eeprom_tmp_dir, tb.tc_lx_eeprom_wp_gpio)
logging.info("args: %s %s %s %s", tb.tc_lx_eeprom_wp_val, tb.tc_lx_eeprom_wp_sz, tb.tc_lx_eeprom_wp_obs, tb.tc_lx_eeprom_wp_wc)

#set board state for which the tc is valid
tb.set_board_state("linux")

#read it into file
tmpfile = tb.tc_lx_eeprom_tmp_dir + 'eepromread'
tmp = 'cat ' + tb.tc_lx_eeprom_file + ' > ' + tmpfile
tb.eof_write_con_lx_cmd(tmp)

#dump first 256 bytes
tmp = 'hexdump -n 256 -C ' + tmpfile
tb.eof_write_con_lx_cmd(tmp)

#############################################
logging.info("check with WP pin protected")

#check if wp pin
if tb.tc_lx_eeprom_wp_gpio == 'none':
    logging.info("no WP pin, check only read eeprom")
    tb.end_tc(True)

#set WP pin into protected state
tb.tc_lx_gpio_nr = tb.tc_lx_eeprom_wp_gpio
tb.tc_lx_gpio_dir = 'out'
tb.tc_lx_gpio_val = tb.tc_lx_eeprom_wp_val
tb.eof_call_tc("tc_lx_gpio.py")

#############################################

#generate random file
randfile = tmpfile + '.random'
tmp = "dd if=/dev/urandom of=" + randfile + " bs=1 count=" + tb.tc_lx_eeprom_wp_sz
tb.eof_write_con_lx_cmd(tmp)

#write randomfile into eeprom
tmp = "dd if=" + randfile + " of=" + tb.tc_lx_eeprom_file + " bs=" + tb.tc_lx_eeprom_wp_obs + " count=" + tb.tc_lx_eeprom_wp_wc
tb.eof_write_con_lx_cmd(tmp)

#reread this data
tmpfile2 = tb.tc_lx_eeprom_tmp_dir + 'eepromread.new'
tmp = 'cat ' + tb.tc_lx_eeprom_file + ' > ' + tmpfile2
tb.eof_write_con_lx_cmd(tmp)

#compare it
tmp = 'cmp ' + randfile + ' ' + tmpfile2
tb.eof_write(tb.c_con, tmp)
tb.tbot_expect_prompt(tb.c_con)
#command must fail, as write should not work
tb.eof_write(tb.c_con, "if [ $? -ne 0 ]; then echo 'FAILED'; fi")
ret = tb.tbot_expect_string(tb.c_con, "FAILED")
if ret == 'prompt':
    tb.end_tc(False)
tb.tbot_expect_prompt(tb.c_con)

#############################################
logging.info("check with WP pin unprotected")

#set WP pin into unprotected state
tb.tc_lx_gpio_nr = tb.tc_lx_eeprom_wp_gpio
if tb.tc_lx_eeprom_wp_val == '1':
    tb.tc_lx_gpio_val='0'
else:
    tb.tc_lx_gpio_val='1'
tb.eof_call_tc("tc_lx_gpio.py")

#generate random file
randfile = tmpfile + '.random'
tmp = "dd if=/dev/urandom of=" + randfile + " bs=1 count=" + tb.tc_lx_eeprom_wp_sz
tb.eof_write_con_lx_cmd(tmp)

#write randomfile into eeprom
tmp = "dd if=" + randfile + " of=" + tb.tc_lx_eeprom_file + " bs=" + tb.tc_lx_eeprom_wp_obs + " count=" + tb.tc_lx_eeprom_wp_wc
tb.eof_write_con_lx_cmd(tmp)

#reread this data
tmpfile2 = tb.tc_lx_eeprom_tmp_dir + 'eepromread.new'
tmp = 'cat ' + tb.tc_lx_eeprom_file + ' > ' + tmpfile2
tb.eof_write_con_lx_cmd(tmp)

#compare it
tmp = 'cmp ' + randfile + ' ' + tmpfile2
tb.eof_write_con_lx_cmd(tmp)

#############################################
logging.info("restore original image")

#restore original
tmp = "dd if=" + tmpfile + " of=" + tb.tc_lx_eeprom_file + " bs=" + tb.tc_lx_eeprom_wp_obs + " count=" + tb.tc_lx_eeprom_wp_wc
tb.eof_write_con_lx_cmd(tmp)

#set WP pin into protected state
tb.tc_lx_gpio_nr = tb.tc_lx_eeprom_wp_gpio
tb.tc_lx_gpio_val = tb.tc_lx_eeprom_wp_val
tb.eof_call_tc("tc_lx_gpio.py")

tb.end_tc(True)
