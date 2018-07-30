# SPDX-License-Identifier: GPL-2.0
#
# Description:
# switch to superuser with user 'root' and password
# tb.config.switch_su_board
#
# used variables
#
# - tb.config.switch_su_board
#| boardname with which password get searched in password file.
#| default: 'lab'
#
# End:

from tbotlib import tbot

tb.define_variable('switch_su_board', 'lab')
logging.info("args: workfd %s", tb.workfd.name)

c = tb.workfd
#switch to root
tb.eof_write(tb.workfd, "su")
ret = tb.tbot_expect_string(tb.workfd, 'assword')
if ret == 'prompt':
    tb.end_tc(False)

tb.eof_write_workfd_passwd("root", tb.config.switch_su_board)

# read until timeout
oldt = c.get_timeout()
c.set_timeout(2)
try:
    c.expect_string('#\$')
except:
    logging.debug("did not get prompt after passwd")
    tb.end_tc(False)

c.set_timeout(oldt)

# set prompt
tb.set_prompt(tb.workfd, tb.config.labprompt, 'linux')

tb.set_term_length(tb.workfd)
tb.end_tc(True)
