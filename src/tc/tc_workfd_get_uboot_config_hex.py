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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_workfd_get_uboot_config_hex.py
# get a hex parameter from U-Boot configuration
# Input:
# tb.tc_workfd_cd_name: name of the u-boot source
# tb.uboot_get_parameter_file_list: list of files, where TC searches
#   for the define
# tb.uboot_config_option: config option which get searched
#
# return value:
# TC ends True, if hex value found, else False
# tb.config_result: founded hex value, else 'undef'
from tbotlib import tbot

logging.info("args: workfd: %s %s %s %s", tb.workfd, tb.tc_workfd_cd_name, tb.uboot_get_parameter_file_list, tb.uboot_config_option)

tb.config_result = 'undef'
# must be set: tb.tc_workfd_cd_name
tb.eof_call_tc("tc_workfd_cd_to_dir.py")
#check if u-boot source is configured
tb.tc_workfd_check_if_file_exists_name = '.config'
tb.eof_call_tc("tc_workfd_check_if_file_exist.py")

tb.needs_retry = False
tb.config_found = False

def search_define(tb):
    for filename in tb.uboot_get_parameter_file_list:
        tmp = 'cat ' + filename + ' | grep --color=never ' + tb.uboot_config_option
        tb.eof_write(tb.workfd, tmp)
        searchlist = [tb.uboot_config_option]
        tmp = True
        while tmp == True:
            tmp = tb.readline_and_search_strings(tb.workfd, searchlist)
            if tmp == 0:
                if tb.config_found == False:
                    string = tb.buf[tb.workfd]
                    while '\t\t' in string:
                        string = string.replace('\t\t', '\t')
                    delimiters = " ", "\t", "="
                    regexPattern = '|'.join(map(re.escape, delimiters))
                    tmp = re.split(regexPattern, string)
                    if tmp[1] == tb.uboot_config_option:
                        tb.config_found = True
                        # check if string contains a number
                        tb.config_result = tmp[2]
                    if tmp[0] == tb.uboot_config_option:
                        tb.config_found = True
                        # check if string contains a number
                        tb.config_result = tmp[1]

                    hexnum = True
                    intnum = True
                    try:
                        num = hex(tb.config_result)
                    except:
                        hexnum = False

                    try:
                        num = int(tb.config_result)
                    except:
                        intnum = False

                    # if not, it is maybe another define ... search this define
                    if (intnum == False) and (hexnum == False):
                        tb.needs_retry = True
                tmp = True
            elif tmp == None:
                # ! endless loop ...
                tmp = True
            elif tmp == 'prompt':
                tmp = False

        if tb.config_found == True:
            break

search_define(tb)
if tb.needs_retry == True:
    tb.config_found = False
    tb.needs_retry = False
    tb.uboot_config_option = tb.config_result
    search_define(tb)

logging.info("return %s", tb.config_result)
tb.end_tc(tb.config_found)
