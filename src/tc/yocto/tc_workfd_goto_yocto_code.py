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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_goto_yocto_code.py
# switch into yocto source tb.config.tc_lab_source_dir + "/yocto-" + tb.config.boardlabname
# set tb.config.yocto_name to "yocto-" + tb.config.boardlabname
# and tb.config.yocto_fulldir_name to tb.config.tc_lab_source_dir + "/" + tb.config.yocto_name
# End:

from tbotlib import tbot

logging.info("args: %s", tb.workfd)

# set some global config variables
tb.config.yocto_name = "yocto-" + tb.config.boardlabname
tb.config.yocto_fulldir_name = tb.config.tc_lab_source_dir + "/" + tb.config.yocto_name
# cd into yocto code
tmp = "cd " + tb.config.yocto_fulldir_name
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
