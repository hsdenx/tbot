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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_get_uboot_config_string.py
# get a string parameter from U-Boot configuration
# Input:
# tb.config.uboot_get_parameter_file_list: list of files, where TC searches
#   for the define
# tb.uboot_config_option: config option which get searched
#
# return value:
# TC ends True, if string value found, else False
# tb.config_result: founded string value, else 'undef'
# End:

from tbotlib import tbot

logging.info("args: workfd: %s %s %s", tb.workfd, tb.config.uboot_get_parameter_file_list,
             tb.uboot_config_option)

c = tb.workfd
tb.set_term_length(c)
tb.config_result = 'undef'
# switch into u-boot source
tb.eof_call_tc("tc_workfd_goto_uboot_code.py")
# check if u-boot source is configured
tb.config.tc_workfd_check_if_file_exists_name = '.config'
tb.eof_call_tc("tc_workfd_check_if_file_exist.py")

tb.needs_retry = False
tb.config_found = False

def search_define(tb, c):
    for filename in tb.config.uboot_get_parameter_file_list:
        if tb.config_found == True:
            break
        tmp = 'cat ' + filename + ' | grep --color=never ' + tb.uboot_config_option
        tb.eof_write(c, tmp)
        searchlist = [tb.uboot_config_option]
        tmp = True
        while tmp == True:
            ret = tb.tbot_rup_and_check_strings(c, searchlist)
            if ret == 'prompt':
                tmp = False
            if ret == '0':
                if tb.config_found == False:
                    ret = tb.tbot_rup_and_check_strings(c, '\n')
                    if ret == 'prompt':
                        tb.enc_tc(False)

                    string = tb.buf
                    if string == '':
                        continue
                    val = string.replace('=','')
                    val = val.replace('\r','')
                    val = val.replace('\n','')
                    val = val.replace('"','')
                    if val == '':
                        continue
                    tb.config_found = True
                    tb.config_result = val

        if tb.config_found == True:
            break

search_define(tb, c)
if tb.needs_retry == True:
    tb.config_found = False
    tb.needs_retry = False
    tb.uboot_config_option = tb.config_result
    search_define(tb)

logging.info("return %s", tb.config_result)
tb.end_tc(tb.config_found)
