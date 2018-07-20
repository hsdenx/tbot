# SPDX-License-Identifier: GPL-2.0
#
# Description:
# start all linux testcases for the fipad board
# End:

from tbotlib import tbot

tb.workfd = tb.c_ctrl

# delete old linux source tree
tb.eof_call_tc("tc_workfd_rm_linux_code.py")

tb.eof_call_tc("tc_workfd_get_linux_source.py")

tb.eof_call_tc("tc_workfd_goto_linux_code.py")

# compile it
tb.eof_call_tc("tc_workfd_compile_linux.py")

# copy files to tftpdir
c = tb.workfd
tb.statusprint("copy files")
so = "/work/hs/tbot/linux-fipad/arch/arm/boot/zImage"
ta = "/tftpboot/fipad/tbot/zImage"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "/work/hs/tbot/linux-fipad/arch/arm/boot/dts/bosch-mpc1360d.dtb"
ta = "/tftpboot/fipad/tbot/fipad.dtb"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)
so = "/work/hs/tbot/linux-fipad/System.map"
ta = "/tftpboot/fipad/tbot/linux-system.map"
tb.eof_call_tc("tc_lab_cp_file.py", ch=c, s=so, t=ta)

# call ubot setenv
tb.set_board_state("u-boot")
tb.eof_write_cmd(tb.c_con, "version")

tb.workfd = tb.c_con

ret = tb.eof_call_tc("tc_lx_get_version.py")
if ret == False:
    tb.end_tc(False)

tb.statusprint("Linux vers: %s" % (tb.config.tc_return))

tmp = tb.config.tc_return.split()
if tmp[0][0] == '4':
    lx_vers = '4'
else:
    lx_vers = '3'

tb.set_board_state("linux")

tb.statusprint("tc_fipad linux checking for Linux Version %s" % (lx_vers))
# dmesg checks
tb.statusprint("tc_fipad linux dmesg checks")
if lx_vers == '3':
	checks = ['model: MSC nanoRISC i.MX6SOLO',
	'Linux version',
	'Kernel command line',
	'Memory: 512MB = 512MB total',
	'l2x0: 16 ways, CACHE_ID 0x410000c8, AUX_CTRL 0x32450000, Cache size: 524288 B',
	'Creating 4 MTD partitions on',
	'flexcan 2090000.can: device registered',
	'Generic MDIO gpio-0:10',
	'eth0: registered PHC',
	'input: bu21029',
	'input: pwm-beeper',
	'at24 2-0054: 8192 byte 24c64 EEPROM, writable, 32 bytes/write',
	'da9063 2-0058: Device detected (chip-ID: 0x61, var-ID: 0x50)',
	'input: da9063-onkey',
	'da9063-rtc da9063-rtc: IRQ is',
	'da9063-rtc da9063-rtc: rtc core: registered da9063-rtc',
	'at24 3-0050: 131072 byte 24c1024 EEPROM, writable, 128 bytes/write',
	'da9063-battery da9063-battery: Iset=6000uA, Vset=3100mV'
	]
else:
	# linux 4.x checks
	checks = ['model: MSC nanoRISC i.MX6SOLO',
	'Linux version',
	'Kernel command line',
	'L2C-310: CACHE_ID 0x410000c8, AUX_CTRL 0x76450001',
	'Creating 4 MTD partitions on',
	'flexcan 2090000.flexcan: device registered',
	'imx-drm display-subsystem: bound display@di0 (ops imx_pd_ops)',
	'mdio_bus gpio-0:10',
	'eth0: registered PHC',
	'input: bu21029',
	'input: pwm-beeper',
	'at24 4-0054: 8192 byte 24c64 EEPROM, writable, 32 bytes/write',
	'da9063 4-0058: Device detected (chip-ID: 0x61, var-ID: 0x50)',
	'input: da9063-onkey',
	#'da9063-rtc da9063-rtc: IRQ is',
	'da9063-rtc da9063-rtc: rtc core: registered da9063-rtc',
	'at24 5-0050: 131072 byte 24c1024 EEPROM, writable, 128 bytes/write',
	'da9063-battery da9063-battery: Iset=6000uA, Vset=3100mV'
	]

for tb.config.tc_lx_dmesg_grep_name in checks:
    tb.eof_call_tc("tc_lx_dmesg_grep.py")

# register checks
tb.statusprint("tc_fipad pinmux check")
files = ['src/files/fipad_lx_pinmux.reg',
         'src/files/fipad_lx_pwm.reg',
         'src/files/fipad_lx_ipu.reg']
for tb.config.tc_lx_create_reg_file_name in files:
    tb.eof_call_tc("tc_lx_check_reg_file.py")

