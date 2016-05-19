#!/bin/sh
# $1 : input logfile
# $2 : output file

#delete all unnecessary line
sed '/INFO/d' $1 > gnlmpf
#delete "tb_ctrl:"
sed 's/^.*tb_ctrl/tb_ctrl/' gnlmpf > gnlmpf2
sed 's/^.*tb_con/tb_con/' gnlmpf2 > $2

rm gnlmpf
rm gnlmpf2
