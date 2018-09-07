# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple set default values for tbot
#
# used variables
#
# - tb.config.ip
#| ip of the lab PC
#| default: ''
#
# - tb.config.user
#| username for loggin into lab PC
#| default: ''
#
# - tb.config.boardname
#| boardname: name of the board.
#| default: ''
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
# - tb.config.tc_lab_denx_power_tc
#| Name of testcase, which controlls power state of the board
#| default: 'tc_lab_denx_power.py'
#
# - tb.config.tc_lab_denx_get_power_state_tc
#| Name of the testcase, which reads the current powerstate of the board
#| default: 'tc_lab_denx_get_power_state.py'
#
# - tb.config.tc_lab_denx_connect_to_board_tc
#| Name of the testcase, which connects to boards console
#| default: 'tc_lab_denx_connect_to_board.py'
#
# - tb.config.tc_lab_denx_disconnect_from_board_tc
#| Name of the testcase, which disconnects from boards console
#| default: 'tc_lab_denx_disconnect_from_board.py'
#
# - tb.config.linux_prompt_default
#| linux default prompt, after login into console
#| default: 'root@generic-armv7a-hf:~# '
#
# - tb.config.labprompt
#| prompt of the lab, tbot set after login
#| default: tb.config.linux_prompt
#
# - tb.config.linux_prompt
#| prompt of the lab, tbot set after login
#| default: ''
#
# - tb.config.linux_user
#| Username for linux used on the board
#| default: 'root'
#
# - tb.config.create_dot
#| Call the "dot" backend after tbot finsihed
#| default: 'no'
#
# - tb.config.create_statistic
#| Call the "statistic" backend after tbot finsihed
#| default: 'no'
#
# - tb.config.create_dashboard
#| Call the "dashboard" backend after tbot finsihed
#| default: 'no'
#
# - tb.config.create_webpatch
#| Call the "webpatch" backend after tbot finsihed
#| default: 'no'
#
# - tb.config.create_html_log
#| Call the "html_log" backend after tbot finsihed
#| default: 'no'
#
# - tb.config.create_documentation
#| Call the "documentation" backend after tbot finsihed
#| default: 'no'
#
# - tb.config.event_documentation_strip_list
#| see documentation backend documentation
#| default: '[]'
#
# - tb.config.create_documentation_auto
#| see documentation backend documentation
#| default: '[]'
#
# - tb.config.create_junit
#| Call the "junit" backend after tbot finsihed
#| default: 'no'
#
# - tb.config.junit_tclist
#| list of testcasenames, for which the logfile get delivered to jenkins
#| default: "['tc_lab_get_uboot_source.py',
#|            'tc_workfd_set_toolchain.py', 'tc_workfd_compile_uboot.py',
#|            'tc_workfd_connect_with_kermit.py', 'tc_ub_upd_uboot.py',
#|            'tc_ub_upd_spl.py', 'tc_ub_check_version.py']"
#
# - tb.config.junit_ignlist
#| list of testcasesnames, which get not passed to jenkins
#| default: "['tc_workfd_check_cmd_success.py',
#|            'tc_dummy.py']"
#
# - tb.config.tb_set_after_linux
#| testcase called after logging into linux on board.
#| default: 'none'
#
# End:

from tbotlib import tbot

tb.define_variable('ip', '')
tb.define_variable('user', '')
tb.define_variable('boardname', '')
tb.define_variable('linux_prompt', '')
tb.define_variable('tb_set_after_linux', 'none')
tb.define_variable('junit_ignlist', "['tc_workfd_check_cmd_success.py', 'tc_dummy.py']")
tb.define_variable('junit_tclist', "['tc_lab_get_uboot_source.py', 'tc_workfd_set_toolchain.py', 'tc_workfd_compile_uboot.py', 'tc_workfd_connect_with_kermit.py', 'tc_ub_upd_uboot.py', 'tc_ub_upd_spl.py', 'tc_ub_check_version.py']")
tb.define_variable('create_junit', 'no')
tb.define_variable('event_documentation_strip_list', '[]')
tb.define_variable('create_documentation', 'no')
tb.define_variable('create_documentation_auto', 'no')
tb.define_variable('create_html_log', 'no')
tb.define_variable('create_webpatch', 'no')
tb.define_variable('create_dashboard', 'no')
tb.define_variable('create_statistic', 'no')
tb.define_variable('create_dot', 'no')
tb.define_variable('linux_user', 'root')
tb.define_variable('labprompt', tb.config.linux_prompt)
tb.define_variable('linux_prompt_default', 'root@generic-armv7a-hf:~# ')
tb.define_variable('tc_lab_denx_disconnect_from_board_tc', 'tc_lab_denx_disconnect_from_board.py')
tb.define_variable('tc_lab_denx_connect_to_board_tc', 'tc_lab_denx_connect_to_board.py')
tb.define_variable('tc_lab_denx_get_power_state_tc', 'tc_lab_denx_get_power_state.py')
tb.define_variable('tc_lab_denx_power_tc', 'tc_lab_denx_power.py')
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
tb.define_variable('state_uboot_timeout', '1')
tb.define_variable('uboot_autoboot_key', 'none')
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
if not tb.config.lab_tmp_dir.endswith(os.sep):
    tb.config.lab_tmp_dir + os.sep
if not tb.config.tc_lab_source_dir.endswith(os.sep):
    tb.config.tc_lab_source_dir + os.sep
if not tb.config.tc_workfd_work_dir.endswith(os.sep):
    tb.config.tc_workfd_work_dir + os.sep

tb.gotprompt = True
tb.end_tc(True)
