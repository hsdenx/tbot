# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple copy file from tb.config.tc_workfd_cp_file_from to tb.config.tc_workfd_cp_file_to
#
# used variables
#
# - tb.config.tc_workfd_cp_file_from
#| source path + filename
#| default: ''
#
# - tb.config.tc_workfd_cp_file_to
#| target path + filename
#| default: ''
#
# End:
from tbotlib import tbot

tb.define_variable('tc_workfd_cp_file_from', '')
tb.define_variable('tc_workfd_cp_file_to', '')

tmp = "cp " + tb.config.tc_workfd_cp_file_from + " " + tb.config.tc_workfd_cp_file_to
tb.write_lx_cmd_check(tb.workfd, tmp)
tb.end_tc(True)
