# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_lx_mtdutils_install.py
# check if mtdutils are installed. If not, clone the code with
# git clone git://git.infradead.org/mtd-utils.git mtd-utils
# and install it
# End:

from tbotlib import tbot

logging.info("args: %s", tb.config.tc_workfd_work_dir)

# set board state for which the tc is valid
tb.set_board_state("linux")

c = tb.c_con
# check if mtdinfo exist
tb.config.tc_workfd_check_if_cmd_exist_cmdname = 'mtdinfo'
tb.workfd = tb.c_con
ret = tb.call_tc("tc_workfd_check_if_cmd_exist.py")
if ret == True:
    # check if mtdinfo exist
    tb.config.tc_workfd_check_if_cmd_exist_cmdname = 'ubinfo'
    tb.config.tc_ubi_cmd_path = ''
    ret = tb.call_tc("tc_workfd_check_if_cmd_exist.py")
    if ret == True:
        tb.end_tc(True)

tb.eof_call_tc("tc_workfd_goto_tbot_workdir.py")

# if not download it
# git clone git://git.infradead.org/mtd-utils.git mtd-utils
tb.workfd = tb.c_con
tb.config.tc_workfd_check_if_dir_exists_name = "mtd-utils"
ret = tb.call_tc("tc_workfd_check_if_dir_exist.py")
if ret == False:
    tmp = 'git clone git://git.infradead.org/mtd-utils.git mtd-utils'
    tb.eof_write(c, tmp)
    tb.tbot_expect_prompt(c)
    tb.eof_call_tc("tc_workfd_check_cmd_success.py")

# cd into dir
tb.eof_write_con_lx_cmd('cd mtd-utils')

# if code is compiled, exit
tb.config.tc_workfd_check_if_file_exists_name = 'ubi-utils/mtdinfo'
ret = tb.call_tc("tc_workfd_check_if_file_exist.py")
if ret == True:
    tb.config.tc_ubi_cmd_path = tb.config.tc_workfd_work_dir + '/mtd-utils'
    tb.end_tc(True)

# apply patches if any
# use src/tc/tc_lab_apply_patches.py
# but this is for ctrl fd ...

# compile it
tb.eof_write_con_lx_cmd('make')

# install it ...
# tb.eof_write_con_lx_cmd('cp devmem2 /usr/local/bin')
# tb.workfd = tb.c_con
# tb.eof_call_tc("tc_workfd_check_cmd_success.py")
tb.config.tc_ubi_cmd_path = tb.config.tc_workfd_work_dir + '/mtd-utils'
tb.end_tc(True)