# do some basic tests
tb.statusprint("tc_fipad basic checks")
if lx_vers == '3':
	basiclist = [{"cmd":"cat /sys/bus/i2c/devices/0-0040/name", "val":"bu21029"},
              {"cmd":"cat /sys/class/thermal/thermal_zone0/temp", "val":"undef"},
              {"cmd":"cat /sys/bus/i2c/devices/i2c-2/name", "val":"i2c-1-mux (chan_id 0)"},
              {"cmd":"cat /sys/bus/i2c/devices/i2c-3/name", "val":"i2c-1-mux (chan_id 1)"},
              {"cmd":"cat /sys/bus/i2c/devices/2-0054/name", "val":"24c64"},
              {"cmd":"cat /sys/bus/i2c/devices/3-0050/name", "val":"24c1024"},
              {"cmd":"cat /sys/bus/i2c/devices/2-0058/name", "val":"da9063"},
              {"cmd":"cat /sys/class/leds/debug-green/trigger", "val":"none nand-disk mmc0 mmc1 mmc2 timer [heartbeat] backlight gpio cpu0"},
              {"cmd":"cat /sys/class/leds/debug-yellow/trigger", "val":"none nand-disk mmc0 [mmc1] mmc2 timer heartbeat backlight gpio cpu0"},
              {"cmd":"cat /sys/class/leds/system-fault/trigger", "val":"none nand-disk mmc0 mmc1 mmc2 timer heartbeat backlight gpio [cpu0]"},
              {"cmd":"cat /sys/class/rtc/rtc1/name", "val":"da9063-rtc"},
              {"cmd":"cat /sys/class/rtc/rtc1/hctosys", "val":"1"},
              {"cmd":"cat /sys/fsl_otp/HW_OCOTP_MAC0", "val":"0xd612bdec"},
              {"cmd":"cat /sys/fsl_otp/HW_OCOTP_MAC1", "val":"0x30"}]
else:
	# list for 4.x current mainline
	basiclist = [{"cmd":"cat /sys/bus/i2c/devices/0-0040/name", "val":"bu21029"},
              {"cmd":"cat /sys/class/thermal/thermal_zone0/temp", "val":"undef"},
              {"cmd":"cat /sys/bus/i2c/devices/i2c-4/name", "val":"i2c-1-mux (chan_id 0)"},
              {"cmd":"cat /sys/bus/i2c/devices/i2c-5/name", "val":"i2c-1-mux (chan_id 1)"},
              {"cmd":"cat /sys/bus/i2c/devices/4-0054/name", "val":"24c64"},
              {"cmd":"cat /sys/bus/i2c/devices/5-0050/name", "val":"24c1024"},
              {"cmd":"cat /sys/bus/i2c/devices/4-0058/name", "val":"da9063"},
              {"cmd":"cat /sys/class/leds/debug-green/trigger", "val":"[heartbeat]"},
              {"cmd":"cat /sys/class/leds/debug-yellow/trigger", "val":"[mmc1]"},
              {"cmd":"cat /sys/class/leds/system-fault/trigger", "val":"[cpu0]"},
              {"cmd":"find /sys -name dummy_phy16", "val":"/sys/firmware/devicetree/base/mdio/dummy_phy16"},
              {"cmd":"hexdump -C /sys/devices/soc0/mdio/mdio_bus/gpio-0/gpio-0\:10/of_node/phy_id", "val":"00 00 24 01"},
              {"cmd":"hexdump -C /sys/devices/soc0/soc/2100000.aips-bus/21bc000.ocotp/imx-ocotp0/nvmem", "val":"02 03 22 20 5f 72 64 df  d4 b1 17 01 5e 00 51 a6"},
              {"cmd":"cat /sys/class/rtc/rtc1/name", "val":"da9063-rtc"},
              {"cmd":"cat /sys/class/rtc/rtc1/hctosys", "val":"1"},
              {"cmd":"/media/mmcblk1p2/opt/a-sample-test/functional/GetBoardID.sh", "val":"PCBA HW version: 0.0.0"},
              {"cmd":"lsblk", "val":"/media/mmcblk1p2"},
              {"cmd":"hexdump -C /sys/bus/nvmem/devices/imx-ocotp0/nvmem", "val":"00000100  da ba da ba da ba da ba  da ba da ba da ba da ba"}]

for bl in basiclist:
    if bl["val"] == 'undef':
        tb.eof_write_cmd(tb.c_con, bl["cmd"])
    else:
        tb.eof_write_cmd_check(tb.c_con, bl["cmd"], bl["val"])

# Test spitest module
tb.config.tc_workfd_insmod_mpath = '/home/hs/fipad/modules/lib/modules'
tb.config.tc_workfd_insmod_module_path = 'kernel/drivers/char/bosch'
tb.config.tc_workfd_insmod_module = 'spitest'
tb.config.tc_workfd_insmod_module_checks = ['spitest spi0.0: gpio 26 reserved', 'spitest spi0.0: gpio 105 reserved', 'spitest spi0.0: gpio 27 reserved']
tb.eof_call_tc("tc_workfd_insmod.py")

# regulator tests
if lx_vers != '3':
    tb.statusprint("tc_fipad regulator checks")
    tb.eof_call_tc("tc_lx_regulator.py")

# check if flexcan driver works
tb.statusprint("tc_fipad can check")
tb.eof_call_tc("tc_workfd_can.py")

# iperf checks
tb.config.tc_workfd_iperf_minval = 90
tb.statusprint("tc_fipad iperf check")
tb.config.tc_workfd_iperf_sip = '192.168.20.97'
tb.config.tc_workfd_c_sr = tb.c_con
tb.config.tc_workfd_c_sl = tb.c_ctrl
tb.eof_call_tc("tc_workfd_iperf.py")

tb.config.tc_workfd_iperf_sip = '192.168.1.1'
tb.config.tc_workfd_c_sr = tb.c_ctrl
tb.config.tc_workfd_c_sl = tb.c_con
tb.eof_call_tc("tc_workfd_iperf.py")

# power off board at the end
#tb.eof_call_tc("tc_lab_poweroff.py")
tb.end_tc(True)
