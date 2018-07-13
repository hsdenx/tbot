# SPDX-License-Identifier: GPL-2.0
#
# Description:
# connect to console with conmux
# Never tested !!!
# End:

from tbotlib import tbot

logging.info("args: workdfd: %s", tb.workfd)

tmp = "conmux-console " + tb.config.boardlabname
ret = tb.write_stream(tb.workfd, tmp)
if not ret:
    tb.end_tc(False)

# search for error/success strings (from connmux-console if there are ??)
# If no output from connmux for error/success, delete the follwoing lines
# just end with "tb.end_tc(True)"
# here if "Unknown target" read -> fail
# "Connect" -> success
searchlist = ["Unknown target", "Connect"]
tmp = True
connected = True
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(tb.c_con, searchlist)
    if ret == '0':
        connected = False
    elif ret == '1':
        tmp = False

if not connected:
    tb.end_tc(False)

tb.end_tc(True)
