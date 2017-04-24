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
# remove the path tb.config.tc_lab_rm_dir
#
# End:

from tbotlib import tbot

logging.info("arg: %s %s", tb.workfd.name, tb.config.tc_lab_rm_dir)

tb.set_board_state("lab")
if tb.workfd.name == "tb_con":
    tb.set_board_state("linux")

tmp = "rm -rf " + self.config.tc_lab_rm_dir
tb.write_lx_cmd_check(tb.workfd, tmp)

tb.end_tc(True)
