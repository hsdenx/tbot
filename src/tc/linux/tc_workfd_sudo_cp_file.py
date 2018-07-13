# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple copy file from tb.config.tc_workfd_cp_file_from to tb.config.tc_workfd_cp_file_to
# with sudo rights
# End:

from tbotlib import tbot
logging.info("args: workfd %s %s %s", tb.workfd, tb.config.tc_workfd_cp_file_from, tb.config.tc_workfd_cp_file_to)

tb.eof_write(tb.workfd, "su")
ret = tb.tbot_expect_string(tb.workfd, 'Password')
if ret == 'prompt':
    tb.end_tc(False)

tb.write_stream_passwd(tb.workfd, "root", "lab")

# wait here for a standard prompt

tb.set_prompt(tb.workfd, tb.config.linux_prompt, 'linux')
tmp = "\cp " + tb.config.tc_workfd_cp_file_from + " " + tb.config.tc_workfd_cp_file_to
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.eof_write_cmd(tb.workfd, "exit")
tb.end_tc(True)
