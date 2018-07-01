# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -s labconfigname -c boardconfigname -t tc_workfd_get_uboot_config_vars.py
#
# try to get some configuration variables from the U-Boot
# source code, and save them in config variables.
#
# 'CONFIG_SYS_SDRAM_BASE' saved in tb.config.tc_ub_memory_ram_ws_base
# tb.config.tc_ub_memory_ram_ws_base_alt = tc_ub_memory_ram_ws_base + 0x100000
# tb.config.tc_ub_memory_ram_big depended on CONFIG_SYS_ARCH
# if CONFIG_SYS_ARCH == powerpc than yes else no
#
# used variables
#
# - tb.config.tc_ub_memory_ram_ws_base
#| base address for memory tests in RAM
#| if 'undef' testcase tc_workfd_get_uboot_config_vars.py
#| try to detect a good value from U-Boot config
#| default: 'undef'
#
# - tb.config.tc_ub_memory_ram_ws_base_alt
#| alternate address in RAM for memory tests
#| if 'undef' testcase tc_workfd_get_uboot_config_vars.py
#| try to detect a good value from U-Boot config
#| default: 'undef'
#
# - tb.config.tc_ub_memory_ram_big
#| big or little endian
#| if 'undef' testcase tc_workfd_get_uboot_config_vars.py
#| try to detect a good value from U-Boot config
#| default: 'undef'
#
# - tb.config.tc_ub_memory_base
#| only output the content of the 'help base' and
#| 'base' and 'md tb.config.tc_ub_memory_ram_ws_base 0xc'
#| command.
#| default: 'yes'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_ub_memory_ram_ws_base', 'undef')
tb.define_variable('tc_ub_memory_ram_ws_base_alt', 'undef')
tb.define_variable('tc_ub_memory_ram_big', 'undef')
tb.define_variable('tc_ub_memory_base', 'yes')

if (tb.config.tc_ub_memory_ram_ws_base == 'undef'):
    # Try to get the SDRAM Base
    tb.uboot_config_option = 'CONFIG_SYS_SDRAM_BASE'
    tb.eof_call_tc("tc_workfd_get_uboot_config_hex.py")
    tb.config.tc_ub_memory_ram_ws_base = tb.config_result
    tb.event.create_event('main', tb.config.boardname, "DUTS_UBOOT_SDRAM_BASE", tb.config.tc_ub_memory_ram_ws_base)

if (tb.config.tc_ub_memory_ram_ws_base_alt == 'undef'):
    try:
        tmp = int(tb.config.tc_ub_memory_ram_ws_base, 16)
    except:
        tb.end_tc(False)
    tmp += 1024 * 1024
    tb.config.tc_ub_memory_ram_ws_base_alt = hex(tmp)
    tb.event.create_event('main', tb.config.boardname, "DUTS_UBOOT_SDRAM_BASE_ALT", tb.config.tc_ub_memory_ram_ws_base_alt)

if (tb.config.tc_ub_memory_ram_big == 'undef'):
    # Try to get CONFIG_SYS_ARCH
    tb.uboot_config_option = 'CONFIG_SYS_ARCH'
    tb.eof_call_tc("tc_workfd_get_uboot_config_string.py")
    tb.config_result = tb.config_result.replace(" ", "")
    tb.config.uboot_arch = tb.config_result
    tb.event.create_event('main', tb.config.boardname, "DUTS_UBOOT_ARCH", tb.config.uboot_arch)
    if tb.config_result == 'powerpc':
        tb.config.tc_ub_memory_ram_big = 'yes'
    else:
        tb.config.tc_ub_memory_ram_big = 'no'

logging.info("detected: %s %s %s", tb.config.tc_ub_memory_ram_ws_base, tb.config.tc_ub_memory_ram_ws_base_alt,
             tb.config.tc_ub_memory_ram_big)

tb.end_tc(True)
