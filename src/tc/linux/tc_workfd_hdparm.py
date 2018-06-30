# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_hdparm.py
# make a minimal hdparm check
# call hdparm -t tb.config.tc_workfd_hdparm_dev
# and check if read speed is greater than tb.config.tc_workfd_hdparm_min
# It is possible to add a PATH tb.config.tc_workfd_hdparm_path
# where hdparm is installed
# Testcase fails if readen speed is <= tb.config.tc_workfd_hdparm_min
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s %s", tb.config.tc_workfd_hdparm_path, tb.config.tc_workfd_hdparm_dev, tb.config.tc_workfd_hdparm_min)

tb.set_board_state("linux")

c = tb.c_con
tmp = ''
if tb.config.tc_workfd_hdparm_path != 'none':
    tmp = tb.config.tc_workfd_hdparm_path

cmd = tmp + 'hdparm -t ' + tb.config.tc_workfd_hdparm_dev

tb.eof_write(c, cmd)
searchlist = ["MB/sec", "kB/s"]
tmp = True
result = False
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(c, searchlist)
    if ret == '0' or ret == '1':
        # extract value from line
        str1 = tb.buf.split('=')
        str1 = str1[1].strip(' ')
        str1 = str1.split(' ')
        val = float(str1[0])
        # check if value is greater then expected minimum
        if val > float(tb.config.tc_workfd_hdparm_min):
            logging.info("value %s > %s -> OK", str1[0], tb.config.tc_workfd_hdparm_min)
            result = True
        else:
            logging.error("value %s <= %s", str1[0], tb.config.tc_workfd_hdparm_min)
    elif ret == 'prompt':
        tmp = False

if result != True:
    tb.end_tc(False)
tb.end_tc(True)
