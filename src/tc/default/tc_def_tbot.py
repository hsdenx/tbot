# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple set default values for tbot
#
# used variables
#
# - tb.config.uboot_strings
#| Strings found when U-Boot is booting
#| default: "['Autobooting in', 'noautoboot',  'autoboot', 'EOF', 'RomBOOT']"
#
# - tb.config.tc_lab_source_dir
#| tbot source directory on lab PC
#| default: '/work/hs/tbot'
#
# - tb.config.tc_workfd_work_dir
#| tbots workdirectory on labor PC
#| default: tb.config.tc_lab_source_dir
#
# - tb.config.tc_workfd_tbotfiles_dir
#| place for tbot to store tempfiles on labor PC
#| default: tb.config.tc_workfd_work_dir + '/tmpfiles'
#
# - tb.config.board_has_debugger
#| if 'yes' board has a debugger
#| default: 'no'
#
# End:

from tbotlib import tbot

tb.define_variable('uboot_strings', "['Autobooting in', 'noautoboot',  'autoboot', 'EOF', 'RomBOOT']")
tb.define_variable('tc_lab_source_dir', '/work/hs/tbot')
tb.define_variable('tc_workfd_work_dir', tb.config.tc_lab_source_dir)
tb.define_variable('tc_workfd_tbotfiles_dir', tb.config.tc_workfd_work_dir + '/tmpfiles')
tb.define_variable('board_has_debugger', 'no')

tb.gotprompt = True
tb.end_tc(True)
