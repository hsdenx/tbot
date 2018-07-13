# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple check if previous shell command was succesful
# End:

from tbotlib import tbot
logging.info("args: workfd %s", tb.workfd.name)

# we can not check if we are in linux, as this deletes
# the state of the last command...
tb.eof_write(tb.workfd, "if [ $? -ne 0 ]; then echo 'FAILED'; fi", False)
searchlist = ["FAILED"]
tmp = True
cmd_ok = True
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
        cmd_ok = False
    elif ret == 'prompt':
        tmp = False

tb.end_tc(cmd_ok)
