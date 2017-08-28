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
#
# - goto linux code
# - compile it
# - deploy it
#
# End:

from tbotlib import tbot

try:
    tb.c_cpc
    tb.workfd = tb.c_cpc
except:
    tb.workfd = tb.c_ctrl

try:
    tb.config.tc_demo_linux_test_deploy
except:
    tb.config.tc_demo_linux_test_deploy = ''

logging.info("args: %s %s", tb.workfd.name, tb.config.tc_demo_linux_test_deploy)

tb.eof_call_tc("tc_workfd_goto_linux_code.py")

# compile it
tb.eof_call_tc("tc_workfd_compile_linux.py")

if tb.config.tc_demo_linux_test_deploy != '':
    tb.eof_call_tc(tb.config.tc_demo_linux_test_deploy)
    tb.end_tc(True)

# copy files to tftpdir
c = tb.workfd
tb.statusprint("copy files")
r = tb.config.tftprootdir
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
