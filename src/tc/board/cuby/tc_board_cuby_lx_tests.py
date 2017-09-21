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
# tbot.py -s lab_denx -c cuby -t tc_board_cuby_lx_tests.py
# start all linux testcases for the cuby board
# End:

from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("linux")

# enable watchdog
# tmp = '/usr/sbin/watchdog start'
tmp = 'wdt-trigger &'
tb.write_lx_cmd_check(tb.c_con, tmp)

tb.statusprint("cuby linux dmesg checks")
checks = ['SSI AM335x Cuby',
	'44e09000.serial: ttyS0 at MMIO 0x44e09000',
	'48024000.serial: ttyS2 at MMIO 0x48024000',
	'm25p80 spi1.0: m25pe80 (1024 Kbytes)',
	'7 cmdlinepart partitions found on MTD device spi1.0',
	'c_can_platform 481cc000.can',
	'c_can_platform 481d0000.can',
	'omap_rtc 44e3e000.rtc: rtc core: registered 44e3e000.rtc as rtc',
	'omap_rtc 44e3e000.rtc: setting system clock to',
	'mmc0: new high speed MMC card at address 0001',
	'RAMDISK: gzip image found at block 0',
	'tps65910 0-002d: No interrupt support, no core IRQ',
	'omap-sham 53100000.sham: hw accel on OMAP rev 4.3',
	'omap-aes 53500000.aes: OMAP AES hw accel rev: 3.2',
	'omap_wdt: OMAP Watchdog Timer Rev 0x01: initial timeout 60 sec',
	'c_can_platform 481cc000.can can0: setting BTR=2701 BRPE=0000',
	'c_can_platform 481d0000.can can1: setting BTR=2701 BRPE=0000'
	]

for tb.config.tc_lx_dmesg_grep_name in checks:
    tb.eof_call_tc("tc_lx_dmesg_grep.py")

tb.workfd = tb.c_con
tb.statusprint("cuby pinmux check")
tb.eof_call_tc("tc_lx_check_reg_file.py")

tb.set_board_state("linux")
# do some basic tests
tb.statusprint("cuby basic checks")
basiclist = [
	{"cmd":"cat /proc/version", "val":"Linux version 4.1"},
	# {"cmd":"", "val":"undef"},
	]

for bl in basiclist:
    if bl["val"] == 'undef':
        tb.eof_write_cmd(tb.c_con, bl["cmd"])
    else:
        tb.eof_write_cmd_check(tb.c_con, bl["cmd"], bl["val"])

tb.statusprint("cuby eMMC speed check")
tb.eof_call_tc("tc_workfd_hdparm.py")

# check if we have an sd card
tb.config.tc_workfd_check_if_file_exists_name = '/dev/mmcblk1'
ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
if ret == True:
    tb.config.tc_workfd_hdparm_dev = tb.config.tc_workfd_check_if_file_exists_name
    tb.config.tc_workfd_hdparm_min = '20.0'
    tb.eof_call_tc("tc_workfd_hdparm.py")

filelist = [
	'/dev/uio0',
	'/sys/class/uio/uio0/maps/map0/addr',
	'/sys/class/uio/uio0/maps/map0/size',
#	'/opt/ssi/etc/cuby-system/tmp/cuby-update-mirror.inf',
	'/opt/ssi/bin/scripts/setup_epamodule.sh',
	'/etc/sw-versions',
	'/etc/hwrevision',
	'/etc/version'
	]

for bl in filelist:
    tb.config.tc_workfd_check_if_file_exists_name = bl
    tb.eof_call_tc("tc_workfd_check_if_file_exist.py")

# we have now the shuttle application 
# tb.eof_call_tc("tc_board_cuby_lx_pru.py")

# swupdate tests ... ps swupd correct init ?

# check if mongoose webbroser works on correct workdirectory
tb.workfd = tb.c_con
tb.eof_call_tc("tc_workfd_linux_get_ifconfig.py")
ip = tb.config.linux_get_ifconfig_ip
cmd = 'wget http://' + ip + ':8080/index.html'
tb.write_lx_cmd_check(tb.c_ctrl, cmd)

tb.end_tc(True)
