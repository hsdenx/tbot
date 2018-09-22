# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple create a random file tb.tc_workfd_generate_random_file_name
# with tb.tc_workfd_generate_random_file_length length.
#
# used variables
#
# - tb.config.tc_workfd_generate_random_file_name
#| name of random file which get created
#| default: ''
#
# - tb.config.tc_workfd_generate_random_file_length
#| lenght in bytes which get created
#| default: ''
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_generate_random_file_name', '')
tb.define_variable('tc_workfd_generate_random_file_length', '')

tmp = "dd if=/dev/urandom of=" + tb.config.tc_workfd_generate_random_file_name + " bs=1 count=" + tb.config.tc_workfd_generate_random_file_length
tb.write_lx_cmd_check(tb.workfd, tmp)

tmp = "hexdump -C -n 48 " + tb.config.tc_workfd_generate_random_file_name
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
