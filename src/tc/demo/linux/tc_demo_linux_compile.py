# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# - goto linux code with testcase tc_workfd_goto_linux_code.py
# - compile with testcase tc_workfd_compile_linux.py
# - deploy it. If tb.config.tc_demo_linux_test_deploy != 'none'
#|  call boardspecific testcase for deploying linux sources.
#|  else copy files from "$TBOT_BASEDIR_LINUX/arch/arm/boot/"
#|  to tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir
#
# used variables
#
# - tb.config.tc_demo_linux_test_deploy
#| contains the testcasename which get called for deploying linux
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_demo_linux_test_deploy', 'none')

logging.info("args: %s", tb.config.tc_workfd_compile_linux_make_target)
logging.info("args: %s", tb.config.tc_workfd_compile_linux_dt_name)

tb.eof_call_tc("tc_workfd_goto_linux_code.py")

# compile it
tb.eof_call_tc("tc_workfd_compile_linux.py")

if tb.config.tc_demo_linux_test_deploy != 'none':
    tb.eof_call_tc(tb.config.tc_demo_linux_test_deploy)
    tb.end_tc(True)

# copy files to tftpdir
c = tb.workfd
tb.statusprint("copy files")
r = tb.config.tftpdir + '/'
t = r + tb.config.tftpboardname + '/' + tb.config.ub_load_board_env_subdir
s = "$TBOT_BASEDIR_LINUX/arch/arm/boot/"
so = s + tb.config.tc_workfd_compile_linux_make_target
ta = t
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
for f in tb.config.tc_workfd_compile_linux_dt_name:
    so = s + 'dts/' + f
    tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

so = "$TBOT_BASEDIR_LINUX/System.map"
ta = t + "linux-system.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

tb.end_tc(True)
