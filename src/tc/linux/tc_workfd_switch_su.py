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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_switch_su.py
# switch to superuser
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd.name, tb.config.switch_su_board)

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
