# SPDX-License-Identifier: GPL-2.0
#
# Description:
# Test an eeprom:
# - read the content from eeprom @ tb.config.tc_lx_eeprom_tmp_dir
#   with "cat" into tmpfile
# - check tb.config.tc_lx_eeprom_wp_gpio != 'none'
#   if WP pin works
# - generate random file with tb.config.tc_lx_eeprom_wp_sz size
# - write it into eeprom
# - reread it
# - compare it with original
# - restore original eeprom content at end
#
# used variables
#
# - tb.config.tc_lx_eeprom_file
#| linux path to eeprom
#| default: '/sys/class/i2c-dev/i2c-0/device/0-0050/eeprom'
#
# - tb.config.tc_lx_eeprom_tmp_dir
#| temp directory, where eeprom content get stored
#| default: tb.config.lab_tmp_dir
#
# - tb.config.tc_lx_eeprom_wp_gpio
#| if 'none' check only if eeprom is readable
#| else check also if wp pin tb.config.tc_lx_eeprom_wp_gpio works
#| default: 'none'
#
# - tb.config.tc_lx_eeprom_wp_val
#| gpio protected state '0' or '1'
#| default: '0'
#
# - tb.config.tc_lx_eeprom_wp_sz
#| size of eeprom test
#| default: '4096'
#
# - tb.config.tc_lx_eeprom_wp_obs
#| dd obs size for writting into eeprom
#| default: '32'
#
# - tb.config.tc_lx_eeprom_wp_wc
#| dd count size for writting into eeprom
#| default: '128'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_lx_eeprom_file', '/sys/class/i2c-dev/i2c-0/device/0-0050/eeprom')
tb.define_variable('tc_lx_eeprom_tmp_dir', tb.config.lab_tmp_dir)
tb.define_variable('tc_lx_eeprom_wp_gpio', 'none')
tb.define_variable('tc_lx_eeprom_wp_val', '0')
tb.define_variable('tc_lx_eeprom_wp_sz', '4096')
tb.define_variable('tc_lx_eeprom_wp_obs', '32')
tb.define_variable('tc_lx_eeprom_wp_wc', '128')

# set board state for which the tc is valid
tb.set_board_state("linux")

# read it into file
tmpfile = tb.config.tc_lx_eeprom_tmp_dir + 'eepromread'
tmp = 'cat ' + tb.config.tc_lx_eeprom_file + ' > ' + tmpfile
tb.eof_write_con_lx_cmd(tmp)

# dump first 256 bytes
tmp = 'hexdump -n 256 -C ' + tmpfile
tb.eof_write_con_lx_cmd(tmp)

#############################################
logging.info("check with WP pin protected")

# check if wp pin
if tb.config.tc_lx_eeprom_wp_gpio == 'none':
    logging.info("no WP pin, check only read eeprom")
    tb.end_tc(True)

# set WP pin into protected state
tb.config.tc_lx_gpio_nr = tb.config.tc_lx_eeprom_wp_gpio
tb.config.tc_lx_gpio_dir = 'out'
tb.config.tc_lx_gpio_val = tb.config.tc_lx_eeprom_wp_val
tb.eof_call_tc("tc_lx_gpio.py")

#############################################

# generate random file
randfile = tmpfile + '.random'
tmp = "dd if=/dev/urandom of=" + randfile + " bs=1 count=" + tb.config.tc_lx_eeprom_wp_sz
tb.eof_write_con_lx_cmd(tmp)

# write randomfile into eeprom
tmp = "dd if=" + randfile + " of=" + tb.config.tc_lx_eeprom_file + " bs=" + tb.config.tc_lx_eeprom_wp_obs + " count=" + tb.config.tc_lx_eeprom_wp_wc
tb.eof_write_con_lx_cmd(tmp)

# reread this data
tmpfile2 = tb.config.tc_lx_eeprom_tmp_dir + 'eepromread.new'
tmp = 'cat ' + tb.config.tc_lx_eeprom_file + ' > ' + tmpfile2
tb.eof_write_con_lx_cmd(tmp)

# compare it
tmp = 'cmp ' + randfile + ' ' + tmpfile2
tb.eof_write(tb.c_con, tmp)
tb.tbot_expect_prompt(tb.c_con)
# command must fail, as write should not work
tb.eof_write(tb.c_con, "if [ $? -ne 0 ]; then echo 'FAILED'; fi")
ret = tb.tbot_expect_string(tb.c_con, "FAILED")
if ret == 'prompt':
    tb.end_tc(False)
tb.tbot_expect_prompt(tb.c_con)

#############################################
logging.info("check with WP pin unprotected")

# set WP pin into unprotected state
tb.config.tc_lx_gpio_nr = tb.config.tc_lx_eeprom_wp_gpio
if tb.config.tc_lx_eeprom_wp_val == '1':
    tb.config.tc_lx_gpio_val='0'
else:
    tb.config.tc_lx_gpio_val='1'
tb.eof_call_tc("tc_lx_gpio.py")

# generate random file
randfile = tmpfile + '.random'
tmp = "dd if=/dev/urandom of=" + randfile + " bs=1 count=" + tb.config.tc_lx_eeprom_wp_sz
tb.eof_write_con_lx_cmd(tmp)

# write randomfile into eeprom
tmp = "dd if=" + randfile + " of=" + tb.config.tc_lx_eeprom_file + " bs=" + tb.config.tc_lx_eeprom_wp_obs + " count=" + tb.config.tc_lx_eeprom_wp_wc
tb.eof_write_con_lx_cmd(tmp)

# reread this data
tmpfile2 = tb.config.tc_lx_eeprom_tmp_dir + 'eepromread.new'
tmp = 'cat ' + tb.config.tc_lx_eeprom_file + ' > ' + tmpfile2
tb.eof_write_con_lx_cmd(tmp)

# compare it
tmp = 'cmp ' + randfile + ' ' + tmpfile2
tb.eof_write_con_lx_cmd(tmp)

#############################################
logging.info("restore original image")

# restore original
tmp = "dd if=" + tmpfile + " of=" + tb.config.tc_lx_eeprom_file + " bs=" + tb.config.tc_lx_eeprom_wp_obs + " count=" + tb.config.tc_lx_eeprom_wp_wc
tb.eof_write_con_lx_cmd(tmp)

# set WP pin into protected state
tb.config.tc_lx_gpio_nr = tb.config.tc_lx_eeprom_wp_gpio
tb.config.tc_lx_gpio_val = tb.config.tc_lx_eeprom_wp_val
tb.eof_call_tc("tc_lx_gpio.py")

tb.end_tc(True)
