# This file is part of tbot.  tbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
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
