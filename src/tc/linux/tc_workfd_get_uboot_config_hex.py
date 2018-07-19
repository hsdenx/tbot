# SPDX-License-Identifier: GPL-2.0
#
# Description:
# get a hex parameter from U-Boot configuration
#
# return value:
# TC ends True, if hex value found, else False
# tb.config_result: founded hex value, else 'undef'
# End:

from tbotlib import tbot

logging.info("args: workfd: %s %s %s", tb.workfd.name, tb.config.uboot_get_parameter_file_list,
             tb.config.uboot_config_option)

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
        tmp = 'cat ' + filename + ' | grep --color=never ' + tb.config.uboot_config_option
        tb.eof_write(c, tmp)
        searchlist = [tb.config.uboot_config_option]
        tmp = True
        while tmp == True:
            ret = tb.tbot_rup_and_check_strings(c, searchlist)
            if ret == 'prompt':
                tmp = False
            if ret == '0' and tb.config_found == False:
                string = 'define\s' + tb.config.uboot_config_option
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
    tb.config.uboot_config_option = tb.config_result
    search_define(tb, c)

logging.info("return %s", tb.config_result)
tb.end_tc(tb.config_found)
