# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_connect_with_kermit.py
# disconnect from a kermit connection
# End:

from tbotlib import tbot

logging.info("args: workdfd: %s", tb.workfd)
logging.info("args: ssh: %s", tb.config.tc_workfd_connect_with_kermit_ssh)
logging.info("args: kermit: %s %s", tb.config.kermit_line, tb.config.kermit_speed)

string = pack('h', 28)
string = string[:1]
tb.workfd.send_raw(string)
tb.workfd.send_raw('C')
tb.workfd.set_prompt('C-Kermit>', 'linux')
tb.workfd.expect_prompt()

# set lab pc linux prompt
tb.workfd.set_prompt(tb.config.linux_prompt, 'linux')
tb.eof_write(tb.workfd, 'exit', False)
searchlist = ['OK to exit']
tmp = True
once = 0
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
        if once == 0:
            tb.eof_write(tb.workfd, 'OK', False)
            once = 1
    if ret == 'prompt':
        tmp = False

tb.end_tc(True)
