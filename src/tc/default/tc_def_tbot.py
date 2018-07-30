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
# - tb.config.compile_pc_workdir
#| tbots workdirectory on compile PC
#| default: tb.config.tc_lab_source_dir
#
# - tb.config.debug
#| If 'True' enable debugprint() output
#| default: 'False'
#
# - tb.config.debugstatus
#| If 'True' enable statusprintf() output
#| default: 'False'
#
# - tb.config.state_uboot_timeout
#| u-boot read timeout in seconds (float)
#| default: '1'
#
# - tb.config.uboot_autoboot_key
#| U-Boots autoboot key, send if autoboot is read, and != 'none'
#| default: 'none'
#
# - tb.config.tb_power_state
#| last read powerstate
#| default: 'undef'
#
# - tb.config.term_line_length
#| maximal line length of terminal
#| default: '200'
#
# - tb.config.wdt_timeout
#| wdt timeout in seconds
#| default: '120'
#
# - tb.config.state_linux_timeout
#| linux timeout in seconds when reading from channel
#| default: '4'
#
# - tb.config.labsshprompt
#| prompt after login into lab with ssh
#| default: '$ '
#
# - tb.config.tc_return
#| used as return value from testcases
#| default: 'True'
#
# - tb.config.ub_boot_linux_cmd
#| bootcommand for booting linux
#| default: 'run tbot_boot_linux'
#
# - tb.config.do_connect_to_board
#| connect to boards console on tbot start
#| default: 'True'
#
# - tb.config.tftpboardname
#| tftp subdir name for board
#| default: tb.config.boardname
#
# - tb.config.boardlabname
#| boardsname in the lab
#| default: tb.config.boardname
#
# - tb.config.boardlabpowername
#| boards name in the lab for power on/off
#| default: tb.config.boardname
#
# - tb.config.tftpboardrootdir
#| root path for tftp directory (if needed for u-boot)
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('tftpboardrootdir', 'none')
tb.define_variable('tftpboardname', tb.config.boardname)
tb.define_variable('boardlabname', tb.config.boardname)
tb.define_variable('boardlabpowername', tb.config.boardname)
tb.define_variable('do_connect_to_board', 'True')
tb.define_variable('ub_boot_linux_cmd', 'run tbot_boot_linux')
tb.define_variable('tc_return', 'True')
tb.define_variable('labsshprompt', '$ ')
tb.define_variable('state_linux_timeout', '4')
tb.define_variable('wdt_timeout', '120')
tb.define_variable('term_line_length', '200')
tb.define_variable('tb_power_state', 'undef')
tb.define_variable('debug', 'False')
tb.define_variable('debugstatus', 'False')
tb.define_variable('uboot_strings', "['Autobooting in', 'noautoboot',  'autoboot', 'EOF', 'RomBOOT']")
tb.define_variable('tc_lab_source_dir', '/work/hs/tbot')
tb.define_variable('tc_workfd_work_dir', tb.config.tc_lab_source_dir)
tb.define_variable('tc_workfd_tbotfiles_dir', tb.config.tc_workfd_work_dir + '/tmpfiles')
tb.define_variable('board_has_debugger', 'no')
tb.define_variable('lab_tmp_dir', '/var/tmp')
tb.define_variable('compile_pc_workdir', tb.config.tc_lab_source_dir)

# set all path variables with an ending os.sep
if not tb.config.lab_tmp_dir.endwith(os.sep):
    tb.config.lab_tmp_dir + os.sep
if not tb.config.tc_lab_source_dir.endwith(os.sep):
    tb.config.tc_lab_source_dir + os.sep
if not tb.config.tc_workfd_work_dir.endwith(os.sep):
    tb.config.tc_workfd_work_dir + os.sep

tb.gotprompt = True
tb.end_tc(True)
