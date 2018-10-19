# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple set default values for yocto testcases
#
# used variables
#
# - tb.config.tc_demo_yocto_all_result_dir
#| path to directory where images from yocto
#| build get stored. If this dir does not exist
#| create it.
#| default: tb.config.tc_lab_source_dir + '/yocto-results/' + tb.boardname + '/'
#
# - tb.config.tc_workfd_bitbake_machine
#| if != 'none' add "MACHINE=tb.config.tc_workfd_bitbake_machine " bofore
#| bitbake command.
#| default: tb.config.boardname
#
# - tb.config.yocto_builddir
#| name of yocto builddir
#| default: "$TBOT_BASEDIR_YOCTO/build_" + tb.config.tc_workfd_bitbake_machine + "/"
#
# - tb.config.yocto_deploy_dir
#| path to yocto deploy dir
#| default: tb.config.yocto_builddir + 'tmp/deploy/images/' + tb.config.tc_workfd_bitbake_machine
#
# - tb.config.yocto_check_result_files
#| files we expect after successfull yocto build
#| default: ''
#
# End:

from tbotlib import tbot

# set only once default variables
try:
    tb.config.tc_def_yocto_set
except:
    logging.info("Setting yocto defaults now")
    try:
        tb.config.tc_demo_yocto_all_result_dir
    except:
        p = tb.config.tc_lab_source_dir + '/yocto-results/' + tb.config.boardname + '/'
        tb.config.tc_demo_yocto_all_result_dir = p
        tb.config.tc_workfd_linux_mkdir_dir = p
        s = tb.workfd
        tb.workfd = tb.c_ctrl
        tb.eof_call_tc("tc_workfd_linux_mkdir.py");
        tb.workfd = s
        logging.info("default tb.config.tc_demo_yocto_all_result_dir = %s", tb.config.tc_demo_yocto_all_result_dir)

    tb.define_variable('tc_workfd_bitbake_machine', tb.config.boardname)
    tb.define_variable('yocto_builddir', "$TBOT_BASEDIR_YOCTO/build_" + tb.config.tc_workfd_bitbake_machine + "/")
    tb.define_variable('yocto_deploy_dir', tb.config.yocto_builddir + 'tmp/deploy/images/' + tb.config.tc_workfd_bitbake_machine + "/")
    tb.define_variable('yocto_check_result_files', 'empty')

tb.config.tc_def_yocto_set = 'yes'
tb.gotprompt = True
tb.end_tc(True)
