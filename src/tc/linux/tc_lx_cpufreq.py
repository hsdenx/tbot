# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_cpufreq.py
# check if frequencies in tb.config.tc_lx_cpufreq_frequences
# are possible to set with cpufreq-info
# End:

from tbotlib import tbot

logging.info("args: %s", tb.config.tc_lx_cpufreq_frequences)

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

for freq in tb.config.tc_lx_cpufreq_frequences:
    change_freq(tb, tb.workfd, freq)

tb.end_tc(True)
