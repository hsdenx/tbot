.. |Warning| image:: ./images/Warning-icon.png
   :height: 80
   :width: 80

.. |Help| image:: ./images/help.gif
   :height: 80
   :width: 80

.. |Tip| image:: ./images/tip.gif
   :height: 80
   :width: 80


Linux demo top output
#####################

Prerequiste
===========

login to DUTS_BOARDNAME and make traffic
and start :shellvar:`tbot_bbb_top.sh` in another shell

For this pdf I start :shellvar:`memtester` on the DUTS_BOARDNAME
to have some traffic ...

:shellvar:`tbot_bbb_top.sh` starts the tbot testcase, which
logs into the serial console on the board, and
starts the linux :shellvar:`top` command.

Analyses the output from it and writes the results in a file,
which :shellvar:`gnuplot` understands. Now gnuplot is started and creates
resulting images. This images are used for this short demo.

Results
=======

top cmdline settings:

count : DUTS_LINUX_TOP_COUNT

intervall in seconds: DUTS_LINUX_TOP_SEC

Memory usage
------------

.. image:: ../logfiles/top-mem-output.jpg

.. raw:: pdf

   PageBreak

CPU usage
---------

.. image:: ../logfiles/top-cpu-output.jpg

.. raw:: pdf

   PageBreak

Load average
------------

.. image:: ../logfiles/top-load-output.jpg

.. raw:: pdf

   PageBreak

links
=====

tbot_

.. _tbot: https://github.com/hsdenx/tbot
