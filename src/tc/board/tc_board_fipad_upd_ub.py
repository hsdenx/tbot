# SPDX-License-Identifier: GPL-2.0
#
# Description:
# update SPL and u-boot.img on the SPI NOR or the MMC0
# card, and boot it ...
# End:

from tbotlib import tbot

logging.info("typ: %s", tb.config.tc_board_fipad_upd_ub_typ)

tb.workfd = tb.c_con
# update on SPI or MMC0
if tb.config.tc_board_fipad_upd_ub_typ == 'MMC0':
    tb.eof_call_tc("tc_board_fipad_upd_ub_mmc.py")
elif tb.config.tc_board_fipad_upd_ub_typ == 'SPI':
    tb.eof_call_tc("tc_board_fipad_upd_ub_spi.py")
else:
    logging.error("typ %s not supported", tb.config.tc_board_fipad_upd_ub_typ)
    tb.end_tc(True)

# set bootmode
tb.workfd = tb.c_ctrl
if tb.config.tc_board_fipad_upd_ub_typ == 'MMC0':
    tmp = 'relais   relsrv-02-01  1  on'
elif tb.config.tc_board_fipad_upd_ub_typ == 'SPI':
    tmp = 'relais   relsrv-02-01  1  off'
tb.write_lx_cmd_check(tb.workfd, tmp)

# power off
tb.eof_call_tc("tc_lab_poweroff.py")

# check U-Boot version
tb.workfd = tb.c_ctrl
tb.config.tc_ub_get_version_file = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + '/u-boot.bin'
tb.config.tc_ub_get_version_string = 'U-Boot 20'
tb.eof_call_tc("tc_ub_get_version.py")
tb.uboot_vers = tb.config.tc_return
tb.config.tc_ub_get_version_file = "/tftpboot/" + tb.config.tftpboardname + "/" + tb.config.ub_load_board_env_subdir + '/u-boot-spl.bin'
tb.config.tc_ub_get_version_string = 'U-Boot SPL'
tb.eof_call_tc("tc_ub_get_version.py")
tb.spl_vers = tb.config.tc_return

tb.eof_call_tc("tc_ub_check_version.py")
tb.end_tc(True)
