# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple set default values for linux testcases
#
# used variables
#
# - tb.config.tc_lx_mount_dir
#|  path where testcase tc_lx_mount.py mounts
#|  default: '/home/hs/mnt'
#
# - tb.config.tc_return
#| value set from various testcases.
#| used as return value.
#
#
# - tb.config.uboot_get_parameter_file_list
#| list of files, where TC searches for the define
#| used by: tc_workfd_get_uboot_config_string.py
#| tc_workfd_get_uboot_config_hex.py
#| default: ''
#
# - tb.config.uboot_config_option
#| config option which get searched
#| used by: tc_workfd_get_uboot_config_string.py
#| tc_workfd_get_uboot_config_hex.py
#| default: ''
#
# End:

from tbotlib import tbot

# set only once default variables
try:
    tb.config.tc_def_lx_set
except:
    logging.info("Setting linux defaults now")
    tb.define_variable('tc_lx_mount_dir', '/home/hs/mnt')

tb.config.tc_def_lx_set = 'yes'
tb.gotprompt = True
tb.end_tc(True)
