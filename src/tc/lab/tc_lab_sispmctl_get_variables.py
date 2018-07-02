# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get serial and index for tb.config.boardlabpowername for
# controlling the Gembird Silver Shield PM power controller
# and save it in tb.config.gembird_serial and tb.config.gembird_index
#
# used variables
#
# - tb.config.gembird_serial
#| setup at runtime of testcase tc_lab_sispmctl_get_variables.py
#| contains the serial number of the gembird controller
#| to which the tb.config.boardlabpowername is connected
#
# - tb.config.gembird_index
#| setup at runtime of testcase tc_lab_sispmctl_get_variables.py
#| contains the device index of the gembird controller
#| to which the tb.config.boardlabpowername is connected
#
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.config.boardname, tb.config.boardlabpowername)

if tb.config.boardlabpowername == 'beagleboneblack':
    tb.config.gembird_index = '1'
    tb.config.gembird_serial = '01:01:56:a2:f1'
else:
    logging.error("boardlabname %s not found." % (tb.config.boardlabpowername))
    tb.end_tc(False)

tb.end_tc(True)
