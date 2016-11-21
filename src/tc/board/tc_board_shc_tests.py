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
# tbot.py -s lab_denx -c shc -t tc_board_shc_tests.py
# start all testcases for the shc board
# End:

from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("u-boot")

tb.statusprint("tc_shc u-boot setenv")
#call ubot setenv
tb.eof_call_tc("tc_ub_setenv.py")

tb.statusprint("tc_shc linux dmesg checks")
checks = ['SHC',
	'input: gpio_keys',
	'rtc-pcf8563',
	'tps65217 0-0024',
	'at24 0-0050',
	'Detected MACID',
	'usb 1-1: Device is not authorized for usage',
	'input: gpio_keys as',
	'mmc0: new SDHC card at address aaaa',
	'mmc1: new high speed MMC card at address 0001']

for tb.config.tc_lx_dmesg_grep_name in checks:
    tb.eof_call_tc("tc_lx_dmesg_grep.py")

tb.workfd = tb.c_con
tb.statusprint("tc_shc pinmux check")
tb.eof_call_tc("tc_lx_check_reg_file.py")

tb.set_board_state("linux")
# do some basic tests
tb.statusprint("tc_fipad basic checks")
basiclist = [
	{"cmd":"cat /sys/class/leds/shc\:cloud\:bl/trigger", "val":"[none] mmc0 mmc1 timer timer-sync oneshot heartbeat backlight gpio cpu0 default-on"},
	{"cmd":"cat /sys/class/leds/shc\:cloud\:red/trigger", "val":"[none] mmc0 mmc1 timer timer-sync oneshot heartbeat backlight gpio cpu0 default-on"},
	{"cmd":"cat /sys/class/leds/shc\:lan\:bl/trigger", "val":"[none] mmc0 mmc1 timer timer-sync oneshot heartbeat backlight gpio cpu0 default-on"},
	{"cmd":"cat /sys/class/leds/shc\:lan\:red/trigger", "val":"[none] mmc0 mmc1 timer timer-sync oneshot heartbeat backlight gpio cpu0 default-on"},
	{"cmd":"cat /sys/class/leds/shc\:power\:bl/trigger", "val":"none mmc0 mmc1 [timer] timer-sync oneshot heartbeat backlight gpio cpu0 default-on"},
	{"cmd":"cat /sys/class/leds/shc\:power\:red/trigger", "val":"[none] mmc0 mmc1 timer timer-sync oneshot heartbeat backlight gpio cpu0 default-on"},
	{"cmd":"export PATH=$PATH:/home/hs/shc", "val":"undef"},
	{"cmd":"/home//hs/shc/all_led.sh", "val":"shc:power:red  state  trigger"},
	{"cmd":"cat /sys/class/leds/shc\:cloud\:bl/trigger", "val":"none mmc0 mmc1 timer [timer-sync] oneshot heartbeat backlight gpio cpu0 default-on"},
	{"cmd":"cat /sys/class/leds/shc\:cloud\:red/trigger", "val":"none mmc0 mmc1 timer [timer-sync] oneshot heartbeat backlight gpio cpu0 default-on"},
	{"cmd":"cat /sys/class/leds/shc\:lan\:bl/trigger", "val":"none mmc0 mmc1 timer [timer-sync] oneshot heartbeat backlight gpio cpu0 default-on"},
	{"cmd":"cat /sys/class/leds/shc\:lan\:red/trigger", "val":"none mmc0 mmc1 timer [timer-sync] oneshot heartbeat backlight gpio cpu0 default-on"},
	{"cmd":"cat /sys/class/leds/shc\:power\:bl/trigger", "val":"none mmc0 mmc1 timer [timer-sync] oneshot heartbeat backlight gpio cpu0 default-on"},
	{"cmd":"cat /sys/class/leds/shc\:power\:red/trigger", "val":"none mmc0 mmc1 timer [timer-sync] oneshot heartbeat backlight gpio cpu0 default-on"},
	]

for bl in basiclist:
    if bl["val"] == 'undef':
        tb.eof_write_cmd(tb.c_con, bl["cmd"])
    else:
        tb.eof_write_cmd_check(tb.c_con, bl["cmd"], bl["val"])

tb.statusprint("tc_shc eMMC speed check")
tb.eof_call_tc("tc_workfd_hdparm.py")

tb.statusprint("tc_shc partition check")
#call linux tc_lx_partition_check.py
#for testing usb memstick
#check if usb stick is authorized
tb.eof_call_tc("tc_lx_check_usb_authorized.py")
tb.eof_call_tc("tc_lx_partition_check.py")

# only all 60 days
tb.tc_workfd_check_tc_time_timeout = 60 * 24 * 60 * 60
tb.eof_call_tc("tc_lx_bonnie.py")

tb.statusprint("tc_shc eeprom check ")
#gpio 2_5 is eeprom WP
#low = write protect
tb.config.tc_lx_eeprom_wp_gpio='69'
tb.config.tc_lx_eeprom_wp_val='0'
#call linux tc_lx_eeprom.py
tb.eof_call_tc("tc_lx_eeprom.py")

#call linux tc_lx_cpufreq.py
tb.statusprint("tc_shc cpu frequenc check")
tb.eof_call_tc("tc_lx_cpufreq.py")

tb.config.tc_lx_dmesg_grep_name = "MPU Reference"
tb.eof_call_tc("tc_lx_dmesg_grep.py")

tb.statusprint("tc_shc u-boot setenv")
#call ubot setenv
tb.eof_call_tc("tc_ub_setenv.py")

# power off board at the end
tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
