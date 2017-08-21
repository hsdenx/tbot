======
Events
======

  tbot creates while executing testcases so called events.
  After tbot ended with the testcase it can call event_backends,
  which convert the events to different formats.

  There are standard Events which tbot create automatically, for
  example the Event "Start" is created when tbot starts a new
  Testcase.

  It is also possible to create Testcases specific Events. Therefore
  a Testcase only has to call the function **create_event()**
  
Eventlist
=========

current created standard Events
-------------------------------

===============  ============================
  Event-ID           content
===============  ============================
log              log content
Boardname        Name of board
BoardnameEnd     End of tests for Boardname
Start            Start of TC
StartFkt         Start of TC function
End              End of TC
===============  ============================

Testcases specific Events
-------------------------

  tc_lab_set_toolchain.py_
.. _tc_lab_set_toolchain.py: https://github.com/hsdenx/tbot/blob/testing/src/tc/tc_lab_set_toolchain.py

===============  ============================
  Event-ID           content
===============  ============================
Toolchain        used Toolchain
===============  ============================

  tc_workfd_apply_patchwork_patches.py_
.. _tc_workfd_apply_patchwork_patches.py: https://github.com/hsdenx/tbot/blob/testing/src/tc/linux/tc_workfd_apply_patchwork_patches.py

===============  ============================
  Event-ID           content
===============  ============================
PW_NR            current patchwork patchnumber
PW_CLEAN         current patchworknumber patch is clean or not
PW_AA            current patchworknumber patch is already applied
PW_APPLY         current patchworknumber patch is applies clean or not
===============  ============================

  tc_lab_compile_uboot.py_
.. _tc_lab_compile_uboot.py: https://github.com/hsdenx/tbot/blob/testing/src/tc/tc_lab_compile_uboot.py

===============  ============================
  Event-ID           content
===============  ============================
UBOOT_DEFCONFIG  used U-Boot configuration
UBOOT_SRC_PATH   path, where U-boot source is located
===============  ============================

  tc_ub_test_py.py_
.. _tc_ub_test_py.py: https://github.com/hsdenx/tbot/blob/testing/src/tc/uboot/tc_ub_test_py.py

===============  ============================
  Event-ID           content
===============  ============================
UBOOT_TEST_PY    path to test py result
===============  ============================

  tc_ub_get_version.py_
.. _tc_ub_get_version.py: https://github.com/hsdenx/tbot/blob/testing/src/tc/uboot/tc_ub_get_version.py

===============  ============================
  Event-ID           content
===============  ============================
UBOOT_VERSION    U-Boot/SPL version
===============  ============================

  tc_lx_get_version.py_
.. _tc_lx_get_version.py: https://github.com/hsdenx/tbot/blob/testing/src/tc/linux/tc_lx_get_version.py

===============  ============================
  Event-ID           content
===============  ============================
LINUX_VERSION	 Linux version
===============  ============================

  tc_workfd_compile_linux.py_
.. _tc_workfd_compile_linux.py: https://github.com/hsdenx/tbot/blob/testing/src/tc/linux/tc_workfd_compile_linux.py

===============  ============================
  Event-ID           content
===============  ============================
LINUX_DEFCONFIG  used Linux configuration
LINUX_SRC_PATH   path, where Linux source is located
===============  ============================

  documentation.py_
.. _documentation.py: https://github.com/hsdenx/tbot/src/common/event/documentation.py

================  ============================
  Event-ID           content
================  ============================
SET_DOC_FILENAME  set a name for the logfile
================  ============================

==================  ============================
  Event-ID           content
==================  ============================
DUTS_UBOOT_VERSION  U-Boot version 'undef' if not found
DUTS_SPL_VERSION    SPL version, 'undef' if not found
DUTS_BOARDNAME      tb.config.boardlabpowername

When activating the documentation backend, this values
are saved in the file: self.tb.workdir + '/logfiles/duts_settings.txt'

You can later use them to make your document board independent.

  tc_ub_duts_version.py_
.. _tc_workfd_compile_linux.py: https://github.com/hsdenx/tbot/blob/master/src/tc/uboot/duts/tc_ub_duts_version.py

demos
=====

dashboard
---------

  dashboard_source_
.. _dashboard_source: https://github.com/hsdenx/tbot/blob/testing/src/common/event/dashboard.py

  pick some Events and put the content into a MYSQL database.
  Now the DB content can be readen with a simple php script
  to create a webpage, see for a minimal example:


  http://xeidos.ddns.net/tests/test_db_auslesen.php

statistic
---------

  statistic_source_
.. _statistic_source: https://github.com/hsdenx/tbot/blob/testing/src/common/event/statisitic_plot.py

  use gnuplot for creating a statistic image of called testcases.

  http://xeidos.ddns.net/tbot/id_189/statistic.jpg

dot
---

  dot_source_
.. _dot_source: https://github.com/hsdenx/tbot/blob/testing/src/common/event/dot.py

Use the Eventinformation for creating nice DOT graphics from the test.
see a raw example:

  Demo Output of a git bisect Demotestcase_
.. _Demotestcase: https://github.com/hsdenx/tbot/blob/testing/src/tc/demo/tc_demo_part3.py

  http://xeidos.ddns.net/tbot/id_171/graph.png


planned Event backends:
=======================

DUTS:

  make from the logs tbot collected, DUTS specific textfiles, so the logs
  can integrated into the DULG

xunit:

  create xunit files for presenting the results in jenkins

kernel CI:

  adapt to a format, so the testresults can be presented at kernel CI
  (just an idea...)
