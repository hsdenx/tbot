# This file is part of tbot.  tbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Description:
# start with
# tbot.py -s lab_denx -c cuby -t tc_board_cuby_yocto_install.py
# install yocto for the cuby board, and bitbake.
# End:

from tbotlib import tbot

tb.eof_call_tc("tc_connect_to_compilepc.py")

# go into tbot workdir
tb.eof_call_tc("tc_workfd_goto_lab_source_dir.py")

# now get the sources
tb.statusprint("cuby get yocto sources")
tb.eof_call_tc("tc_workfd_get_yocto_source.py")

# get the current meta-cuby branch and commit
tb.config.tc_git_get_branch_commit_tree = '$TBOT_BASEDIR_YOCTO/meta-cuby'
tb.eof_call_tc("tc_git_get_branch_commit.py")

tb.eof_call_tc("tc_workfd_get_yocto_source.py")
# source oe-init-build-env build
tb.write_lx_cmd_check(tb.workfd, 'source oe-init-build-env build')

# and bitbake sdk and rootfs qt-cuby
bitbake_cmd = [
	"-q -q -q qt-cuby -c cleansstate",
	"-q -q -q -c do_populate_sdk qt-cuby",
	"-q -q -q qt-cuby",
]

for l in bitbake_cmd:
    tb.config.tc_workfd_bitbake_args = l
    tb.eof_call_tc("tc_workfd_bitbake.py")

# check if some host files are created
p = 'build/tmp/sysroots/x86_64-linux'
p = 'build/tmp/work/cuby-poky-linux-gnueabi/qt-cuby/1.0-r0/recipe-sysroot-native'
files_host_exist = [
	"$TBOT_BASEDIR_YOCTO/" + p + "/usr/bin/mcopy",
	"$TBOT_BASEDIR_YOCTO/" + p + "/usr/bin/uboot-mkimage",
	"$TBOT_BASEDIR_YOCTO/" + p + "/usr/sbin/parted",
	"$TBOT_BASEDIR_YOCTO/" + p + "/usr/sbin/mkfs.vfat"
]
for l in files_host_exist:
    tb.config.tc_workfd_check_if_file_exists_name = l
    tb.eof_call_tc("tc_workfd_check_if_file_exist.py")

# and bitbake cuby image (swu file for swupdate, including
# signed FIT image)
bitbake_cmd = [
	"-q -q -q cuby-image -c cleansstate",
	"-q -q -q cuby-image",
]

for l in bitbake_cmd:
    tb.config.tc_workfd_bitbake_args = l
    tb.eof_call_tc("tc_workfd_bitbake.py")

# check if files we want exist
files_exist = [
	"$TBOT_BASEDIR_YOCTO/build/tmp/deploy/images/cuby/qt-cuby-signed-cuby.itb",
	"$TBOT_BASEDIR_YOCTO/build/tmp/deploy/images/cuby/MLO",
	"$TBOT_BASEDIR_YOCTO/build/tmp/deploy/images/cuby/MLO.byteswap",
	"$TBOT_BASEDIR_YOCTO/build/tmp/deploy/images/cuby/u-boot-key-cuby.dtb",
	"$TBOT_BASEDIR_YOCTO/build/tmp/deploy/images/cuby/u-boot.img",
	"$TBOT_BASEDIR_YOCTO/build/tmp/deploy/images/cuby/cuby-image-cuby.swu",
	"$TBOT_BASEDIR_YOCTO/build/tmp/deploy/images/cuby/cuby-image-cuby-rootfs-cuby-sd.img",
	"$TBOT_BASEDIR_YOCTO/build/tmp/deploy/sdk/poky-glibc-x86_64-qt-cuby-armv7ahf-neon-toolchain-2.*.sh",
]

for l in files_exist:
    tb.config.tc_workfd_check_if_file_exists_name = l
    tb.eof_call_tc("tc_workfd_check_if_file_exist.py")

# now test some content of the images
tb.config.tc_workfd_check_tar_content_endtc_onerror = True
tb.eof_call_tc("tc_workfd_check_tar_content.py")

for f in tb.config.tc_board_cuby_yocto_deploy_files:
    tb.config.tc_workfd_scp_opt = ''
    tb.config.tc_workfd_scp_from = "$TBOT_BASEDIR_YOCTO/build/tmp/deploy/" + f
    tb.config.tc_workfd_scp_to = tb.config.user + '@' + tb.config.ip + ':' + tb.config.tc_board_cuby_yocto_result_dir + os.path.basename(f)
    tb.call_tc('tc_workfd_scp.py')

# get new rootfs version and save it for later
# we do this on the lab PC, so ... change workfd
tb.workfd = tb.c_ctrl
tb.eof_call_tc("tc_yocto_get_rootfs_from_tarball.py")

tb.end_tc(True)
