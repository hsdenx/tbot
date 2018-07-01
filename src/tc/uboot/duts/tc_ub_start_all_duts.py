# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start all DUTS tests
#
# only start the DUTS testcases, if tb.config.tc_ub_start_all_duts_start
# is set to True (default)
#
# used variables
#
# - tb.config.tc_ub_start_all_duts_start
#| if 'yes' start all duts testcases
#| default: 'yes'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_start_all_duts_start', 'yes')

tb.config.duts_junittclist = [
"tc_ub_duts_version.py",
"tc_ub_basic.py",
"tc_ub_bdinfo.py",
"tc_ub_boot.py",
"tc_ub_coninfo.py",
"tc_ub_download.py",
"tc_ub_environment.py",
"tc_ub_flinfo.py",
"tc_ub_i2c_help.py",
"tc_ub_memory.py",
"tc_ub_run.py",
"tc_ub_date.py",
"tc_ub_dtt.py",
"tc_ub_duts_source.py",
"tc_ub_duts_fdt.py",
"tc_ub_duts_go.py",
"tc_ub_bdinfo.py",
"tc_ub_duts_hush.py",
]

if tb.config.tc_ub_start_all_duts_start == 'no':
    tb.end_tc(True)

dutslist = [
"uboot/duts/tc_ub_duts_version.py",
"uboot/duts/tc_ub_basic.py",
"uboot/duts/tc_ub_bdinfo.py",
"uboot/duts/tc_ub_boot.py",
"uboot/duts/tc_ub_coninfo.py",
"uboot/duts/tc_ub_download.py",
"uboot/duts/tc_ub_environment.py",
"uboot/duts/tc_ub_flinfo.py",
"uboot/duts/tc_ub_i2c_help.py",
"uboot/duts/tc_ub_memory.py",
"uboot/duts/tc_ub_run.py",
"uboot/duts/tc_ub_date.py",
"uboot/duts/tc_ub_dtt.py",
"tc_ub_duts_source.py",
"tc_ub_duts_fdt.py",
"tc_ub_duts_go.py",
"tc_ub_bdinfo.py",
"tc_ub_duts_hush.py",
]

for tc in dutslist:
  tb.eof_call_tc(tc)

tb.end_tc(True)
