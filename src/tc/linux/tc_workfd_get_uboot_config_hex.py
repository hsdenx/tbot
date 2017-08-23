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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_get_uboot_config_hex.py
# get a hex parameter from U-Boot configuration
# Input:
# tb.config.uboot_get_parameter_file_list: list of files, where TC searches
#   for the define
# tb.uboot_config_option: config option which get searched
#
# return value:
# TC ends True, if hex value found, else False
# tb.config_result: founded hex value, else 'undef'
# End:

from tbotlib import tbot

logging.info("args: workfd: %s %s %s", tb.workfd.name, tb.config.uboot_get_parameter_file_list,
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
            if ret == '0' and tb.config_found == False:
                string = 'define\s' + tb.uboot_config_option
                p = re.search(string, tb.buf)
                if p == None:
                    continue
                ret = tb.tbot_rup_and_check_strings(c, '\n')
                if ret == 'prompt':
                    tb.enc_tc(False)
                string = tb.buf
                val = string.split()
                if val == []:
                    continue

                tb.config_found = True
                tb.config_result = val[0]
                hexnum = True
                intnum = True
                try:
                    num = int(tb.config_result, 16)
                except:
                    hexnum = False

                try:
                    num = int(tb.config_result)
                except:
                    intnum = False

                # if not, it is maybe another define ... search this define
                if (intnum == False) and (hexnum == False):
                    tb.needs_retry = True

search_define(tb, c)
if tb.needs_retry == True:
    tb.config_found = False
    tb.needs_retry = False
    tb.uboot_config_option = tb.config_result
    search_define(tb, c)

logging.info("return %s", tb.config_result)
tb.end_tc(tb.config_found)
