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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_check_tar_content.py
# check if the strings in the tb.config.tc_workfd_check_tar_content_elements
# list are in the tar file tb.config.tc_workfd_check_tar_content_path
#
# tb.config.tc_workfd_check_tar_content_path path and file name
# tb.config.tc_workfd_check_tar_content_elements list of elements in the tar file
# tb.config.tc_workfd_check_tar_content_endtc_onerror end TC when element is not found
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s %s %s", tb.workfd.name, tb.config.tc_workfd_check_tar_content_path,
	tb.config.tc_workfd_check_tar_content_elements,
	tb.config.tc_workfd_check_tar_content_endtc_onerror)

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
