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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_check_tc_time.py
# check if time for a special testcase is expired.
# some testcases (like writting in a flash) are not good for
# execute them every day, so give them a timeout. This testcase
# checks, if the testcases is ready for a new run.
# False means time is not expired
# True means time is expired
# End:

from tbotlib import tbot
import time

logging.info("args: workdfd: %s %s", tb.workfd, tb.tc_workfd_tbotfiles_dir)
logging.info("args: %s %s %s", tb.boardname, tb.tc_workfd_check_tc_time_tcname,
             tb.tc_workfd_check_tc_time_timeout)

# set board state for which the tc is valid
timefile = tb.tc_workfd_tbotfiles_dir + "/" + "workfd_check_tc_time_" + tb.boardname + "_" + tb.tc_workfd_check_tc_time_tcname

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
logging.info("cur %d ftime: %d + timeout: %d", curtime, filetime, tb.tc_workfd_check_tc_time_timeout)
# if not expired end False
if curtime < filetime + tb.tc_workfd_check_tc_time_timeout:
    tb.end_tc(False)

# else write new time and end True
check_tc_time_create(tb, c, timefile)
tb.end_tc(True)
