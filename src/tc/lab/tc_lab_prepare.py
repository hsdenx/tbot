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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lab_prepare.py
#
# when logging into a lab, do some basic setup
# - go into workdir
# - if tb.config.tc_lab_prepare_tc_name != 'none' then call
#   testcase which name is defined in tb.config.tc_lab_prepare_tc_name
#
#   In this testcase, you can do lab specific setup you need
#   and set the variable tb.config.tc_lab_prepare_tc_name
#   with the name you give your testcase for lab specific setup.
#
# End:

from tbotlib import tbot

try:
    tb.config.tc_lab_prepare_tc_name
except:
    tb.config.tc_lab_prepare_tc_name = 'none'

logging.info("args: workfd %s %s", tb.workfd.name, tb.config.tc_lab_prepare_tc_name)

# first cd into our workdir
tb.eof_call_tc("tc_workfd_goto_tbot_workdir.py")

if tb.config.tc_lab_prepare_tc_name != 'none':
    tb.eof_call_tc(tb.config.tc_lab_prepare_tc_name)

tb.end_tc(True)
