# SPDX-License-Identifier: GPL-2.0
#
# Description:
#
# - go to compile PC
# - goto lab source dir
# - get yocto sources with tc_workfd_get_yocto_source.py
# - bitbake it
# - check if files we expect exist
# - check tar content
# - deploy files (copy to lab PC)
# - get rootfs version
#
# End:

from tbotlib import tbot

tb.eof_call_tc("tc_connect_to_compilepc.py")

# go into tbot workdir
tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")

# now get the sources
tb.statusprint("get yocto sources")
tb.eof_call_tc("tc_workfd_get_yocto_source.py")

# source oe-init-build-env build
tb.write_lx_cmd_check(tb.workfd, 'source oe-init-build-env build')

# and bitbake what we want
bitbake_cmd = [
	"-q -q -q -c cleansstate core-image-minimal",
	"-q -q -q core-image-minimal",
]
for l in bitbake_cmd:
    tb.config.tc_workfd_bitbake_args = l
    tb.eof_call_tc("tc_workfd_bitbake.py")

# get used xenomai version
tb.eof_write_cmd_get_line(tb.workfd, 'ls tmp/work/cortexa8hf-neon-poky-linux-gnueabi/xenomai/')
tb.event.create_event('main', tb.config.boardname, "DUTS_XENOMAI_VERSION", tb.ret_write_cmd_get_line.rstrip())

# check if files we expect exist
for l in tb.config.yocto_check_result_files:
    tb.config.tc_workfd_check_if_file_exists_name = l
    tb.eof_call_tc("tc_workfd_check_if_file_exist.py")


# now test some content of the images
tb.config.tc_workfd_check_tar_content_endtc_onerror = 'yes'
tb.eof_call_tc("tc_workfd_check_tar_content.py")

for f in tb.config.tc_board_yocto_deploy_files:
    tb.config.tc_workfd_scp_opt = 'none'
    tb.config.tc_workfd_scp_from = f
    tb.config.tc_workfd_scp_to = tb.config.user + '@' + tb.config.ip + ':' + tb.config.yocto_results_dir_lab + os.path.basename(f)
    tb.eof_call_tc('tc_workfd_scp.py')

# get new rootfs version and save it for later
tb.eof_call_tc("tc_yocto_get_rootfs_from_tarball.py")

tb.end_tc(True)
