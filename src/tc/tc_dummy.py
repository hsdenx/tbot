# SPDX-License-Identifier: GPL-2.0
#
# Description:
# This is only a dummy testcase, with which you can start
# to write a testcase.
#
# Add here between "Description:" and "End:" a help text
# which explains what your testcase do and how, which
# variables it uses.
#
# End:

from tbotlib import tbot

# always add some logging info for example which variables
# your testcase uses
# don;t forget to define a default value for a new config variable
# if it makes sense
logging.info("arg: ")

# compile, install and do tests
# call other testcases with
# tb.eof_call_tc("NAME OF TESTCASE)
# if the testcase must end without error
# or if you are interested in the return value with
# ret = tb.call_tc("NAME OF TESTCASE)

# Always end a testcase with tb.end_tc(True or False)
tb.end_tc(True)
