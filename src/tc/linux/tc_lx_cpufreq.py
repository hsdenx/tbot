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
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_cpufreq.py
# check if frequencies in tb.tc_lx_cpufreq_frequences
# are possible to set with cpufreq-info
# End:

from tbotlib import tbot

logging.info("args: %s", tb.tc_lx_cpufreq_frequences)

def change_freq(tb, c, freq):
    # cpufreq-set -g performance
    tb.eof_write_con_lx_cmd('cpufreq-set -g performance')
    # cpufreq-set -f freq
    tmp = 'cpufreq-set -f ' + freq
    tb.eof_write_con_lx_cmd(tmp)
    # cpufreq-info -f
    tb.eof_write_con('cpufreq-info -f')
    tb.eof_expect_string(c, freq)

# set board state for which the tc is valid
tb.set_board_state("linux")

# check if cpufreq-info is installed
tb.eof_write_con_lx_cmd("cpufreq-info")

for freq in tb.tc_lx_cpufreq_frequences:
    change_freq(tb, tb.workfd, freq)

tb.end_tc(True)
