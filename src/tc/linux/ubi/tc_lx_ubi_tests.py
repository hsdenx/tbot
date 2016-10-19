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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_ubi_tests.py
# - install mtd utils if needed with tc_lx_mtdutils_install.py
# - attach ubi device with tc_lx_ubi_attach.py
# - get info with tc_lx_ubi_info.py
# - get parameters with tc_lx_get_ubi_parameters.py
# End:

from tbotlib import tbot

# here starts the real test
logging.info("args: %s %s %s", tb.config.tc_ubi_cmd_path, tb.config.tc_ubi_mtd_dev, tb.config.tc_ubi_ubi_dev)

# set board state for which the tc is valid
tb.set_board_state("linux")

tb.eof_call_tc("tc_lx_mtdutils_install.py")
tb.eof_call_tc("tc_lx_ubi_attach.py")
tb.eof_call_tc("tc_lx_ubi_info.py")
tb.eof_call_tc("tc_lx_get_ubi_parameters.py")

tb.end_tc(True)
