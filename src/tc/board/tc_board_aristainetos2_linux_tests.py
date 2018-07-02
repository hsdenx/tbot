# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start all linux testcases for the aristainetos2 board
# End:

from tbotlib import tbot
import time

tb.workfd = tb.c_ctrl

tb.eof_call_tc("tc_workfd_goto_linux_code.py")

# compile it
tb.eof_call_tc("tc_workfd_compile_linux.py")

# copy files to tftpdir
tb.statusprint("copy files")
c = tb.workfd
so = "/work/hs/tbot/linux-aristainetos/arch/arm/boot/uImage"
ta = "/tftpboot/aristainetos/tbot/uImage-hs-cur"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "/work/hs/tbot/linux-aristainetos/arch/arm/boot/dts/imx6dl-aristainetos2_4.dtb"
ta = "/tftpboot/aristainetos/tbot/imx6dl-aristainetos2_4.dtb"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "/work/hs/tbot/linux-aristainetos/arch/arm/boot/dts/imx6dl-aristainetos2_7.dtb"
ta = "/tftpboot/aristainetos/tbot/imx6dl-aristainetos2_7.dtb"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "/work/hs/tbot/linux-aristainetos/aristainetos2.itb"
ta = "/tftpboot/aristainetos/tbot/aristainetos2.itb"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

# call uboot tc to go into u-boot, and after that boot new kernel
tb.set_board_state("u-boot")
tb.eof_write_cmd(tb.c_con, "version")

tb.workfd = tb.c_con

# board needs some seconds to get ethernet working ...
time.sleep(15)

tb.eof_call_tc("tc_lx_uname.py")

time.sleep(15)

tb.statusprint("linux dmesg checks")
checks = ['Machine model: aristainetos2',
'Linux version',
'Kernel command line',
'Brought up 2 CPU',
'Initialized drm',
'Creating 1 MTD partitions on "gpmi-nand":',
'm25p80 spi3.1: n25q128a11 (16384 Kbytes)',
'Creating 4 MTD partitions on "spi3.1":',
'fec 2188000.ethernet eth0: registered PHC',
'e1000e: Intel(R) PRO/1000 Network Driver',
'rtc-ds1307 2-0068: rtc core: registered m41t00 as rtc0',
'atmel_mxt_ts 2-004b: Touchscreen size X4095Y4095',
'atmel_mxt_ts 2-004b: Family: 128 Variant: 1 Firmware V1.6.AB Objects: 17',
'imx2-wdt 20bc000.wdog: timeout 60 sec (nowayout=0)',
'mmc0: SDHCI controller on 2190000.usdhc',
'mmc1: SDHCI controller on 2194000.usdhc',
'imx-drm display-subsystem: bound imx-ipuv3-crtc.2 (ops ipu_crtc_ops)',
'imx-drm display-subsystem: bound display@di0 (ops imx_pd_ops)',
'Console: switching to colour frame buffer device 60x50',
'rtc-ds1307 2-0068: rtc core: registered m41t00 as rtc0'
]

for tb.config.tc_lx_dmesg_grep_name in checks:
    tb.eof_call_tc("tc_lx_dmesg_grep.py")

tb.statusprint("pinmux check")
files = ['src/files/aristainetos2_pinmux.reg']
for tb.config.tc_lx_create_reg_file_name in files:
    tb.eof_call_tc("tc_lx_check_reg_file.py")

# tb.statusprint("ubi checks")
# tb.eof_call_tc("tc_lx_ubi_tests.py")
# tb.eof_call_tc("tc_board_dxr2_lx_ubi_tests.py")

tb.end_tc(True)
