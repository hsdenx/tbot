# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_check_if_cmd_exist.py
# check if a command exists
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd,
             tb.config.tc_workfd_check_if_cmd_exist_cmdname)

tmp = 'command -v ' + tb.config.tc_workfd_check_if_cmd_exist_cmdname + ' >/dev/null 2>&1 || { echo >&2 "not installed.";}'
tb.eof_write(tb.workfd, tmp)
searchlist = ["not installed"]
tmp = True
cmd_installed = True
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
        cmd_installed = False
    elif ret == 'prompt':
        tmp = False

tb.end_tc(cmd_installed)
