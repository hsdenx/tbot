# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_generate_random_file.py
# simple create a random file tb.tc_workfd_generate_random_file_name
# with tb.tc_workfd_generate_random_file_length length.
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s %s", tb.workfd.name, tb.tc_workfd_generate_random_file_name,
             tb.tc_workfd_generate_random_file_length)

tmp = "dd if=/dev/urandom of=" + tb.tc_workfd_generate_random_file_name + " bs=1 count=" + tb.tc_workfd_generate_random_file_length
tb.write_lx_cmd_check(tb.workfd, tmp)

tmp = "hexdump -C -n 48 " + tb.tc_workfd_generate_random_file_name
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
