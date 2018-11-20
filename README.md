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


## New tbot

This is the old version of tbot, which is deprecated. Please
use the new version of tbot found on:

	https://github.com/Rahix/tbot

Documentation is available here:

	https://rahix.de/tbot

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
  -a ARGUMENTS, --arguments ARGUMENTS
                        arguments for the testcase
  -l LOGFILE, --logfile=LOGFILE
                        the tbot logfilename, if default, tbot creates a
                        defaultnamelogfile
  -t TC, --testcase=TC  the testcase which should be run
  -v, --verbose         be verbose, print all read/write to stdout
  -e EVENTSIM, --event EVENTSIM
                        open eventlogfile and run it
  -p PWFILE, --pwfile PWFILE
                        used password file
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

## Documentation

look for more documentation at:

http://www.tbot.tools/main.html

## Installation

http://www.tbot.tools/overview.html#installation

Guide for installing tbot with the BeagleBoneBlack

http://www.tbot.tools/guide.html

## Contributing

You can submit your patches or post questions reagarding the project to the tbot Mailing List:

tbot@lists.denx.de

General information about the mailing list is at:

http://lists.denx.de/listinfo/tbot

When creating patches, please use something like:

git format-patch -s <revision range>

Please use 'git send- email' to send the generated patches to the ML to bypass changes from your mailer.

## Building docs


```sh
$ python2.7 doc/doc_rst.py
```
Building html docs with sphinx:

see info about sphinx installation:
http://www.sphinx-doc.org/en/stable/install.html

```sh
$ make html
```

create html version:
```sh
$ cd doc/sphinx
$ make html
```
New Documentation now in doc/sphinx/build/html/main.html
```sh
$ firefox doc/sphinx/build/html/main.html
```

Documentation of Testcases:

http://www.tbot.tools/_static/doc_testcases.html

PDF version:

you need rst2pdf installed, for example with:
```sh
$ pip install rst2pdf
```

Then you can create a pdf version of the tbot documentation with:
```sh
$ cd doc/sphinx
$ sphinx-build -b pdf source build/pdf
```

PDF version of the documentation now in doc/sphinx/build/pdf/tbot_doc.pdf
```sh
$ okular doc/sphinx/build/pdf/tbot_doc.pdf
```

create man pages
```sh
$ cd doc/sphinx
$ sphinx-build -b man source build/man;man build/man/tbot.1
```

```sh
$ man doc/sphinx/build/man/tbot.1
```

## Author

**Heiko Schocher**
* Heiko Schocher <hs@denx.de>

## License
GPLv2
