# start with
# python2.7 common/tbot.py tbot.cfg default tc/tc_call.py

sys.path.append("./common")
from tbotlib import tbot

#here starts the real test
logging.info("do something call test")
ret = tb.call_tc("src/tc/tc_test.py")
if ret == False:
    tb.end_tc(False)
tb.end_tc(True)
