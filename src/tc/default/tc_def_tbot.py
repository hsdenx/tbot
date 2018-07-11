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
# - tb.config.lab_tmp_dir
#| directory on lab PC, where tbot stores temporary files.
#| default: '/var/tmp'
#
# End:

from tbotlib import tbot

tb.define_variable('uboot_strings', "['Autobooting in', 'noautoboot',  'autoboot', 'EOF', 'RomBOOT']")
tb.define_variable('tc_lab_source_dir', '/work/hs/tbot')
tb.define_variable('tc_workfd_work_dir', tb.config.tc_lab_source_dir)
tb.define_variable('tc_workfd_tbotfiles_dir', tb.config.tc_workfd_work_dir + '/tmpfiles')
tb.define_variable('board_has_debugger', 'no')
tb.define_variable('lab_tmp_dir', '/var/tmp')

# set all path variables with an ending os.sep
if not tb.config.lab_tmp_dir.endwith(os.sep):
    tb.config.lab_tmp_dir + os.sep
if not tb.config.tc_lab_source_dir.endwith(os.sep):
    tb.config.tc_lab_source_dir + os.sep
if not tb.config.tc_workfd_work_dir.endwith(os.sep):
    tb.config.tc_workfd_work_dir + os.sep

tb.gotprompt = True
tb.end_tc(True)
