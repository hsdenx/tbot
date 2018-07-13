# SPDX-License-Identifier: GPL-2.0
#
# Description:
# check if the strings in the tb.config.tc_workfd_check_tar_content_elements
# list are in the tar file tb.config.tc_workfd_check_tar_content_path
#
# tb.config.tc_workfd_check_tar_content_path path and file name
# tb.config.tc_workfd_check_tar_content_elements list of elements in the tar file
# tb.config.tc_workfd_check_tar_content_endtc_onerror end TC when element is not found
#
# used variables
#
# - tb.config.tc_workfd_check_tar_content_path
#| tar file with full path
#| default: ''
#
# - tb.config.tc_workfd_check_tar_content_elements
#| list of elements which must be in tar file
#| default: ''
#
# - tb.config.tc_workfd_check_tar_content_endtc_onerror
#| if 'yes' end testcase with failure
#| default: 'yes'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_check_tar_content_path', '')
tb.define_variable('tc_workfd_check_tar_content_elements', '')
tb.define_variable('tc_workfd_check_tar_content_endtc_onerror', 'yes')
logging.info("args: workfd %s", tb.workfd.name)

tmp = 'tar tfv ' + tb.config.tc_workfd_check_tar_content_path + ' > gnlmpf'
tb.write_lx_cmd_check(tb.workfd, tmp)

filen = tb.config.tc_workfd_check_tar_content_path
for el in tb.config.tc_workfd_check_tar_content_elements:
    tmp = 'grep ' + el + ' gnlmpf'
    tb.eof_write(tb.workfd, tmp)
    loop = True
    res = False
    while loop:
        ret = tb.tbot_rup_and_check_strings(tb.workfd, el)
        if ret == 'prompt':
            loop = False
        if ret == '0':
            res = True
    if res == False:
        logging.error("element %s not found.", el)
        if tb.config.tc_workfd_check_tar_content_endtc_onerror == True:
            tb.end_tc(False)

tb.end_tc(True)
