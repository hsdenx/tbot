# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c boardname -t tc_workfd_linux_get_uboot_env.py
# read U-Boot Environment variable from tb.config.linux_get_uboot_env_name
# from linux with fw_printenv, and save the value in tb.config.linux_get_uboot_env_value
# End:

from tbotlib import tbot

tb.set_board_state("linux")

logging.info("args: workfd %s %s", tb.workfd.name, tb.config.linux_get_uboot_env_name)

tb.config.linux_get_uboot_env_value = 'undef'
cmd = 'fw_printenv ' + tb.config.linux_get_uboot_env_name
tb.eof_write(tb.workfd, cmd)
ret = True
suc = False
while ret:
    tmp = tb.tbot_rup_and_check_strings(tb.workfd, '\n')
    if tmp == '0':
        tmp = tb.buf.lstrip('\r\n')
        tmp = tmp.split('\r\n')
        tmp = tmp[0].split('=')
        if len(tmp) == 2:
            tb.config.linux_get_uboot_env_value = tmp[1]
            suc = True
    if tmp == 'prompt':
        ret = False

tb.end_tc(suc)
