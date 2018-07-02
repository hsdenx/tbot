# SPDX-License-Identifier: GPL-2.0
#
# Description:
# connect to board tb.config.boardlabname with
# connect script
# End:

from tbotlib import tbot

logging.info("args: %s %s", tb.workfd.name, tb.config.boardlabname)

tmp = "connect " + tb.config.boardlabname
tb.eof_write(tb.workfd, tmp, start=False)

searchlist = ["Unknown target", "Connect", "not accessible", "Locked by process", "Connection closed by"]
tmp = True
connected = True
while tmp == True:
    ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
    if ret == '0':
        connected = False
    elif ret == '1':
        tmp = False
    elif ret == '2':
        connected = False
    elif ret == '3':
        connected = False
    elif ret == '4':
        connected = False

if not connected:
    tb.end_tc(False)

# check for 'not accessible'
tb.workfd.set_timeout(2)
tmp_ign = tb.workfd.ign
tb.workfd.ign = ['==>', 'rlogin']
tb.workfd.cnt_ign = len(tb.workfd.ign)

tmp = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
ret = True
if tmp == '2':
    logging.error("not accessible")
    ret = False
if tmp == '3':
    logging.error("Locked by process")
    ret = False
if tmp == '4':
    logging.error("Conection closed")
    ret = False

tb.workfd.set_timeout(None)

tb.workfd.ign = tmp_ign
tb.workfd.cnt_ign = len(tb.workfd.ign)
tb.send_ctrl_c(tb.workfd)
tb.workfd.flush()
tb.end_tc(ret)
