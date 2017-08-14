=================
Guide to use tbot
=================

This is a small guide of how to use tbot when starting from scratch.

When reading this section, you get a step by step introduction how to use tbot with a beagleboneblack and a
"Gembird Silver Shield PM power controller" and using kermit for accessing the serial console.

tbot installation
=================

Buy the following hw
--------------------

[1] Beagle Bone Black
    http://beagleboard.org/black

[2] Gembird Silver Shield PM power controller
    https://www.amazon.de/EG-PMS2-programmierbare-Steckdosenleiste-%C3%9Cberspannungsschutz-Schnittstelle/dp/B00BAQZJ4K/ref=sr_1_3?ie=UTF8&qid=1502686146&sr=8-3&keywords=SIS-PMS+Silvershield+Power+Manager

[3] USB2serial FTDI
    http://elinux.org/Beagleboard:BeagleBone_Black_Accessories#Serial_Debug_Cables

If you want to switch bootmodes, buy an USB relais

[4]

Remark: you do not need to use/buy this specific hw, for getting tbot running, but it is used in this example.

[5] Lap and Host PC
    Of course you need a PC with a linux installation.
    I use/used fedora 21, 22, 24, and 25, but all other distros should work too.

For this guide we use first the PC [5] as Host and LapPC.

Later, you can install tbot on another PC and use [5] as LapPC
only.

install paramiko on [5]
-----------------------

you need for running tbot the python paramiko module, see:

http://www.paramiko.org/installing.html

install gembird software
------------------------

http://sispmctl.sourceforge.net/


get the tbot source code:
-------------------------

::

  $ git clone https://github.com/hsdenx/tbot.git
  [...]
  $

cd into the tbot directory.

try ssh access to your LabPC
----------------------------

.. image:: image/guide/ssh_shell.png

copy some existing lab config to your new config
------------------------------------------------

::

  hs@localhost:tbot  [master] $ cp config/lab_hs_home.py config/lab_hs_laptop.py
  hs@localhost:tbot  [master] $

You can name your new lab config as you want, but I prefer to let it
begin with prefix `lab_`. In the following guide I use for the lab config
the name "lab_hs_laptop" ... please replace this with the name you
defined here!


Adapt the setting for accessing your labPC
------------------------------------------

.. image:: image/guide/guide_ssh.png

If you need a password for ssh to your PC than add it in
the password.py file

.. image:: image/guide/guide_ssh_password.png

If you need a public key, than add it in your password.py

.. image:: image/guide/guide_ssh_public_key.png

If you need to adapt the portnumber for ssh

.. image:: image/guide/guide_ssh_port.png

Adapt settings for Gembird Powercontroller
------------------------------------------

connect your USB cable from the Gembirs Powercontroller with an USB port on your PC.

check, if your laptop detected the Powercontroller, with dmesg output.

You should see something like that

::

  [ 2475.394934] usb 1-4: new low-speed USB device number 6 using xhci_hcd
  [ 2475.564195] usb 1-4: New USB device found, idVendor=04b4, idProduct=fd13
  [ 2475.564200] usb 1-4: New USB device strings: Mfr=1, Product=2, SerialNumber=0
  [ 2475.564202] usb 1-4: Product: Gembird Silver Shield PM
  [ 2475.564204] usb 1-4: Manufacturer: Gembird Electronics
  [ 2475.565613] usbhid 1-4:1.0: couldn't find an input interrupt endpoint
  hs@localhost:tbot  [master] $ 


Now, check if the "sispmctl" tool work with your Gembird Powercontroller.

Check version of sispmctl tool

.. image:: image/guide/guide_sispmctl_version.png

Scan for the Powercontroller

.. image:: image/guide/guide_sispmctl_scan.png

Now adapt the tbot settings for your needs:

.. image:: image/guide/guide_sispmctl_explanation.png

This is the setup for powering port 1 on/off of the Gembird controller.

If you need to use another port of the Gembird controller, change the
value in "tb.config.gembird_index" to the appropriate value.

Now it should be possible to switch on/off port 1 on the Gembird
Powercontroller with tbot.

If you can;t wait and want to test this now, we need to supress
tbot to connect to the boards console, as we did not have setup
it up yet:

So add in config/lab_hs_laptop.py the line

::

  do_connect_to_board = False

and start tbot:

.. image:: image/guide/guide_sispmctl_fasttest.png


Setup the console
-----------------

Now, we want to setup the console, so remove the line

::

  do_connect_to_board = False

in "config/lab_hs_laptop.py"

attach the USB2serial [3] cable to your USB port on [5]

check dmesg output:

