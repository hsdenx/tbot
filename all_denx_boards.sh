#!/bin/sh

if [ -z "$1" ]; then
	logfile_end=$(date +"20%y-%m-%d")
else
	logfile_end=$1
fi

python2.7 src/common/tbot.py -c tbot_shc.cfg -l log/shc-$logfile_end -t tc_board_shc.py -v

python2.7 src/common/tbot.py -c tbot_smartweb.cfg -l log/smartweb-$logfile_end -t tc_board_smartweb.py -v

python2.7 src/common/tbot.py -c tbot_aristainetos2.cfg -l log/aristainetos2-$logfile_end -t tc_board_aristainetos2.py -v

python2.7 src/common/tbot.py -c tbot_mcx.cfg -l log/mcx-$logfile_end -t tc_board_mcx.py -v

python2.7 src/common/tbot.py -c tbot_tqm5200s.cfg -t tc_board_tqm5200s_try_cur_ub.py -v -l log/tqm5200s-$logfile_end

python2.7 src/common/tbot.py -c tbot_dxr2.cfg -t tc_board_dxr2_ub.py -v -l log/dxr2-ub-$logfile_end

python2.7 src/common/tbot.py -c tbot_dxr2.cfg -t tc_board_dxr2_linux.py -v -l log/dxr2-linux-$logfile_end

python2.7 src/common/tbot.py -c tbot_dxr2.cfg -t tc_ub_dfu_random.py -v -l log/dxr2-ub-dfu-$logfile_end

#python2.7 src/common/tbot.py -c tbot_sirius_dds.cfg -l log/sirius-dds-$logfile_end -t tc_board_sirius_dds.py
