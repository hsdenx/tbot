# SPDX-License-Identifier: GPL-2.0
#
# Description:
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
# used variables
#
# - tb.config.tc_lab_prepare_tc_name
#| call testcase with this name for settings up lab specific
#| tasks.
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_lab_prepare_tc_name', 'none')

logging.info("args: workfd %s", tb.workfd.name)

# first cd into our workdir
tb.eof_call_tc("tc_workfd_goto_tbot_workdir.py")

if tb.config.tc_lab_prepare_tc_name != 'none':
    tb.eof_call_tc(tb.config.tc_lab_prepare_tc_name)

tb.end_tc(True)
