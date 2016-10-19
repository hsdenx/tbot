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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_rm_linux_code.py
# rm linux source tb.config.tc_lab_source_dir + '/linux-' + tb.config.boardlabname
# End:

from tbotlib import tbot

logging.info("args: %s", tb.workfd)

tb.tc_lab_rm_dir = tb.config.tc_lab_source_dir + '/linux-' + tb.config.boardlabname
tb.eof_call_tc("tc_lab_rm_dir.py")

tb.end_tc(True)
