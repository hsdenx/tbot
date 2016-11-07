##tbot

## Table of Contents
- [Short description](#description)
- [Usage](#usage)
- [Demo](#demo)
- [Principles](#principles)
- [Installation](#install)
- [Contributing](#contributing)
- [Building docs](#building-docs)
- [Author](#author)
- [License](#license)


## Short description

- execute testcases on real hw
- testcases written in python
- call testcases from another testcase
- Based on ideas from:
  http://www.denx.de/wiki/DUTS/DUTSDocs

## Usage

```
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
```

## Demo

click on the gif to see the full video on youtube

[![Demo tbot](https://github.com/hsdenx/tbot/blob/master/demo.gif)](https://youtu.be/zfjpj3DLsx4)

demo video for a CAN bus testcase:

https://youtu.be/hl7gI4b9CG8

demo for a buildbot integration:

http://xeidos.ddns.net/buildbot/tgrid


## Principles

- Test case (TC):
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
   
- Host PC (where tbot runs, currently only linux host tested)
  must not be a powerful machine.

- Lab PC: 
  - Host PC connects through ssh to the Lab PC
    -> so it is possible to test boards, which
       are not at the same place as the Host PC.
       (Lab PC and Host PC can be the same of course)
       -> maybe we can setup a Testsystem, which does nightly
          U-Boot/Linux builds and test current mainline U-Boot
          on boards all over the world ...

  - currently only Lab PC with an installed linux supported/tested.

- Boards(s):
  the boards on which shell commands are executed.

- Board state:
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

- Virtual laboratory (VL)
   VL is the basic environment that groups:
  - [a number of] boards - target devices on which tbot executes testcases.
  - one Lab PC
  - Basic tasks:
    - power on/off boards
    - read current power state of a board
    - connect to boards console

    read more in doc/README.install how to integrate your own VL

Overview:

![tbot_structure](https://github.com/hsdenx/tbot/blob/master/doc/tbot_structure.png)

- Events:

  tbot creates while executing testcases so called events.
  After tbot ended with the testcase it can call event_backends,
  which convert the events to different formats, see more

  doc/README.event

  demo for a event backend:

  http://xeidos.ddns.net/tests/test_db_auslesen.php

## Installation

Look for more infos into:
```
doc/README.install
```

## Contributing

You can submit your patches or post questions reagarding the project to the tbot Mailing List:

tbot@lists.denx.de

General information about the mailing list is at:

http://lists.denx.de/mailman/listinfo/tbot

When creating patches, please use something like:

git format-patch -s <revision range>

Please use 'git send- email' to send the generated patches to the ML to bypass changes from your mailer.

## Building docs


```sh
$ python2.7 doc/doc_tc.py
```
Dokumentation of Testcases:
https://cdn.rawgit.com/hsdenx/tbot/master/doc/doc_testcase.html

best view when opening it from local clone ...

## Author

**Heiko Schocher**
* Heiko Schocher <hs@denx.de>

## License
GPLv2
