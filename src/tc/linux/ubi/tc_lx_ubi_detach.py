# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_ubi_detach.py
# detach ubi device tb.config.tc_ubi_mtd_dev
# End:

from tbotlib import tbot
import re

# here starts the real test
logging.info("args: %s %s", tb.config.tc_ubi_cmd_path, tb.config.tc_ubi_mtd_dev)

mtd_dev_nr = re.sub("[^0-9]", "", tb.config.tc_ubi_mtd_dev)
logging.info("mtd_dev_nr: %s", mtd_dev_nr)

# set board state for which the tc is valid
tb.set_board_state("linux")

def create_ubi_cmd(tb, cmd):
    tmp = tb.config.tc_ubi_cmd_path + '/' + cmd
    return tmp

tmp = create_ubi_cmd(tb, 'ubi-utils/ubidetach -m ' + mtd_dev_nr)
tb.eof_write_con_lx_cmd(tmp)
tb.end_tc(True)
