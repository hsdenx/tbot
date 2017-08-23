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
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_ub_testfkt.py
#
# This testcase is for demonstration of using functions in
# testcases, and use them from other testcases.
#
# testcase which calls this function for demo:
# src/tc/uboot/tc_ub_setenv_fkt.py
#
# defines 2 functions:
# - ub_setenv(tb, c, name, val)
#   set Environment variable name with value val
# - ub_checkenv(tb, c, name, val)
#   checks, if U-Boot Environmentvariable name
#   has the value val.
#
# there are 2 ways from calling this testcase directly
# from the cmdline:
#
# - with arguments:
#   tbot.py -s lab_denx -c beagleboneblack -t tc_ub_testfkt.py -a "Heiko Schochernew"
#
#      name = tb.arguments.split()[0]
#      val = tb.arguments.split()[1]
#
# - without arguments:
#   tbot.py -s lab_denx -c beagleboneblack -t tc_ub_testfkt.py
#
#   in this case 
#      name = tb.config.setenv_name
#      val = tb.config.setenv_value
#
# End:
from tbotlib import tbot
from tbotlib import tb_call_tc

@tb_call_tc
def ub_setenv(tb, c, name, val):
    tb.set_board_state("u-boot")
    cmd = 'setenv ' + name + ' ' + val
    tb.eof_write(c, cmd)
    tb.tbot_expect_prompt(c)
    tb.eof_call_tc("tc_ub_help.py")
    tb.end_tc(True)

@tb_call_tc
def ub_checkenv(tb, c, name ,val):
    tb.set_board_state("u-boot")
    tmp = 'printenv ' + name
    tb.eof_write(c, tmp)
    str3 = name + '=' + val
    ret = tb.tbot_expect_string(c, str3)
    if ret == 'prompt':
        tb.end_tc(False)

    tb.tbot_expect_prompt(c)
    tb.end_tc(True)

# If called from cmdline, we need to do testcase specific
# setup here.

if __name__ == "tbotlib":
    from tbotlib import tbot

    # print("testfkt ******************* FILE ", __file__, __name__, tb.starttestcase, tb.calltestcase)
    # check if we got arguments from cmdline and
    # if we are called from the cmdline
    if tb.arguments and (tb.starttestcase == tb.calltestcase):
        name = tb.arguments.split()[0]
        val = tb.arguments.split()[1]
    else:
        name = tb.config.setenv_name
        val = tb.config.setenv_value

    logging.info("testcase arg: %s %s", name, val)

    ub_setenv(tb, tb.c_con, name, val)
    logging.warn("nach ub_setenv fkt call testcase arg: %s %s", name, val)
    ub_checkenv(tb, tb.c_con, name, val)
    logging.warn("nach ub_checkenv fkt call testcase arg: %s %s", name, val)
    tb.end_tc(True)
