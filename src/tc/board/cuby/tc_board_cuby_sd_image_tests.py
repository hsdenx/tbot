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
# test the sd image, which is created from yocto build
#
# steps:
# - install nfs rootfs tb.config.yocto_results_dir_lab + tb.config.rootfs_tar_file
#   into tb.config.tc_board_cuby_nfs_dir_w
# - delete the SPI NOR
#   (so we boot from sd card)
# - mount the nfs
# - cp sd card image into it
# - cp sd card image onto sd card
# - reboot and check some messages, be sure we boot from SD card
# - when we are in linux, update with swupdate, so we write
#   all we need onto SPI NOR and eMMC
# - invalidate sd card -> we boot from SPI NOR if something is
#   in SPI NOR ... so may, we do not need this step, but if
#   we not detect that something gone wrong with swupdate, we may
#   have no u-boot in SPI NOR ... so its better to invalidate SD card.
# - reboot and check we are booting from SPI NOR
#
# End:

import time
from tbotlib import tbot

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.c_con

def do_reboot(tb, c, check, ps_check):
    tb.eof_call_tc("tc_lab_poweroff.py")
    time.sleep(3)
    tb.eof_call_tc("tc_lab_poweron.py")

    for tmp in check:
        tb.eof_expect_string(c, tmp, wait_prompt=False)

    # send password
    tb.set_board_state("linux")
    
    # check ps

    # enable watchdog
    #cmd = '/usr/sbin/watchdog start'
    cmd = 'wdt-trigger &'
    tb.write_lx_cmd_check(c, cmd)

save = tb.workfd
tb.workfd = tb.c_ctrl

tb.statusprint("install nfs")
tb.config.tc_yocto_install_rootfs_as_nfs_path = tb.config.yocto_results_dir_lab
tb.eof_call_tc("tc_yocto_install_rootfs_as_nfs.py")
tb.workfd = save

tb.statusprint("delete spi nor")
tb.event.create_event('main', 'tc_board_cuby_sd_image_tests.py', 'SET_DOC_FILENAME', 'delete_spi_nor')
spi_nor_part = ['0', '1', '2', '3', '4', '5', '6']

for partnr in spi_nor_part:
    cmd = 'flash_erase /dev/mtd' + partnr + ' 0 0'
    tb.write_lx_cmd_check(c, cmd)

tb.statusprint("mount nfs")
tb.event.create_event('main', 'tc_board_cuby_sd_image_tests.py', 'SET_DOC_FILENAME', 'mount_nfs')
nfs_loc_mnt = '/tmp/mnt_nfs'
tb.write_lx_cmd_check(c, 'mkdir -p ' + nfs_loc_mnt)
tb.write_lx_cmd_check(c, 'mount -t nfs '+ tb.config.nfs_serverip +':' + tb.config.tc_board_cuby_nfs_dir_w + ' ' + nfs_loc_mnt)

tb.statusprint("cp sdimg to nfs")
tb.event.create_event('main', 'tc_board_cuby_sd_image_tests.py', 'SET_DOC_FILENAME', 'cp_img_to_nfs')
cmd = 'sudo cp ' + tb.config.tc_board_cuby_yocto_result_dir + tb.config.tc_board_cuby_sd_image_name + ' ' + tb.config.tc_board_cuby_nfs_dir_w + tb.config.tc_board_cuby_nfs_dir_loc
tb.write_lx_sudo_cmd_check(tb.c_ctrl, cmd, tb.config.user, tb.config.ip)

tb.statusprint("cp sdimg to sd card")
tb.event.create_event('main', 'tc_board_cuby_sd_image_tests.py', 'SET_DOC_FILENAME', 'cp_img_to_sd')
tb.write_lx_cmd_check(c, 'dd if=' + nfs_loc_mnt + tb.config.tc_board_cuby_nfs_dir_loc + tb.config.tc_board_cuby_sd_image_name + ' of=/dev/mmcblk1')
tb.write_lx_cmd_check(c, 'sync')
tb.write_lx_cmd_check(c, 'sync')
tb.write_lx_cmd_check(c, 'hdparm -z /dev/mmcblk1')

