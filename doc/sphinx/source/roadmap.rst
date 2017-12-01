==================
Project's road-map
==================

Here you will find "ideas" what can be done in tbot

tbot internal
=============

tbotlib suggestions
-------------------

Check if a TC ends with a prompt read

[simplify] create a "setup" script, which simplify setup after
tbot is installed. (Adapt all config variables for a new lab ...
Currently all defaultvalues are proper for the DENX lab)

[simplify] create testcases, specific for a specific SoC, so board
testcases can use them. For Example, create a tc_soc_imx6_xxx.py
testcases, which contains testcases we want to run on an imx based
board.

[simplify] make it possible to move virtual lab specific config options
into lab specific config files, and include them in board
config files

[simplify] make a documentation of "tbot conventions"
currently this are my personal conventions, if there are more
user try to identify my conventions and discuss and document them

currently they are hidden in default settings of tbot variables ...

[simplify] Get Vars for TC from U-Boot Code
started with, see TC:

- src/tc/tc_workfd_get_uboot_config_hex.py
- src/tc/tc_workfd_get_uboot_config_string.py

simplify tbot usage ... all ToDo points marked with [simplify]
goal: show tbot installation/usage on 2 pages ... (maybe 1 is possible ?)

- one for tbot installation and how to setup a virtual lab
- one for how to setup a board testcase

call testcases with arguments

move testcases into functions and use python decorators ...
I played with this approach, but I am not happy with it.

rework tbot completly into a more pythonic style

Event Backends
==============

Dokumentation Backend
---------------------

extract for each testcase the logs in files
Filename: testcasename_connectionname_index_incnumber.txt

- testcasename:   Name of TC
- connectionname: Name of the tbot connection
- index: counts, how often the TC was called, starts with 1
- incnumber: each switch to another connection increments this number starts with 1

Now you have all logs in a seperate file, you can
integrate into a documentation

Saying the format of your documentation ist a rst file

You can for example define a keyword "tbotref:filename"

Now writting a script which searches in your document file
for the above keword, and replaces it with the content
of filename in for example
http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#literal-blocks
format ...

and you can create a documentation with current logs.

kernel-ci backend
-----------------

simple convert the collected events into a format, so
we can integrate tbot into kernel-ci
