#!/bin/sh

#delete all unnecessary line
sed '/read 1/!d' $1 > gnlmpf
#delete ":tbotlib   # read_line hs@pollux.denx.org:"
sed 's/INFO   :tbotlib   # read 1:/ /g' gnlmpf > $2
rm gnlmpf
