# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_goto_lab_source_dir.py
# switch into lab PC source directory tb.config.tc_lab_source_dir
# set TBOT_BASEDIR to tb.config.tc_lab_source_dir
# End:

from tbotlib import tbot
logging.info("args: %s", tb.workfd)

try:
    tb.workfd.tc_lab_source_dir_checked
except:
    tb.workfd.tc_lab_source_dir_checked = False

if tb.workfd.tc_lab_source_dir_checked == False:
    if tb.workfd.name == 'tb_cpc':
        try:
            tb.config.compile_pc_workdir
        except:
            tb.config.compile_pc_workdir = tb.config.tc_lab_source_dir

        tmp = 'export TBOT_BASEDIR=' + tb.config.compile_pc_workdir
    else:
        tmp = 'export TBOT_BASEDIR=' + tb.config.tc_lab_source_dir
    tb.write_lx_cmd_check(tb.workfd, tmp, create_doc_event=True)

    self.event.create_event('main', 'tc_workfd_goto_lab_source_dir.py', 'SET_DOC_FILENAME', 'TBOT_BASEDIR_check_exist')
    tb.config.tc_workfd_check_if_dir_exists_name = '$TBOT_BASEDIR'
    ret = tb.call_tc("tc_workfd_check_if_dir_exist.py")
    if ret == False:
        tmp = 'mkdir $TBOT_BASEDIR'
        tb.write_lx_cmd_check(tb.workfd, tmp, create_doc_event=True)

    tb.workfd.tc_lab_source_dir_checked = True

tmp = "cd $TBOT_BASEDIR"
tb.write_lx_cmd_check(tb.workfd, tmp, create_doc_event=True)

tb.end_tc(True)
