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
# Sets a GPIO through sysfs gpio high/low
#
# Call like this:
# tb.eof_call_tc("tc_workfd_set_gpio.py", highlow='high', gpio=gpioname)
#
# End:

from tbotlib import tbot

c = tb.workfd
args = ['highlow', 'gpio']
arg = tb.check_args(args)
gpiotemp = arg.get('gpio')

logging.info("arg: %s %s %s", tb.workfd.name, gpiotemp, arg.get('highlow'))

try:
    gpiotemp.exported
except AttributeError:

    tb.config.tc_workfd_check_if_dir_exists_name = gpiotemp.path + 'gpio' + gpiotemp.number + '/'
    ret = tb.call_tc('tc_workfd_check_if_dir_exist.py')
    if (ret == False):
        tb.eof_write_cmd(c, 'echo ' + gpiotemp.number + ' > ' + gpiotemp.path + 'export')
        tb.eof_write_cmd(c,'echo out > ' + gpiotemp.path + 'gpio' + gpiotemp.number + '/direction')
    gpiotemp.exported = True


if arg.get('highlow') == 'high':
    tb.eof_write_cmd(c, 'echo 1 > ' + gpiotemp.path + 'gpio' + gpiotemp.number + '/value')

elif arg.get('highlow') == 'low':
    tb.eof_write_cmd(c, 'echo 0 > ' + gpiotemp.path + 'gpio' + gpiotemp.number + '/value')
else:
    logging.error("%s not supported.", arg.get('highlow'))
    tb.end_tc(False)

tb.end_tc(True)
