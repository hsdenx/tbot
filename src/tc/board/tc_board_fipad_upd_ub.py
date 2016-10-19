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
# tbot.py -s lab_denx -c fipad -t tc_board_fipad_upd_ub.py
# update SPL and u-boot.img on the SPI NOR or the MMC0
# card, and boot it ...
# End:

from tbotlib import tbot

logging.info("typ: %s", tb.tc_board_fipad_upd_ub_typ)

tb.workfd = tb.c_con
# update on SPI or MMC0
if tb.tc_board_fipad_upd_ub_typ == 'MMC0':
    tb.eof_call_tc("tc_board_fipad_upd_ub_mmc.py")
elif tb.tc_board_fipad_upd_ub_typ == 'SPI':
    tb.eof_call_tc("tc_board_fipad_upd_ub_spi.py")
else:
    logging.error("typ %s not supported", tb.tc_board_fipad_upd_ub_typ)
    tb.end_tc(True)

# set bootmode
tb.workfd = tb.c_ctrl
if tb.tc_board_fipad_upd_ub_typ == 'MMC0':
    tmp = 'relais   relsrv-02-01  1  on'
elif tb.tc_board_fipad_upd_ub_typ == 'SPI':
    tmp = 'relais   relsrv-02-01  1  off'
tb.write_lx_cmd_check(tb.workfd, tmp)

# power off
tb.eof_call_tc("tc_lab_poweroff.py")

# check U-Boot version
tb.workfd = tb.c_ctrl
tb.tc_ub_get_version_file = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + '/u-boot.bin'
tb.tc_ub_get_version_string = 'U-Boot 20'
tb.eof_call_tc("tc_ub_get_version.py")
tb.uboot_vers = tb.config.tc_return
tb.tc_ub_get_version_file = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + '/u-boot-spl.bin'
tb.tc_ub_get_version_string = 'U-Boot SPL'
tb.eof_call_tc("tc_ub_get_version.py")
tb.spl_vers = tb.config.tc_return

tb.eof_call_tc("tc_ub_check_version.py")
tb.end_tc(True)
