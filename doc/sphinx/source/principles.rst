Principles
==========

Test case (TC):
---------------

  A piece of python code, which uses the tbot class.
  Tbot provides functions for sending shell commands and parsing the
  shell commands output.
  Tbot waits endless for a shell commands end (detected through reading
  the consoles prompt).
  A TC can also call other TC-es.
  
  remark:
  Tbot not really waits endless, for a shell commands end, instead
  tbot starts a watchdog in the background, and if it triggers, tbot
  ends the TC as failed. In the tbot beginning there was a lot of
  timeouts / retry cases, but it turned out, that waiting endless
  is robust and easy ...
   
Host PC
-------

where tbot runs, currently only linux host tested
must not be a powerful machine. For example, I run it on a raspberry Pi.

Lab PC:
-------

Host PC connects through ssh to the Lab PC, so it is possible to test boards, which are not at the same place as the Host PC.

(Lab PC and Host PC can be the same of course)

curently only Lab PC with an installed linux supported/tested.

Boards(s):
----------

the boards on which shell commands are executed.

Board state:
------------

equals to the software, the board is currently running.

Currently tbot supports 2 board states:

- "u-boot", if the board is running U-Boot
- "linux", if the board is running a linux kernel

A board state is detected through analysing the boards
shell prompt. In linux tbot sets a special tbot prompt,
in U-Boot the prompt is static, and configurable through a
board config file.

A TC can say in which board state it want to send shell commands.
Tbot tries to detect the current board state, if board is not in
the requested  board state, tbot tries to switch into the correct
state. If this fails, the TC fails.
It is possible to switch in a single TC between board states.

Virtual laboratory (VL)
-----------------------

VL is the basic environment that groups:

  - [a number of] boards - target devices on which tbot executes testcases.
  - one Lab PC
  - Basic tasks:
    - power on/off boards
    - read current power state of a board
    - connect to boards console

read more in doc/README.install how to integrate your own VL

Overview:

.. image:: image/tbot_structure.png


