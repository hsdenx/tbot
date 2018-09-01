# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# checks if tb.config.tc_linux_imx_usb_loader_install_path is already
# set. If so, we have a correct installation of imx_usb_loader
# and path to imx_usb is stored in tb.config.tc_linux_imx_usb_loader_install_path
#
# If tb.config.tc_linux_imx_usb_loader_install_path is not set,
# set tb.config.tc_linux_imx_usb_loader_install_path to
# tb.config.tc_linux_imx_usb_loader_install_path = tb.config.tbot_src_path + 'imx_usb_loader/'
# and check if directory exists. If True, we assume that there is
# a correct imx_usb installation and return
#
# If tb.config.tc_linux_imx_usb_loader_install_path
# does not exist, try to clone imx_usb_loader from
# https://github.com/boundarydevices/imx_usb_loader
# and set it up for our needs, and compile it.
# We use for vid:pid the setting in
# tb.config.tc_linux_imx_usb_loader_install_vid_pid
#
# be sure, libusb is installed on your system.
#
# used variables:
#
# - tb.config.tbot_src_dirname
#|  path, where tbot installs programs used from tbot
#|  on the lab pc
#|   default = 'src/'
#
# - tb.config.tbot_src_path
#|  full path to src directory
#|  default = tb.config.tc_workfd_work_dir + tb.config.tbot_src_dirname
#
# End:

from tbotlib import tbot

tb.workfd = tb.c_ctrl

tb.define_variable('tbot_src_dirname', 'src/')
tb.define_variable('tbot_src_path', tb.config.tc_workfd_work_dir + tb.config.tbot_src_dirname)

logging.info("arg: %s", tb.workfd.name)

try:
    # if we have already imx_usb installed, break
    tb.config.tc_linux_imx_usb_loader_install_path
    logging.info("arg: %s", tb.config.tc_linux_imx_usb_loader_install_path)
    tb.end_tc(True)
except:
    pass

# look if directory exists
tb.config.tc_linux_imx_usb_loader_install_path = tb.config.tbot_src_path + 'imx_usb_loader/'
tb.config.tc_workfd_check_if_dir_exists_name = tb.config.tc_linux_imx_usb_loader_install_path
tb.config.tc_workfd_check_if_dir_exists_create = 'no'
ret = tb.call_tc("tc_workfd_check_if_dir_exist.py")
if ret == True:
    tb.end_tc(True)

# check if tbot src dir exists
tb.config.tc_workfd_check_if_dir_exists_create = 'yes'
tb.config.tc_workfd_check_if_dir_exists_name = tb.config.tbot_src_path
tb.eof_call_tc("tc_workfd_check_if_dir_exist.py")

cmd = 'cd ' + tb.config.tbot_src_path
tb.write_lx_cmd_check(tb.workfd, cmd)

# get imx_usb_loader
cmd = 'git clone https://github.com/boundarydevices/imx_usb_loader'
tb.write_lx_cmd_check(tb.workfd, cmd)

tb.config.tc_linux_imx_usb_loader_install_path = tb.config.tbot_src_path + 'imx_usb_loader/'
cmd = 'cd ' + tb.config.tc_linux_imx_usb_loader_install_path
tb.write_lx_cmd_check(tb.workfd, cmd)

# create config file
fname = 'mx6_usb_sdp_spl_tbot.conf'
filecontent = [
	'mx6_spl_sdp',
	'#hid/bulk,[old_header,]max packet size, {ram start, ram size}(repeat valid ram areas)',
	'#In SPL, we typically load u-boot.img which has a U-boot header...',
	'hid,uboot_header,1024,0x10000000,1G,0x00907000,0x31000',
	'#u-boot.img:jump header2'
]
first = ' > '
for fc in filecontent:
    cmd = 'echo "' + fc + '"' + first + fname
    tb.write_lx_cmd_check(tb.workfd, cmd)
    first = ' >> '

# add config file into imx_usb.conf
try:
    tb.config.tc_linux_imx_usb_loader_install_vid_pid
except:
    tb.config.tc_linux_imx_usb_loader_install_vid_pid = '0x15a2:0x1060'

vid_pid = tb.config.tc_linux_imx_usb_loader_install_vid_pid + ', '
cmd = 'echo "' + vid_pid  + fname + '"' + first + 'imx_usb.conf'
tb.write_lx_cmd_check(tb.workfd, cmd)

# compile
cmd = 'make'
tb.write_lx_cmd_check(tb.workfd, cmd)

tb.end_tc(True)