tb.statusprint("check sd card")
tb.event.create_event('main', 'tc_board_cuby_sd_image_tests.py', 'SET_DOC_FILENAME', 'check_sd')
tb.write_lx_cmd_check(c, 'ls -al /dev/mmcblk1p1')

setepa = 'yes'
if setepa == 'yes':
    tb.statusprint("set epa off")
    # as we test with local network and witout epa we must
    # set epa off
    cmd = 'fw_setenv epa off'
    tb.write_lx_cmd_check(c, cmd)
    #cmd = 'fw_setenv optargs loglevel=8'
    #tb.write_lx_cmd_check(c, cmd)
    # env gets stored, so no 'Warning - bad CRC' string
    check = [
	'boot from MMC1',
	'Setting up Environment',
	'SD/MMC found on device 0 part 1',
	'Booting Linux on physical',
	'waiting for updates to bootpart 2',
    ]
else:
    check = [
	'boot from MMC1',
	'Warning - bad CRC',
	'Setting up Environment',
	'SD/MMC found on device 0 part 1',
	'Booting Linux on physical',
	'waiting for updates to bootpart 2',
    ]

tb.statusprint("reboot board and check bootmessages")
tb.event.create_event('main', 'tc_board_cuby_sd_image_tests.py', 'SET_DOC_FILENAME', 'reboot_check_mmc1')

ps_check = [
	'/usr/bin/swupdate -v -w -document_root /www -k /home/root/swu-pub.pem -e stable,copy2',
	]

do_reboot(tb, c, check, ps_check)

save = tb.workfd
tb.workfd = tb.c_con
tb.eof_call_tc("tc_workfd_linux_get_ifconfig.py")
ip = tb.config.linux_get_ifconfig_ip
tb.workfd = save

tb.statusprint("get new swu file")
tb.event.create_event('main', 'tc_board_cuby_sd_image_tests.py', 'SET_DOC_FILENAME', 'send_new_swu_file')
tmp = tb.config.tc_board_cuby_yocto_result_dir + tb.config.tc_board_cuby_swu_name
tb.write_lx_cmd_check(tb.c_ctrl, 'curl -H "X_FILENAME: ' + tmp + '" --data-binary @' + tmp + ' http://' + ip + ':8080/handle_post_request')

tb.statusprint("check swu file output")
tb.event.create_event('main', 'tc_board_cuby_sd_image_tests.py', 'SET_DOC_FILENAME', 'get_new_swu_file')
tb.eof_expect_string(c, 'Valid image found: copying to FLASH', wait_prompt=False)
if setepa == 'yes':
    tb.eof_expect_string(c, 'U-Boot environment updated', wait_prompt=False)
else:
    tb.eof_expect_string(c, 'Updating U-boot environment', wait_prompt=False)
tb.eof_expect_string(c, 'Main loop Daemon', wait_prompt=False)

tb.statusprint("Invalidate SD card")
tb.event.create_event('main', 'tc_board_cuby_sd_image_tests.py', 'SET_DOC_FILENAME', 'invalidate_sd')
tb.write_lx_cmd_check(c, 'dd if=/dev/zero of=/dev/mmcblk1 bs=1024 count=4096')
tb.write_lx_cmd_check(c, 'sync')
tb.write_lx_cmd_check(c, 'hdparm -z /dev/mmcblk1')

time.sleep(3)

tb.statusprint("reboot board and check bootmessages now from SPI")
tb.event.create_event('main', 'tc_board_cuby_sd_image_tests.py', 'SET_DOC_FILENAME', 'reboot_check_spi')
check = [
	'boot from SPI',
	'SD/MMC found on device 1 part 2',
	'Booting Linux on physical',
	'waiting for updates to bootpart 1'
	]
ps_check = [
	'/usr/bin/swupdate -v -w -document_root /www -k /home/root/swu-pub.pem -e stable,copy1',
	]

do_reboot(tb, c, check, ps_check)

tb.end_tc(True)
