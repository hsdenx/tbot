# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_sudo_cp_file.py
# simple copy file from tb.tc_workfd_cp_file_a to tb.tc_workfd_cp_file_b
# with sudo rights
# End:

from tbotlib import tbot
logging.info("args: workfd %s %s %s", tb.workfd, tb.tc_workfd_cp_file_a, tb.tc_workfd_cp_file_b)

tb.eof_write(tb.workfd, "su")
ret = tb.tbot_expect_string(tb.workfd, 'Password')
if ret == 'prompt':
    tb.end_tc(False)

tb.write_stream_passwd(tb.workfd, "root", "lab")

# wait here for a standard prompt

tb.set_prompt(tb.workfd, tb.config.linux_prompt, 'linux')
tmp = "\cp " + tb.tc_workfd_cp_file_a + " " + tb.tc_workfd_cp_file_b
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.eof_write_cmd(tb.workfd, "exit")
tb.end_tc(True)
