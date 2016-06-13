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
# start with
# python2.7 src/common/tbot.py -c config/tbot_dxr2_uboot_kconfig_check.cfg -t tc_uboot_get_arch.py
# get architecture from u-boot config
from tbotlib import tbot

logging.info("args: %s", tb.tc_workfd_grep_file)

archs = ['ARC', 'ARM', 'AVR32', 'BLACKFIN', 'M68K', 'MICROBLAZE', 'MIPS', 'NDS32', 'NIOS2', 'OPENRISC', 'PPC', 'SANDBOX', 'SH', 'SPARC', 'X86']
archs_ret = ['arc', 'arm', 'avr32', 'blackfin', 'm68k', 'microblaze', 'mips', 'nds32', 'nios2', 'openrisc', 'powerpc', 'sandbox', 'sh', 'sparc', 'x86']

tb.cur_uboot_arch = 'undef'
index = 0
result = False
for arch in archs:
    if arch == 'SANDBOX':
        tb.tc_workfd_grep_string = 'CONFIG_' + arch
    else:
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
