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
#
# install swu image with curl
# reboot the board
# check rootfs version
# call tc_board_cuby_lx_tests.py
#
# End:

import time
from tbotlib import tbot

tb.set_board_state("linux")

tb.workfd = tb.c_ctrl

# install the image on the board
tmp = tb.config.tc_board_cuby_yocto_result_dir + tb.config.tc_board_cuby_swu_name

tb.config.tc_workfd_check_if_file_exists_name = tmp
tb.eof_call_tc("tc_workfd_check_if_file_exist.py")

# now send it with curl to it, and install
# cmd = 'curl -H "X_FILENAME: ' + tmp + '"  --data-binary @' + tmp + ' http://' + boardip + ':8080/handle_post_request'
# first get ip address from the board
tb.workfd = tb.c_con
tb.eof_call_tc("tc_workfd_linux_get_ifconfig.py")
ip = tb.config.linux_get_ifconfig_ip

tb.event.create_event('main', 'tc_board_cuby_yocto_test', 'SET_DOC_FILENAME', 'get_current_bootpart')

# second: get current bootpart from the board
tb.config.linux_get_uboot_env_name = 'bootpart'
tb.eof_call_tc("tc_workfd_linux_get_uboot_env.py")
running_bootpart = tb.config.linux_get_uboot_env_value

# -> swupdate must install on other partition
# check this
if running_bootpart == '1':
    target_bootpart = '2'
else:
    target_bootpart = '1'

tb.event.create_event('main', 'tc_board_cuby_yocto_test', 'SET_DOC_FILENAME', 'send_image_to_board')

# send the image to the board
tb.workfd = tb.c_ctrl
cmd = 'curl -H "X_FILENAME: ' + tmp + '" --data-binary @' + tmp + ' http://' + ip + ':8080/handle_post_request'
# output in good case:
# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN
# "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
# <html xmlns=\"http://www.w3.org/1999/xhtml"><head><meta http-equiv="refresh" content="0; url=./update.html" /></head></html>HTTP/1.0 200 OK
# -> we only interested in 'OK'
tb.eof_write(tb.workfd, cmd)
tb.eof_expect_string(tb.workfd, 'OK')

tb.event.create_event('main', 'tc_board_cuby_yocto_test', 'SET_DOC_FILENAME', 'result_from_board')
# now check the output from the board
con = tb.c_con
tb.workfd = con

tb.eof_expect_string(con, 'U-Boot var: bootpart', wait_prompt=False)
tb.eof_expect_string(con, '\n', wait_prompt=False)
tmp = tb.buf.lstrip('\r\n')
tmp = tmp.split('\r\n')
tmp = tmp[0].split('=')
tmp = tmp[1].split('=')
tmp = tmp[0].strip()

bp_ok = True
if target_bootpart != tmp: 
    logging.error("target_bootpart %s != bootpart %s" % (target_bootpart, tmp))
    bp_ok = False

tb.eof_expect_string(con, 'Valid image found: copying to FLASH', wait_prompt=False)
tb.eof_expect_string(con, 'Updating U-boot environment', wait_prompt=False)
tb.eof_expect_string(con, 'Main loop Daemon', wait_prompt=False)

# check bootpart U-Boot Envvariable
tb.config.linux_get_uboot_env_name = 'bootpart'
tb.eof_call_tc("tc_workfd_linux_get_uboot_env.py")
new_bootpart = tb.config.linux_get_uboot_env_value

if new_bootpart != target_bootpart:
    logging.error("target_bootpart %s != U-Boot Env bootpart %s" % (target_bootpart, new_bootpart))

# check bootcounter register in RTC
tmp = 'devmem2 0x44E3E068'
tb.eof_write(tb.workfd, tmp)
tb.eof_expect_string(tb.workfd, '0x000001B0')

# give the board more time
oldtimeout = tb.config.state_linux_timeout
tb.config.state_linux_timeout = 4 * oldtimeout

# now reboot the board, and check if u-boot boots the target_bootpart
# tb.eof_write(con, 'reboot')
tb.eof_call_tc("tc_lab_poweroff.py")
time.sleep(3)
tb.eof_call_tc("tc_lab_poweron.py")

# we must find the string "part " + bootpart...
tmp = 'device 1 part ' + target_bootpart
tmp2 = 'device 1 part ' + running_bootpart
ret = False
strings = [tmp, tmp2]
while ret == False:
    tmp = self.tbot_rup_and_check_strings(con, strings)
    if tmp == '0':
        ret = True
    if tmp == '1':
        logging.error("Wrong bootpartition %s detected", running_bootpart)
        tb.end_tc(False)
    if tmp == 'prompt':
        ret = False

# if correct bootpart found, go to linux state
tb.set_board_state("linux")

tb.config.state_linux_timeout = oldtimeout

# check if we booted the new rootfs version
cmd = 'cat /etc/version'
tb.eof_write_cmd_get_line(tb.c_con, cmd)
rootfsvers = tb.ret_write_cmd_get_line.strip()
try:
    tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version
except:
    tb.workfd = tb.c_ctrl
    tb.eof_call_tc("tc_yocto_get_rootfs_from_tarball.py")

if tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version != rootfsvers:
    logging.error("Wrong rootfs vers found: %s != %s" % (rootfsvers, tb.config.tc_yocto_get_rootfs_from_tarball_rootfs_version))
    tb.end_tc(False)

# now we have booted the new image ... test it
tb.eof_call_tc("tc_board_cuby_lx_tests.py")

tb.end_tc(True)
