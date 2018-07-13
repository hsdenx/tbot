# SPDX-License-Identifier: GPL-2.0
#
# Description:
# check if a command tb.config.tc_workfd_check_if_cmd_exist_cmdname
# exists
#
# used variables
#
# - tb.config.tc_workfd_check_if_cmd_exist_cmdname
#| command name which gets checked
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_check_if_cmd_exist_cmdname', 'none')
logging.info("args: workfd %s", tb.workfd)

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
