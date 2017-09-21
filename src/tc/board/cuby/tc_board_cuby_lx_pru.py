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
# tbot.py -s lab_denx -c cuby -t tc_board_cuby_lx_pru.py
# test linux pruss
# End:

import time
from tbotlib import tbot

tb.set_board_state("linux")
c = tb.c_con
tb.workfd = c

tmp = 'cd /home/root/check-setup'
tb.write_lx_cmd_check(c, tmp)

tmp = 'ls -al'
tb.write_lx_cmd_check(c, tmp)

tmp = './check_setup'
tb.eof_write(c, tmp, start=False)

err_list = [
	'FAIL'
]
tb.tbot_rup_error_on_strings(c, err_list, endtc=True)

"""
in /home/root/check_setup
script fuer pruss test ausfuehren

root@cuby [ 8:27:02] ttbott> ./check_setup 
Looking for kernel module 'uio_pruss'   --> [ \033[0;32mOK\033[0m ]
Checking GPIOs in sysfs   --> [ \033[0;32mOK\033[0m ]
Exporting GPIO 100   --> [ \033[0;32mOK\033[0m ]
Switching GPIO 100 to output mode   --> [ \033[0;32mOK\033[0m ]
Setting GPIO 100 to HIGH which enables shift registers 2 - 4   --> [ \033[0;32mOK\033[0m ]
Starting unit test ...
********* Start testing of TestMkcPruDriver *********
Config: Using QtTest library 5.7.0, Qt 5.7.0 (arm-little_endian-ilp32-eabi-hardfloat shared (dynamic) release build; by GCC 6.2.0)
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Initializing PRU interface ...
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Opened PRU Subsystem Driver. Hardware version: AM33XX
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Shared memory created at QSharedPointer(0x1ccd848)
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Creating interrupt handler instance
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Establishing digital inputs
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Input 4 alias "MF4-FLT" ( "FaultFingerMotor4" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Input 5 alias "MF3-FLT" ( "FaultFingerMotor3" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Input 6 alias "MF2-FLT" ( "FaultFingerMotor2" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Input 7 alias "MF1-FLT" ( "FaultFingerMotor1" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Input 8 alias "001B14" ( "PositionSensorFinger1" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Input 14 alias "001B15" ( "PositionSensorFinger2" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Input 12 alias "001B16" ( "PositionSensorFinger3" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Input 10 alias "001B13" ( "PositionSensorFinger4" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Input 9 alias "001BE52" ( "RackEmptyRight" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Input 13 alias "001BE51" ( "RackEmptyLeft" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Input 16 alias "001B12" ( "LhdCenterRight" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Input 21 alias "001B11" ( "LhdCenterLeft" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Input 22 alias "001B21" ( "LhdCenterDirection" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Establishing digital outputs
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Digital output 0 alias "P24V" ( "Power24V" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Digital output 3 alias "MOT-X-24V" ( "MotorX_24V" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Digital output 4 alias "MOT-Z-24V" ( "MotorZ_24V" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Digital output 20 alias "MF4-DIR" ( "DirectionFingerMotor4" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Digital output 18 alias "MF3-DIR" ( "DirectionFingerMotor3" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Digital output 16 alias "MF2-DIR" ( "DirectionFingerMotor2" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Digital output 22 alias "MF1-DIR" ( "DirectionFingerMotor1" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Establishing PWM outputs
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: PWM output 21 alias "MF4-ON" ( "PowerFingerMotor4" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: PWM output 19 alias "MF3-ON" ( "PowerFingerMotor3" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: PWM output 17 alias "MF2-ON" ( "PowerFingerMotor2" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: PWM output 23 alias "MF1-ON" ( "PowerFingerMotor1" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Digital output 14 alias "LED_G" ( "GreenLED" ) created
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: PRU Firmware downloaded and launched
QDEBUG : TestMkcPruDriver::initTestCase() MkcPruDriver: Interrupt handler started
QDEBUG : TestMkcPruDriver::initTestCase() "MF1-FLT" :  High
PASS   : TestMkcPruDriver::initTestCase()
PASS   : TestMkcPruDriver::testAvailableInputs()
PASS   : TestMkcPruDriver::testAvailableOutputs()
PASS   : TestMkcPruDriver::testAvailablePwms()
PASS   : TestMkcPruDriver::testPruRunning()
PASS   : TestMkcPruDriver::testInputEnable()
PASS   : TestMkcPruDriver::testInputDisable()
QDEBUG : TestMkcPruDriver::testOutputEnable() "MF4-FLT" :  Low
QDEBUG : TestMkcPruDriver::testOutputEnable() "MF3-FLT" :  Low
QDEBUG : TestMkcPruDriver::testOutputEnable() "MF2-FLT" :  Low
QDEBUG : TestMkcPruDriver::testOutputEnable() "MF1-FLT" :  Low
PASS   : TestMkcPruDriver::testOutputEnable()
PASS   : TestMkcPruDriver::testOutputDisable()
PASS   : TestMkcPruDriver::testPwmEnable()
PASS   : TestMkcPruDriver::testPwmDisable()
QDEBUG : TestMkcPruDriver::test24vOn() "MF3-FLT" :  High
QDEBUG : TestMkcPruDriver::test24vOn() "MF1-FLT" :  High
QDEBUG : TestMkcPruDriver::test24vOn() "MF4-FLT" :  High
QDEBUG : TestMkcPruDriver::test24vOn() "MF4-FLT" :  Low
QDEBUG : TestMkcPruDriver::test24vOn() "MF3-FLT" :  Low
QDEBUG : TestMkcPruDriver::test24vOn() "MF1-FLT" :  Low
QDEBUG : TestMkcPruDriver::test24vOn() "MF4-FLT" :  High
QDEBUG : TestMkcPruDriver::test24vOn() "MF3-FLT" :  High
QDEBUG : TestMkcPruDriver::test24vOn() "MF2-FLT" :  High
QDEBUG : TestMkcPruDriver::test24vOn() "MF1-FLT" :  High
PASS   : TestMkcPruDriver::test24vOn()
PASS   : TestMkcPruDriver::testOutputInputFeedback()
FAIL!  : TestMkcPruDriver::test24vOff() 'm_in_24v_on->isLow()' returned FALSE. ()
   Loc: [/home/cuby/CubyDevel/CUBYRAD-398/cuby_shuttle_control_software/mkc_pru_driver/source/unit_tests/test_pru_driver.cpp(366)]
QDEBUG : TestMkcPruDriver::cleanupTestCase() MkcPruDriver: Interrupt handler terminating
QDEBUG : TestMkcPruDriver::cleanupTestCase() MkcPruDriver: Interrupt handler stopped
PASS   : TestMkcPruDriver::cleanupTestCase()
Totals: 14 passed, 1 failed, 0 skipped, 0 blacklisted, 3474ms
********* Finished testing of TestMkcPruDriver *********
Unit test failed   --> [ \033[0;31mFAILED\033[0m ]

\033[0;31mTest completed with errors!\033[0m
root@cuby [ 8:27:08] ttbott> 
"""


tb.end_tc(True)
