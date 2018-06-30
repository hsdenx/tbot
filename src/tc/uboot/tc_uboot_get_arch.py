# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start with
# python2.7 src/common/tbot.py -c config/tbot_dxr2_uboot_kconfig_check.cfg -t tc_uboot_get_arch.py
# get architecture from u-boot config
# End:

from tbotlib import tbot

logging.info("args: %s", tb.tc_workfd_grep_file)

archs = ['ARC', 'ARM64', 'ARM', 'AVR32', 'BLACKFIN', 'M68K', 'MICROBLAZE', 'MIPS', 'NDS32', 'NIOS2', 'OPENRISC', 'PPC', 'SANDBOX', 'SH', 'SPARC', 'X86']
archs_ret = ['arc', 'arm64', 'arm', 'avr32', 'blackfin', 'm68k', 'microblaze', 'mips', 'nds32', 'nios2', 'openrisc', 'powerpc', 'sandbox', 'sh', 'sparc', 'x86']

tb.cur_uboot_arch = 'undef'
index = 0
result = False
for arch in archs:
    tb.tc_workfd_grep_string = 'CONFIG_' + arch + '=y'
    ret = tb.call_tc("tc_workfd_grep.py")
    if ret == False:
        index += 1
        continue
    else:
        tb.cur_uboot_arch = archs_ret[index]
        result = True
        break

tb.end_tc(result)
