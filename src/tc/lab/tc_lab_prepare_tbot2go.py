# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# do setup needed for the pi in tbot2go mode, when used as
# lapPC
#
# End:

from tbotlib import tbot

logging.info("args: workfd %s %s", tb.workfd.name, tb.config.tc_workfd_check_if_dir_exists_name)

con = True
try:
    tb.c_cpc
    if tb.workfd.name == tb.c_cpc.name:
        con = False
except:
    pass

if con == False:
    # do not set anything on compile PC
    tb.end_tc(True)

# currently we do not setup anything here, but let this
# testcase in code as an example
# setup ip addr for eth0 interface
#cmd = 'sudo ifconfig eth0 down 192.168.3.1 up'
#tb.write_lx_sudo_cmd_check(tb.workfd, cmd, tb.config.user, tb.config.ip)

tb.end_tc(True)
