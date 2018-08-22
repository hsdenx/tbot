# SPDX-License-Identifier: GPL-2.0
#
# Description:
# go into the tbot work dir tb.config.tc_workfd_work_dir
# if not exist, create it
# End:

from tbotlib import tbot

logging.info("args: workfd: %s %s", tb.workfd.name, tb.config.tc_workfd_work_dir)

tmp = '[ ! -d "' + tb.config.tc_workfd_work_dir + '" ] && echo "Does not exist"'
tb.eof_write(tb.workfd, tmp)
ret = tb.tbot_expect_string(tb.workfd, 'Does not exist')
if ret != 'prompt':
    tb.tbot_expect_prompt(tb.workfd)
    # directory does not exist, create it
    tmp = "mkdir -p " + tb.config.tc_workfd_work_dir
    tb.write_lx_cmd_check(tb.workfd, tmp)

tmp = "cd " + tb.config.tc_workfd_work_dir
tb.write_lx_cmd_check(tb.workfd, tmp)
tb.end_tc(True)
