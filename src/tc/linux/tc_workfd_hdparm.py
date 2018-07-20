# SPDX-License-Identifier: GPL-2.0
#
# Description:
# make a minimal hdparm check
# call hdparm -t tb.config.tc_workfd_hdparm_dev
# and check if read speed is greater than tb.config.tc_workfd_hdparm_min
# It is possible to add a PATH tb.config.tc_workfd_hdparm_path
# where hdparm is installed
# Testcase fails if readen speed is <= tb.config.tc_workfd_hdparm_min
#
# used variables
#
# - tb.config.tc_workfd_hdparm_path
#| path to hdparm utility
#| default: '/home/hs/shc/hdparm-9.50/'
#
# - tb.config.tc_workfd_hdparm_dev
#| hdparm device "-t tb.config.tc_workfd_hdparm_dev"
#| default: '/dev/mmcblk1'
#
# - tb.config.tc_workfd_hdparm_min
#| Testcase fails if readen speed is <= tb.config.tc_workfd_hdparm_min
#| default: '12.0'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_hdparm_path', '/home/hs/shc/hdparm-9.50/')
tb.define_variable('tc_workfd_hdparm_dev', '/dev/mmcblk1')
tb.define_variable('tc_workfd_hdparm_min', '12.0')

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
