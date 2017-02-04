=============
tbot overview
=============

Short description
=================

- execute testcases on real hw
- testcases written in python
- call testcases from another testcase
- Based on ideas from:
  http://www.denx.de/wiki/DUTS/DUTSDocs

Usage
=====

::

  $ tbot.py --help
  Usage: tbot.py [options]

  Options:
    -h, --help            show this help message and exit
    -c CFGFILE, --cfgfile=CFGFILE
                          the tbot board configfilename
    -s LABFILE, --slabfile=LABFILE
                          the tbot lab configfilename
    -l LOGFILE, --logfile=LOGFILE
                          the tbot logfilename, if default, tbot creates a
                          defaultnamelogfile
    -t TC, --testcase=TC  the testcase which should be run
    -v, --verbose         be verbose, print all read/write to stdout
    -w WORKDIR, --workdir=WORKDIR
                          set workdir, default os.getcwd()

Demo
====

click on the gif to see the full video on youtube

.. image:: image/demo.gif
https://youtu.be/zfjpj3DLsx4

demo video for a CAN bus testcase:

https://youtu.be/hl7gI4b9CG8

demo for a buildbot integration:

http://xeidos.ddns.net/buildbot/tgrid

Installation
============

install tbot on your PC (linux only tested):
--------------------------------------------

get the source code:
++++++++++++++++++++

::

  $ git clone https://github.com/hsdenx/tbot.git
  [...]
  $

cd into the tbot directory.

install paramiko
++++++++++++++++

you need the for running tbot the python paramiko module, see:

http://www.paramiko.org/installing.html

paramiko is used for handling ssh sessions, and open filedescriptors
on a ssh connection. Tbot open a ssh connection to a "lab PC" and
opens on that connection 2 filehandles, one for control functions
and one for the connection to the boards console. May it is worth
to think about to open more filehandles and use them in tbot, but
thats a point in the Todo list ...

See [1] for more infos about tbot principles.

create logfile directory
++++++++++++++++++++++++

prepare a directory for storing the logfiles
and pass it with the commandline option "-l"
to tbot. Default is the directory "log" in the tbot
root (don;t forget to create it, if you want to use it)

create VLAB
+++++++++++

If your VL is not yet in tbot source, integrate it
(This task has only to be done once for your VL):

prepare a lab config file for your lab:
.......................................

special case
::::::::::::

if you own a "Gembird Silver Shield PM power controller"
and use "kermit" for accessing the serial console:

*gratulation, you are finished with setting up virtual Lab!*

use:

https://github.com/hsdenx/tbot/blob/master/config/lab_home.py

and adapt the variables:

"ip", "user", "labsshprompt", "tc_workfd_work_dir",
"lab_tmp_dir" and "tftprootdir" for your needs.

setup in:

https://github.com/hsdenx/tbot/blob/master/src/tc/lab/tc_lab_sispmctl_get_variables.py

your special settings, where tbot finds through
"tb.config.boardlabpowername" the boards settings for the
"Gembird Silver Shield PM power controller"

go to step `prepare password file`_

setup tasks
:::::::::::

* create a new folder in src/tc/lab/XXX
  replace XXX to a proper value

  Each VL needs a configuration file, passed with the option '-s' to
  tbot, example:

  https://github.com/hsdenx/tbot/blob/master/config/lab_hs_home.py

  simple copy this and rename it to

  https://github.com/hsdenx/tbot/blob/master/config/lab_XXX.py

  and adapt the settings to your specific needs.

* Then you have to setup Testcases for the 3 VL tasks:

  + Task a) power on/off board:

    default TC for this task is:

    https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_denx_power.py

    now copy this file to for example

    ::

      cp src/tc/lab/denx/tc_lab_denx_power.py src/tc/lab/XXX/tc_lab_XXX_power_onoff.py

    and adapt the "remote_power" command from the denx lab to your needs.

    As this TC powers on the board for all your boards in your VL,
    you can differ between the boards through the tbot class
    variable

    ::

      tb.config.boardlabpowername

    (which is in the default case the same as "tb.config.boardname"),
    but you may need to name the power target
    with an other name than boardname, so you can configure this case.
    The power state "tb.power_state" which the TC has to set
    is "on" for power on, or "off" for power off.

    If switching on the power is successful, call "tb.end_tc(True)"
    else "tb.end_tc(False)"

    set in your lab config file:

    tc_lab_denx_power_tc = 'tc_lab_XXX_power_onoff.py'

  + Task b) get power state of a board:

    default TC for this task is:

    https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_denx_get_power_state.py

    now copy this file to for example
    (replace XXX to a proper value)

    ::

      cp src/tc/lab/denx/tc_lab_denx_get_power_state.py src/tc/lab/XXX/tc_lab_XXX_get_power_state.py

    and adapt the commands to your needs.

    If the power of the board is on, call "tb.end_tc(True)"
    else "tb.end_tc(False)"

    set in your lab config file:

    tc_lab_denx_get_power_state_tc = 'tc_lab_XXX_get_power_state.py'

  + Task c) connect to the boards console:

    default TC for this task is:

    https://github.com/hsdenx/tbot/blob/master/src/tc/lab/denx/tc_lab_denx_connect_to_board.py

    now copy this file to for example

    ::

      cp src/tc/lab/denx/tc_lab_denx_connect_to_board.py src/tc/lab/XXX/tc_lab_XXX_connect_to_board.py

    and adapt the commands to your needs.

    If connect fails end this TC with "tb.end_tc(False)"
    else call "tb.end_tc(True)"

    If you want to use kermit for connecting to the boards console, you
    can use:

    https://github.com/hsdenx/tbot/blob/master/src/tc/linux/tc_workfd_connect_with_kermit.py

    Example for such a board in the VL from denx:

    tc_lab_denx_connect_to_board_tc = 'tc_workfd_connect_with_kermit.py'

    https://github.com/hsdenx/tbot/blob/master/config/tbot_dxr2.cfg#L20

    set in your lab config file:

    tc_lab_denx_connect_to_board_tc = 'tc_lab_XXX_connect_to_board.py'

prepare password file
+++++++++++++++++++++

This file contains all passwords tbot needs (for example for
linux login on the boards)
tbot searches this file in the tbot root directory.
It is a simple python file, for example:

::

  # passwords for the lab
  if (board == 'lab'):
      if (user == 'hs'):
          password = 'passwordforuserhs'
      if (user == 'root'):
          password = 'passwordforrootuser'
  # passwords for the boards
  elif (board == 'mcx'):
      if (user == 'root'):
          password = 'passwordformcxrootfs'
  else:
      if (user == 'root'):
          password = ''

tbot searches in the root folder for this file.

prepare board config file
+++++++++++++++++++++++++

Each board which is found in the VL needs a tbot configuration file
pass the config file name with the option '-c' to tbot, tbot searches
in the "config" folder for them.

board Example (dxr2 board):
https://github.com/hsdenx/tbot/blob/master/config/dxr2.py

Now comes a list of variables TC needs, this vary from what you
you want to test...



Thats it ... you now can call tbot and hopefully, it works ;-)

If you have problems in settings up tbot, please contact me
(and may give me ssh access to your Lab PC ;-)

Heiko Schocher <hs@denx.de>
v2 2016.11.02
