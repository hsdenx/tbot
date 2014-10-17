#!/bin/sh

if [ -z "$1" ]; then
	logfile_end=$(date +"20%y-%m-%d")
else
	logfile_end=$1
fi

python2.7 src/common/tbot.py -c tbot_shc.cfg -l log/shc-$logfile_end -t tc_board_shc.py -v

python2.7 src/common/tbot.py -c tbot_smartweb.cfg -l log/smartweb-$logfile_end -t tc_board_smartweb.py -v

python2.7 src/common/tbot.py -c tbot_aristainetos2.cfg -l log/aristainetos2-$logfile_end -t tc_board_aristainetos2.py -v

#python2.7 src/common/tbot.py -c tbot_sirius_dds.cfg -l log/sirius-dds-$logfile_end -t tc_board_sirius_dds.py
