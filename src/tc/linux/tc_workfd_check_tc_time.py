# SPDX-License-Identifier: GPL-2.0
#
# Description:
# check if time for a special testcase is expired.
# some testcases (like writting in a flash) are not good for
# execute them every day, so give them a timeout. This testcase
# checks, if the testcases is ready for a new run.
# False means time is not expired
# True means time is expired
#
# used variables
#
# - tb.config.tc_workfd_check_tc_time_tcname
#| tc name
#| default: ''
#
# - tb.config.tc_workfd_check_tc_time_timeout
#| timeout in seconds
#| default: '2592000' which is 30 days
#
# End:

from tbotlib import tbot
import time

tb.define_variable('tc_workfd_check_tc_time_tcname', '')
tb.define_variable('tc_workfd_check_tc_time_timeout', '2592000')
logging.info("args: %s", tb.config.tc_workfd_tbotfiles_dir)
logging.info("args: %s", tb.config.boardname)

# set board state for which the tc is valid
timefile = tb.config.tc_workfd_tbotfiles_dir + "/" + "workfd_check_tc_time_" + tb.config.boardname + "_" + tb.config.tc_workfd_check_tc_time_tcname

c = tb.workfd
tb.set_term_length(c)
def check_tc_time_create(tb, c, timefile):
    tmp = 'echo ' + str(int(time.time())) + ' > ' + timefile
    tb.eof_write_cmd(c, tmp)
    tmp = 'cat ' + ' ' + timefile
    tb.eof_write_cmd(c, tmp)

# try to open file
tmp = 'cat ' + timefile
tb.eof_write_cmd(c, tmp)
ret = tb.call_tc("tc_workfd_check_cmd_success.py")
# if not create it, and return false
if ret == False:
    #write current date
    logging.info("no timefile %s, creating it -> timer expired", timefile)
    check_tc_time_create(tb, c, timefile)
    tb.end_tc(True)

# check date
tb.eof_write(c, 'cat ' + ' ' + timefile)
ret = True
while(ret):
    ret = tb.read_line(tb.workfd)
    if ret == True:
        se = self.buf.split()
        if se == []:
            continue
        ret = se[0].isdigit()
        if ret == True:
            filetime = int(se[0])
            break
        else:
            ret = True
    else:
        logging.debug("error, could not read line")
        tb.end_tc(False)

tb.tbot_expect_prompt(c)
curtime = int(time.time())
logging.info("cur %d ftime: %d + timeout: %s", curtime, filetime, tb.config.tc_workfd_check_tc_time_timeout)
# if not expired end False
if curtime < filetime + int(tb.config.tc_workfd_check_tc_time_timeout):
    tb.end_tc(False)

# else write new time and end True
check_tc_time_create(tb, c, timefile)
tb.end_tc(True)