::

  [ 7554.706870] usb 1-3: new full-speed USB device number 7 using xhci_hcd
  [ 7554.871691] usb 1-3: New USB device found, idVendor=067b, idProduct=2303
  [ 7554.871696] usb 1-3: New USB device strings: Mfr=1, Product=2, SerialNumber=0
  [ 7554.871698] usb 1-3: Product: USB-Serial Controller
  [ 7554.871700] usb 1-3: Manufacturer: Prolific Technology Inc.
  [ 7556.354720] usbcore: registered new interface driver pl2303
  [ 7556.354741] usbserial: USB Serial support registered for pl2303
  [ 7556.354763] pl2303 1-3:1.0: pl2303 converter detected
  [ 7556.355611] usb 1-3: pl2303 converter now attached to ttyUSB0
  hs@localhost:tbot  [master] $ 

In our case the USB cable is on /dev/ttyUSB0, so add this value in
"config/lab_hs_laptop.py"

.. image:: image/guide/guide_serial_setup_edit.png

Be sure you have installeed kermit and have the correct access rights
to access the serial port!

You can test this with:

.. image:: image/guide/guide_kermit_test.png

power on the beaglebone and you should see some output from the beagleboneblack.

Put in the powerplug from the beaglebone in the port 1 of your Gembird Powercontroller
(or the port you defined in step `Adapt settings for Gembird Powercontroller`_.

Try a first small U-Boot testcase. Simply set an U-Boots Environment variable.

.. image:: image/guide/guide_first_run.png

If you want to see, what tbot is doing, enable the verbose "-v" option from tbot.
See also hint `more readable verbose output`_.

Also you can look into the logfile log/tbot.log (filename passed with tbots option "-l")

If you get "set board state failure end" message

.. image:: image/guide/guide_first_run_failure.png

May you have a Beagleboneblack board with a very old U-Boot.

U-Boots prompt changes once from "U-Boot# " to "=> ".

The default value is the new "=> " one ... so, edit the board config
"config/beagleboneblack.py" as follow:

.. image:: image/guide/guide_first_run_fix_prompt.png


Now you can start with writting testcases for the beagleboneblack board,
see `tbot write a testcase`_.

tbot install statistic backend
------------------------------

install gnuplot on your labPC [5]. Installation see

http://www.gnuplot.info/

Used version in for this guide:

.. image:: image/guide/guide_backend_statistic_gnuplotversion.png

Enable the statistic backend in tbot

.. image:: image/guide/guide_backend_statistic_enable.png

run tbot and after tbot finsihed you got in tbot source dir the file
"stat.dat". Simply call now gnuplot:

::

  hs@localhost:tbot  [master] $ gnuplot src/files/balkenplot.sem
  hs@localhost:tbot  [master] $

and find the output.jpg in tbot source dir.

tbot install dot backend
------------------------

install dot on your labPC [5]. Installation see

http://www.graphviz.org/Download..php

Used version in for this guide:

.. image:: image/guide/guide_backend_dot_version.png

Enable the dot backend in tbot

.. image:: image/guide/guide_backend_dot_enable.png

Simply run now tbot and after tbot finshed you see the file
"tc.dot" in tbot source directory.

Create a png Image with

::

   $ dot -Tpng tc.dot > tc.png

or a ps file with

::

  $ dot -Tps tc.dot > tc.ps




ToDo:

- guide for setting up event backends

  - dashboard
  - nice log
  - documentation

- guide for using demo1 testcase

  https://github.com/hsdenx/tbot/blob/master/src/tc/demo/tc_demo_part1.py

tbot write a testcase
=====================

ToDo

- copy a already existing one
- modify it for your needs

tbot function name glossar
--------------------------

eof_= exit on failure

end tbot when the function ends False. So you save
a lot of

::

  if ret = False:
      tb.end_tc(False)

constructs
              
rup_= read until prompt

This functions reads until prompt. You do not need to
wait for a prompt after this function finished.

tbot Tips/Tricks/Hints
======================

more readable verbose output
----------------------------

tbot prints as fast the incoming characters in verbose mode as possible.

This leads in more or less unreadable verbose output, if you want to
follow what tbot does ... So add the following patch:

::

  hs@localhost:tbot  [master] $ git diff
  diff --git a/src/common/tbot_connection_paramiko.py b/src/common/tbot_connection_paramiko.py
  index b5bdd33..423d8f6 100644
  --- a/src/common/tbot_connection_paramiko.py
  +++ b/src/common/tbot_connection_paramiko.py
  @@ -7,6 +7,7 @@ import logging
   import paramiko
   import socket
   import traceback
  +from time import sleep
   
   class Connection(object):
     """ The connection class
  @@ -83,6 +84,7 @@ class Connection(object):
           """ get bytes from connection
           """
           try:
  +            sleep(0.2)
               tmp = self.channel.recv(self.maxread)
           except socket.timeout:
               logging.debug("read_bytes: Timeout")
  hs@localhost:tbot  [master] $

!! This slows down tbot !! Do not use it in "normal" test environment.


