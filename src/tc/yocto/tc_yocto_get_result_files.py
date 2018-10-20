# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# If we use a compile PC we must copy the result files
# from tb.config. yocto_deploy_dir to 
# tb.config.tc_demo_yocto_all_result_dir
#
# End:

from tbotlib import tbot

try:
    tb.c_cpc
    with_compilepc = 1
except:
    with_compilepc = 0

for f in tb.config.yocto_check_result_files:
    fr = tb.config.yocto_deploy_dir + os.path.basename(f)
    to = tb.config.tc_demo_yocto_all_result_dir + os.path.basename(f)

    if with_compilepc:
        tb.config.tc_workfd_scp_opt = ''
        tb.config.tc_workfd_scp_from = fr
        tb.config.tc_workfd_scp_to = tb.config.user + '@' + tb.config.ip + ':' + to
        tb.eof_call_tc('tc_workfd_scp.py')
    else:
        tb.config.tc_workfd_cp_file_from = fr
        tb.config.tc_workfd_cp_file_to = to
        tb.eof_call_tc("tc_workfd_cp_file.py")

tb.end_tc(True)
