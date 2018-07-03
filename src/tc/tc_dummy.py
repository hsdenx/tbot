# SPDX-License-Identifier: GPL-2.0
#
# Description:
# This is only a dummy testcase, with which you can start
# to write a testcase.
#
# Add here between "Description:" and "End:" a help text
# which explains what your testcase do and how.
#
# If it defines a new variable with tb.define_variable
# add the following section, where you explain the new
# variable.
#
# used variables
#
# - tb.config.varname
#|  some text, which describes the function of the variable
#|  default: 'default value'
#
# End:

from tbotlib import tbot

# add variables for your testcase with
tb.define_variable('varname', 'default value')
# also logging is done with this function
# access the variable with tb.config.varname

# add some logging info with
# logging.info("arg: ")

# compile, install and do tests
# call other testcases with
# tb.eof_call_tc("NAME OF TESTCASE")
# if the testcase must end without error
# or if you are interested in the return value with
# ret = tb.call_tc("NAME OF TESTCASE")

# Always end a testcase with tb.end_tc(True or False)
tb.end_tc(True)
