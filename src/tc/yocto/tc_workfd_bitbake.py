# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# simple call bitbake with tb.config.tc_workfd_bitbake_args
#
# if tb.config.tc_workfd_bitbake_machine is != 'none', also cat
# the content of the newest file in tmp/log/cooker/" + tb.config.tc_workfd_bitbake_machine + "/*
#
# used variables:
#
# - tb.config.tc_workfd_bitbake_machine
#| if != 'none' add "MACHINE=tb.config.tc_workfd_bitbake_machine " bofore
#| bitbake command.
#| default: 'none'
#
# - tb.config.tc_workfd_bitbake_args
#| arguments for bitbake command
#| default: ''
#
# End:

from tbotlib import tbot

tb.define_variable('tc_workfd_bitbake_machine', 'none')
tb.define_variable('tc_workfd_bitbake_args', '')

logging.info("args: %s %s", tb.workfd, tb.config.tc_workfd_bitbake_args)

tlist = [
	'pid',
	'tasks',
	'Loading',
	'NOTE',
	'recipe'
]

if tb.config.tc_workfd_bitbake_machine != 'none':
    cmd = 'MACHINE=' + tb.config.tc_workfd_bitbake_machine + ' '
else:
    cmd = ''

cmd += 'bitbake ' + tb.config.tc_workfd_bitbake_args
tb.write_lx_cmd_check(tb.workfd, cmd, triggerlist=tlist)

if tb.config.tc_workfd_bitbake_machine != 'none':
    # list newest file in tmp/log/cooker/<machine>/*
    ma = tb.config.tc_workfd_bitbake_machine

    cmd = "ls -t tmp/log/cooker/" + ma + "/* | head -n1"
    tb.eof_write_cmd_get_line(tb.workfd, cmd)

    self.event.create_event('main', 'tc_workfd_bitbake.py', 'SET_DOC_FILENAME', 'get_build_info')
    cmd = 'head -60 ' + tb.ret_write_cmd_get_line.rstrip()
    tb.eof_write(tb.workfd, cmd)
    searchlist = ['NOTE', 'BB_VERSION', 'BUILD_SYS', 'NATIVELSBSTRING', 'TARGET_SYS',
		'MACHINE', 'DISTRO_VERSION'
	]
    tmp = True
    while tmp == True:
        ret = tb.tbot_rup_and_check_strings(tb.workfd, searchlist)
        if ret == 'prompt':
            tmp = False
        elif ret == '0':
            self.tbot_trigger_wdt()
        else:
            val = searchlist[int(ret)]
            ret = tb.tbot_expect_string(tb.workfd, '\n')
            if ret == 'prompt':
                tb.end_tc(False)
            v = tb.buf.rstrip()
            v = v.split('"')
            tb.event.create_event('main', tb.config.boardname, "DUTS_" + val, v[1])

tb.end_tc(True)
