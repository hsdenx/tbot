# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simple set default values for linux testcases
#
# used variables
#
# - tb.config.i2c_pre
#|  string added before 'i2cget' command
#|  default: ''
#
# - tb.config.tc_lx_mount_dir
#|  path where testcase tc_lx_mount.py mounts
#|  default: '/home/hs/mnt'
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
# - tb.config.tc_workfd_lx_get_bc_file
#| path with filename to bootcounter file
#| default: '/sys/devices/soc0/soc/2100000.aips-bus/21a0000.i2c/i2c-0/0-0008/bootcount'
#
# - tb.config.devmem2_pre
#| if != 'none' added to devmem2 command
#| default: 'none'
#
# End:

from tbotlib import tbot

# set only once default variables
try:
    tb.config.tc_def_lx_set
except:
    logging.info("Setting linux defaults now")
    tb.define_variable('tc_lx_mount_dir', '/home/hs/mnt')
    tb.define_variable('tc_workfd_lx_get_bc_file', '/sys/devices/soc0/soc/2100000.aips-bus/21a0000.i2c/i2c-0/0-0008/bootcount')
    tb.define_variable('i2c_pre', 'empty')
    tb.define_variable('devmem2_pre', 'none')

tb.config.tc_def_lx_set = 'yes'
tb.gotprompt = True
tb.end_tc(True)
