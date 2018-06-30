# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# tbot.py -s lab_denx -c cfgfile -t tc_def_tbot.py
# simple set default values for tbot
# End:

from tbotlib import tbot

try:
    tb.config.tc_lab_source_dir
except AttributeError:
    tmp = tb.config.tc_lab_source_dir + '/u-boot-tqm5200'
    tb.config.__dict__.update({'tc_lab_source_dir' : tmp})

try:
    tb.config.tc_workfd_tbotfiles_dir
except AttributeError:
    tmp = tb.config.tc_workfd_work_dir + "/tmpfiles"
    tb.config.__dict__.update({'tc_workfd_tbotfiles_dir' : tmp})

tb.gotprompt = True
tb.end_tc(True)
