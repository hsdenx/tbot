#!/bin/sh

if [ -z "$1" ]; then
	logfile_end=$(date +"20%y-%m-%d")
else
	logfile_end=$1
fi

tbot.py -s lab_denx -c fipad -t tc_board_fipad_linux.py -v log/fipad-$logfile_end
tbot.py -s lab_denx -c shc -t tc_board_shc_ub_tests.py -v log/shc-$logfile_end
tbot.py -s lab_denx -c smartweb -t tc_board_smartweb.py -v log/smartweb-$logfile_end
tbot.py -s lab_denx -c corvus -t tc_board_corvus.py -v log/corvus-$logfile_end
tbot.py -s lab_denx -c tqm5200 -t tc_board_tqm5200s_try_cur_ub.py -v log/tqm5200-$logfile_end
