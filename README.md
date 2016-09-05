##tbot

- execute testcases on real hw
- write testcases in python
- call testcases from another testcase
- create logfile
- Based on ideas from:

  http://www.denx.de/wiki/DUTS/DUTSDocs

  but used python instead of expect

## Demo

[![Demo tbot](https://github.com/hsdenx/tbot/blob/master/demo.gif)](https://www.youtube.com/watch?v=ZwUA0QNDnP4)

-------------------------------------------------

Submitting patches

You can submit your patches or post questions reagarding the project to the tbot Mailing List:

tbot-devel@googlegroups.com

When creating patches, please use something like:

git format-patch -s <revision range>

Please use 'git send- email' to send the generated patches to the ML to bypass changes from your mailer.

-------------------------------------------------

Why python?
- python has a lot of string manipulation possibility
- easy to use
- a lot of python modules (for example paramiko
  is used for ssh access)
- you can easily integrate tbot into buildbot
  http://buildbot.net/
  You can build your images with buildbot and test
  them on real hw with tbot. Results and the log
  file also accessible in buildbot

  demo for a usecase with buildbot:

  http://xeidos.ddns.net/buildbot/tgrid

-------------------------------------------------

Basic ideas:

- Virtual laboratory (VL)
   VL is the basic environment that groups:
  - [a number of] boards - target devices on which tbot executes testcases.
  - one Lab PC

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
  is robust and easy ... ToDo: clean up tbot code ...
   
- Host PC (where tbot runs, currently only linux host tested)
  must not a powerful machine.

- Lab PC: 
  - Host PC connects through ssh to the Lab PC
    -> so it is possible to test boards, which
       are not at the same place as the Host PC.
       (Lab PC and Host PC can be the same of course)
       -> maybe we can setup a Testsystem, which does nightly
          U-Boot/Linux builds and test current mainline U-Boot
          on boards all over the world ...

  - necessary tasks a Lab PC must deliver:
    - connect to boards console through a shell command.
    - power on/off boards through a shell command
    - detect the current power state of a board through
      a shell command

  - optional tasks:
    - tftp server (for example loading images)
    - nfs server (used as rootfs for linux kernels)
    - Internet access for example for downloading
      U-Boot source with git.
    - toolchains installed for compiling source code

      -> a linux machine is preffered.

  - currently only Lab PC with an installed linux supported/tested.

- Boards(s):
  the boards on which shell commands are executed.

- Board state:
  equals to the software, the board is currently running.

  Currently tbot supports 2 board states:
    - "u-boot", if the board is running U-Boot
    - "linux", if the board is running a linux kernel

  It should be easy to add other board states to tbot, see
  https://github.com/hsdenx/tbot/tree/master/src/lab_api

  A board state is detected through analysing the boards
  shell prompt. In linux tbot sets a special tbot prompt,
  in U-Boot the prompt is static, and configurable through a
  board config file.

  A TC can say in which board state it want to send shell commands.
  Tbot tries to detect the current board state, if board is not in
  the requested  board state, tbot tries to switch into the correct
  state. If this fails, the TC fails.
  It is possible to switch in a single TC between board states.

- Events:

  tbot creates while executing testcases so called events.
  After tbot ended with the testcase it can call event_backends,
  which convert the events to different formats, see more

  doc/README.event

  demo for a event backend:

  http://xeidos.ddns.net/tests/test_db_auslesen.php

Look for more infos into:
```
doc/README.install
```

Dream:

Setup somewhere a tbot host, which has access to
labs with boards and do automated nightly builds
and test the images on real hw.

http://xeidos.ddns.net/buildbot/waterfall

Also find out automated, which commit is the cause,
when a testcase failed ... currently I think, not
far away, except missing more labs and boards ...

![tbot_structure](https://github.com/hsdenx/tbot/blob/master/doc/tbot_structure.png)

-------------------------------------------------

Dokumentation of Testcases:
https://github.com/hsdenx/tbot/blob/master/doc/doc_testcase.html

try to open it with:

http://htmlpreview.github.io/?https://github.com/hsdenx/tbot/blob/master/doc/doc_testcase.html

best view when opening it from local clone ...

created with
```
python2.7 doc/doc_tc.py
```

-------------------------------------------------

Theory of operation
steps executed when calling a testcase:

- connect to lab
  - a lab must be defined in src/lab_api/lab_name.py
  - the lab which the board uses, is included in the
    board.cfg file
  - a connection must have the possibility to
    have more than one channel/filedescriptor
    because we use one for sending/reading strings
    to the board, another for control functions like
    powering on/off

- power the board
  - power on/off the board
  - get the current power state
  - in src/lab_api/lab_name.py

- we define in tbot board states. For each testcase
  must be defined, for which board state it is valid.
  You cannot run for example a linux tc under u-boot
  tbot switches the board into the state when starting
  a testcase. Board states are defined in src/lap_api

  dependent on state (set in testcase through "tb.set_board_state("linux")")
  - debugger: connect to debugger
    - ToDo

  - u-boot: src/lab_api/state_uboot.py
    - connect to serial
    - try to get U-Boot prompt

      if not, reset board, wait for U-Boot prompt

      if not tc fail

  - linux: src/lab_api/state_linux.py
    - connect to serial
    - try to get linux tbot prompt

      if not, boot linux with using testcase:

         src/tc/tc_ub_boot_linux.py

         then get linux prompt, and set tbot linux prompt

         if not tc fail

after this steps, we are ready to execute the testcase.

This sounds complicated, but in the testcase there are
only 2 lines necessary for setting this up:

```
1 # start with
2 # python2.7 src/common/tbot.py -c tbot.cfg -t tc_setenv.py
3 from tbotlib import tbot
4 
5 #here starts the real test
6 logging.info("u-boot setenv testcase arg: %s %s", tb.setenv_name, tb.setenv_value)
7 #set board state for which the tc is valid
8 tb.set_board_state("u-boot")
```

```
line 3: include tbot
line 8: set the state for which the tc is valid
        (you can switch in a testcase between board states)

line 6 is optional, it adds a line in the log file, here it
       prints the arguments for the testcase
```

-------------------------------------------------------------------------

every board needs a board config file. It contains
the board specific setting (which lab api to use, boardname,
lab specific settings username/password, ...)

-------------------------------------------------------------------------

As we have usernames and passwords, they are not included
in the source code. tbot loads them from the tbot work
directory through the password.py file (denx.api specific)
Maybe we can get rid of this...

This is a simple text file with python code:

```
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
```

-------------------------------------------------------------------------
Known problems / ToDo:

- end of line detection

  As the end of a line is \n, and tbot checks end of line with
  \n this maybe leads into errors, if the COLUMNS of the linux
  terminal is not long enough, and insert a \n ...

  `echo $COLUMNS` must show a value, which can hold the longest
  command tbot send ...

  I currently set:
```
stty cols 155
export TERM=vt200
```
which I think is not the best way to do it ...
Suggestions welcome

- rework file handle

  currently 2 filehandles are open, one for the lab
  and one for the serial console. This is fix in the
  code, maybe its better to use an array of file handles.

  Also, no file handle is used in testcases ... maybe this
  was a bad decision ...

  started introducing this. Testcases, which are not only
  for lx over the console fd converted to using tb.workfd.
  
  Problem is, we cannot pass variables to tc ... so we must
  use tb.workfd ... which maybe has problems when a tc call
  anther tc and this second tc changes the tb.workfd ...
  Maybe we must save it in call_tc and restore it in end_tc

- rename functionnames

  rename functionnames in tbotlib to more meaningful names
  Oh, yes ... and maybe extract more tbotlib functions
  into testcases.

-------------------------------------------------------------------------

Here an example of tbot execution:

testcase for mounting/writing in linux into a partition
steps executed:
- mount partition (for this call testcase tc_lx_mount.py)
- create dummy file
- write it to the partition
- umount partition
- mount it again
- compare dummy file with the file copied
  to the partition

```
testcase tc_lx_partition_check.py:
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
# start with
# python2.7 src/common/tbot.py -c tbot.cfg -t tc_lx_partition_check.py
# cp a dummy file into a partiton umount/mount it and
# diff it
from tbotlib import tbot

#set board state for which the tc is valid
tb.set_board_state("linux")

#call tc mount partition
tb.eof_call_tc("tc_lx_mount.py")

#create tempfile
tb.tc_lx_dummy_file_bs = "1024"
tb.tc_lx_dummy_file_count = "1024"
tb.tc_lx_dummy_file_tempfile = "/tmp/gnlmpf_partition"
ret = tb.eof_call_tc("tc_lx_create_dummy_file.py")

#copy dummy file into partition
tmp = "cp " + tb.tc_lx_dummy_file_tempfile + " " + tb.tc_lx_mount_dir
tb.eof_write_con(tmp)
tb.eof_wait_prompt(5)

#umount the partition
tmp = "umount " + tb.tc_lx_mount_dev
tb.eof_write_con(tmp)
tb.eof_wait_prompt(5)

#mount it again
tb.eof_call_tc("tc_lx_mount.py")

#compare the dummy file with the file in the partition
tmp = "cmp " + tb.tc_lx_dummy_file_tempfile + " " + tb.tc_lx_mount_dir + "/gnlmpf_partition"
tb.eof_write_con(tmp)
ret = tb.search_str_in_readline_con("diff")
if ret == True:
    tb.end_tc(False)

tb.eof_read_end_state_con(2)
tb.end_tc(True)
```

--------------

board configuration file (shc board): tbot_shc.cfg

```
#tbot configuration
# for testing dfu with zug boards and dfu-util on ts8
self.boardname = 'shc'
self.powerboardname = 'g2c1' #we have another name as the boardname for powering on/off
self.labprompt='ttbott' #prompt the lab (running linux there) gets
self.debug=False #no debug output
self.debugstatus=True # print debug status output
self.ip='pollux.denx.org' # how to reach the denx lab
self.user='hs'
self.accept_all=True
self.keepalivetimeout=1
self.channel_timeout=0.5
self.loglevel='INFO' #debug logging level

self.uboot_prompt = 'U-Boot#'
self.linux_prompt = 'ttbott#'

#testcases
self.setenv_name = 'Heiko'
self.setenv_value = 'Schocher'
self.ub_load_board_env_addr = '0x81000000'
self.ub_load_board_env_subdir = '20150814-stable'
```
--------------

commandline for starting this testcase:

```
hs@localhost:tbot  [master] $ python2.7 src/common/tbot.py -c tbot_shc.cfg -l shc-20150925.log -t tc_lx_partition_check.py
**** option cfg: tbot_shc.cfg log: shc-20150925.log tc: tc_lx_partition_check.py v 0
('CUR WORK PATH: ', '/home/hs/data/Entwicklung/tbot')
('CFGFILE ', 'tbot_shc.cfg')
('LOGFILE ', '/home/hs/data/Entwicklung/tbot/shc-20150925.log')
End of TBOT: success
hs@localhost:tbot  [master] $ 
```
--------------

logfile tbot created:

```
2015-09-26 04:53:46,554:INFO   :tbotlib   # *****************************************
2015-09-26 04:53:46,554:INFO   :tbotlib   # Started logging @  2015-09-26 04:53
2015-09-26 04:53:46,554:INFO   :tbotlib   # working directory /home/hs/data/Entwicklung/tbot
2015-09-26 04:53:46,555:INFO   :tbotlib   # testcase directory /home/hs/data/Entwicklung/tbot/src/tc
2015-09-26 04:53:46,555:INFO   :denx      # setup with denx API
2015-09-26 04:53:47,074:INFO   :transport # Connected (version 2.0, client OpenSSH_6.6.1)
2015-09-26 04:53:47,462:INFO   :transport # Authentication (publickey) failed.
2015-09-26 04:53:47,559:INFO   :transport # Authentication (password) successful!
2015-09-26 04:53:47,879:INFO   :denx      # got connection for hs@pollux.denx.org
2015-09-26 04:53:47,879:INFO   :tbotlib   # read 0: Last login: Sat Sep 26 04:53:03 2015 from 87.97.2.150.pool.invitel.hu
2015-09-26 04:53:47,879:INFO   :tbotlib   # read 0: 
2015-09-26 04:53:47,879:INFO   :tbotlib   # read 0: *************************************************************
2015-09-26 04:53:47,879:INFO   :tbotlib   # read 0: BDI2000 Assignment:    (last updated:  2015-05-13 10:05 MEST)
2015-09-26 04:53:47,879:INFO   :tbotlib   # read 0: bdi1  => techem     bdi2  => cetec_mx25   bdi3  => lpc3250
2015-09-26 04:53:47,880:INFO   :tbotlib   # read 0: bdi4  => -          bdi5  => --Rev.B!--   bdi6  => stka6x
2015-09-26 04:53:47,880:INFO   :tbotlib   # read 0: bdi7  => [stefano]  bdi8  => g45          bdi9  => rut
2015-09-26 04:53:47,880:INFO   :tbotlib   # read 0: bdi10 => pcm052     bdi11 => socrates     bdi12 => aristainetos
2015-09-26 04:53:47,880:INFO   :tbotlib   # read 0: bdi13 => imx53      bdi14 => ib8315       bdi15 => cairo
2015-09-26 04:53:47,880:INFO   :tbotlib   # read 0: bdi16 => g2c1       bdi17 => titanium     bdi18 => symphony
2015-09-26 04:53:47,880:INFO   :tbotlib   # read 0: bdi19 => dxr2       bdi20 => ima3-mx6     bdi21 => sama5d3
2015-09-26 04:53:47,880:INFO   :tbotlib   # read 0: bdi98 => -          bdi99 => -            bdi0  => -
2015-09-26 04:53:47,880:INFO   :tbotlib   # read 0: Please power off unused systems when you leave!   Thanks, wd.
2015-09-26 04:53:47,880:INFO   :tbotlib   # read 0: *************************************************************
2015-09-26 04:53:48,881:INFO   :tbotlib   # read no ret 0 
pollux:~ hs[0;32m [0m$ 
2015-09-26 04:53:48,881:INFO   :tbotlib   # write 0: export PS1="\u@\h [\$(date +%k:%M:%S)] ttbott >"
2015-09-26 04:53:48,977:INFO   :tbotlib   # read 0: export PS1="\u@\h [\$(date +%k:%M:%S)] ttbott >"
2015-09-26 04:53:48,978:INFO   :tbotlib   # read 0: hs@pollux [ 4:53:48] ttbott >
2015-09-26 04:53:48,979:INFO   :tbotlib   # set prompt:export PS1="\u@\h [\$(date +%k:%M:%S)] ttbott >"
2015-09-26 04:53:48,979:INFO   :denx      # get power state g2c1
2015-09-26 04:53:48,979:INFO   :tbotlib   # write 0: remote_power g2c1 -l
2015-09-26 04:53:49,075:INFO   :tbotlib   # read 0: hs@pollux [ 4:53:48] ttbott >remote_power g2c1 -l
2015-09-26 04:53:49,107:INFO   :tbotlib   # read 0: g2c1        	ON
2015-09-26 04:53:49,107:INFO   :tbotlib   # read 0: hs@pollux [ 4:53:49] ttbott >
2015-09-26 04:53:49,108:INFO   :tbotlib   # write 1: connect shc
2015-09-26 04:53:49,108:INFO   :tbotlib   # read 1: Last login: Sat Sep 26 04:53:47 2015 from 87.97.2.150.pool.invitel.hu
2015-09-26 04:53:49,108:INFO   :tbotlib   # read 1: 
2015-09-26 04:53:49,109:INFO   :tbotlib   # read 1: *************************************************************
2015-09-26 04:53:49,109:INFO   :tbotlib   # read 1: BDI2000 Assignment:    (last updated:  2015-05-13 10:05 MEST)
2015-09-26 04:53:49,109:INFO   :tbotlib   # read 1: bdi1  => techem     bdi2  => cetec_mx25   bdi3  => lpc3250
2015-09-26 04:53:49,109:INFO   :tbotlib   # read 1: bdi4  => -          bdi5  => --Rev.B!--   bdi6  => stka6x
2015-09-26 04:53:49,109:INFO   :tbotlib   # read 1: bdi7  => [stefano]  bdi8  => g45          bdi9  => rut
2015-09-26 04:53:49,109:INFO   :tbotlib   # read 1: bdi10 => pcm052     bdi11 => socrates     bdi12 => aristainetos
2015-09-26 04:53:49,109:INFO   :tbotlib   # read 1: bdi13 => imx53      bdi14 => ib8315       bdi15 => cairo
2015-09-26 04:53:49,109:INFO   :tbotlib   # read 1: bdi16 => g2c1       bdi17 => titanium     bdi18 => symphony
2015-09-26 04:53:49,109:INFO   :tbotlib   # read 1: bdi19 => dxr2       bdi20 => ima3-mx6     bdi21 => sama5d3
2015-09-26 04:53:49,110:INFO   :tbotlib   # read 1: bdi98 => -          bdi99 => -            bdi0  => -
2015-09-26 04:53:49,110:INFO   :tbotlib   # read 1: Please power off unused systems when you leave!   Thanks, wd.
2015-09-26 04:53:49,110:INFO   :tbotlib   # read 1: *************************************************************
2015-09-26 04:53:49,205:INFO   :tbotlib   # read 1: pollux:~ hs[0;32m [0m$ connect shc
2015-09-26 04:53:49,670:INFO   :tbotlib   # read 1: ### Connect to "shc" using command: /usr/bin/rlogin metis -l shc
2015-09-26 04:53:49,670:INFO   :tbotlib   # read 1: 

2015-09-26 04:53:50,671:INFO   :tbotlib   # read no ret 1 

2015-09-26 04:53:53,673:INFO   :denx      # connected to shc
2015-09-26 04:53:53,673:INFO   :tbotlib   # *****************************************
2015-09-26 04:53:53,673:INFO   :tbotlib   # Starting with tc tc_lx_partition_check.py
2015-09-26 04:53:53,674:INFO   :state_linux# switch state to linux
2015-09-26 04:53:53,738:INFO   :tbotlib   # read 1: 
2015-09-26 04:53:54,743:INFO   :tbotlib   # read no ret 1 
ttbott#
2015-09-26 04:53:56,745:INFO   :tbotlib   # write 1: PS1=ttbott#
2015-09-26 04:53:56,840:INFO   :tbotlib   # read 1: PS1=ttbott#
2015-09-26 04:53:56,904:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:53:56,905:INFO   :tbotlib   # *****************************************
2015-09-26 04:53:56,905:INFO   :tbotlib   # Starting with tc tc_lx_mount.py
2015-09-26 04:53:56,905:INFO   :tc_lx_mount# dev: /dev/sda1 fs_type: ext4 dir: /home/hs/mnt
2015-09-26 04:53:56,905:INFO   :state_linux# switch state to linux
2015-09-26 04:53:56,969:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:53:57,973:INFO   :tbotlib   # read no ret 1 
ttbott#
2015-09-26 04:53:59,975:INFO   :tbotlib   # write 1: PS1=ttbott#
2015-09-26 04:54:00,071:INFO   :tbotlib   # read 1: PS1=ttbott#
2015-09-26 04:54:00,135:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:54:01,136:INFO   :tbotlib   # read no ret 1 
ttbott#
2015-09-26 04:54:01,136:INFO   :tbotlib   # write 1: mount
2015-09-26 04:54:01,232:INFO   :tbotlib   # read 1: mount
2015-09-26 04:54:01,232:INFO   :tbotlib   # read 1: 

2015-09-26 04:54:01,328:INFO   :tbotlib   # read 1: 192.168.1.1:/opt/eldk-5.5/armv5te/rootfs-qte-sdk on / type nfs (rw,relatime,vers=3,rsize=4096,wsize=4096,namlen=255,hard,nolock,proto=udp,timeo=11,retrans=3,sec=sys,mountaddr=192.168.1.1,mountvers=3,mountproto=udp,local_lock=all,addr=192.168.1.1)
2015-09-26 04:54:01,328:INFO   :tbotlib   # read 1: devtmpfs on /dev type devtmpfs (rw,relatime,size=241324k,nr_inodes=60331,mode=755)
2015-09-26 04:54:01,329:INFO   :tbotlib   # read 1: proc on /proc type proc (rw,relatime)
2015-09-26 04:54:01,329:INFO   :tbotlib   # read 1: sysfs on /sys type sysfs (rw,relatime)
2015-09-26 04:54:01,329:INFO   :tbotlib   # read 1: debugfs on /sys/kernel/debug type debugfs (rw,relatime)
2015-09-26 04:54:01,329:INFO   :tbotlib   # read 1: tmpfs on /run type tmpfs (rw,nosuid,nodev,mode=755)
2015-09-26 04:54:01,329:INFO   :tbotlib   # read 1: tmpfs on /var/volatile type tmpfs (rw,relatime)
2015-09-26 04:54:01,329:INFO   :tbotlib   # read 1: devpts on /dev/pts type devpts (rw,relatime,gid=5,mode=620)
2015-09-26 04:54:01,345:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:54:02,377:INFO   :tbotlib   # read no ret 1 
ttbott#
2015-09-26 04:54:02,378:INFO   :tbotlib   # write 1: mount -t ext4 /dev/sda1 /home/hs/mnt
2015-09-26 04:54:02,473:INFO   :tbotlib   # read 1: mount -t ext4 /dev/sda1 /home/hs/mnt
2015-09-26 04:54:02,475:INFO   :tbotlib   # read 1: 

2015-09-26 04:54:09,143:INFO   :tbotlib   # read 1: [  173.521053] EXT4-fs (sda1): recovery complete
2015-09-26 04:54:09,174:INFO   :tbotlib   # read 1: [  173.535375] EXT4-fs (sda1): mounted filesystem with ordered data mode. Opts: (null)
2015-09-26 04:54:09,175:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:54:09,175:INFO   :tbotlib   # End of TC: %s success
2015-09-26 04:54:09,175:INFO   :tbotlib   # -----------------------------------------
2015-09-26 04:54:09,175:INFO   :tbotlib   # *****************************************
2015-09-26 04:54:09,175:INFO   :tbotlib   # Starting with tc tc_lx_create_dummy_file.py
2015-09-26 04:54:09,253:INFO   :tc_lx_create_dummy_file# linux create dummy file
2015-09-26 04:54:09,253:INFO   :state_linux# switch state to linux
2015-09-26 04:54:09,317:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:54:10,317:INFO   :tbotlib   # read no ret 1 
ttbott#
2015-09-26 04:54:12,319:INFO   :tbotlib   # write 1: PS1=ttbott#
2015-09-26 04:54:12,449:INFO   :tbotlib   # read 1: PS1=ttbott#
2015-09-26 04:54:12,449:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:54:13,449:INFO   :tbotlib   # read no ret 1 
ttbott#
2015-09-26 04:54:13,450:INFO   :tbotlib   # write 1: dd if=/dev/urandom of=/tmp/gnlmpf_partition bs=1024 count=1024
2015-09-26 04:54:13,546:INFO   :tbotlib   # read 1: dd if=/dev/urandom of=/tmp/gnlmpf_partition bs=1024 count=1024
2015-09-26 04:54:13,546:INFO   :tbotlib   # read 1: 

2015-09-26 04:54:14,261:INFO   :tbotlib   # read 1: 1024+0 records in
2015-09-26 04:54:14,261:INFO   :tbotlib   # read 1: 1024+0 records out
2015-09-26 04:54:14,261:INFO   :tbotlib   # read 1: 1048576 bytes (1.0 MB) copied, 0.660412 s, 1.6 MB/s
2015-09-26 04:54:14,262:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:54:14,262:INFO   :tbotlib   # End of TC: %s success
2015-09-26 04:54:14,262:INFO   :tbotlib   # -----------------------------------------
2015-09-26 04:54:15,278:INFO   :tbotlib   # read no ret 1 
ttbott#
2015-09-26 04:54:15,279:INFO   :tbotlib   # write 1: cp /tmp/gnlmpf_partition /home/hs/mnt
2015-09-26 04:54:15,374:INFO   :tbotlib   # read 1: cp /tmp/gnlmpf_partition /home/hs/mnt
2015-09-26 04:54:15,439:INFO   :tbotlib   # read 1: 

2015-09-26 04:54:15,503:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:54:16,511:INFO   :tbotlib   # read no ret 1 
ttbott#
2015-09-26 04:54:16,511:INFO   :tbotlib   # write 1: umount /dev/sda1
2015-09-26 04:54:16,797:INFO   :tbotlib   # read 1: umount /dev/sda1
2015-09-26 04:54:16,797:INFO   :tbotlib   # read 1: 

2015-09-26 04:54:16,961:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:54:16,961:INFO   :tbotlib   # *****************************************
2015-09-26 04:54:16,962:INFO   :tbotlib   # Starting with tc tc_lx_mount.py
2015-09-26 04:54:16,962:INFO   :tc_lx_mount# dev: /dev/sda1 fs_type: ext4 dir: /home/hs/mnt
2015-09-26 04:54:16,962:INFO   :state_linux# switch state to linux
2015-09-26 04:54:17,126:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:54:18,127:INFO   :tbotlib   # read no ret 1 
ttbott#
2015-09-26 04:54:20,129:INFO   :tbotlib   # write 1: PS1=ttbott#
2015-09-26 04:54:20,225:INFO   :tbotlib   # read 1: PS1=ttbott#
2015-09-26 04:54:20,289:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:54:21,289:INFO   :tbotlib   # read no ret 1 
ttbott#
2015-09-26 04:54:21,290:INFO   :tbotlib   # write 1: mount
2015-09-26 04:54:21,386:INFO   :tbotlib   # read 1: mount
2015-09-26 04:54:21,387:INFO   :tbotlib   # read 1: 

2015-09-26 04:54:21,452:INFO   :tbotlib   # read 1: 192.168.1.1:/opt/eldk-5.5/armv5te/rootfs-qte-sdk on / type nfs (rw,relatime,vers=3,rsize=4096,wsize=4096,namlen=255,hard,nolock,proto=udp,timeo=11,retrans=3,sec=sys,mountaddr=192.168.1.1,mountvers=3,mountproto=udp,local_lock=all,addr=192.168.1.1)
2015-09-26 04:54:21,483:INFO   :tbotlib   # read 1: devtmpfs on /dev type devtmpfs (rw,relatime,size=241324k,nr_inodes=60331,mode=755)
2015-09-26 04:54:21,484:INFO   :tbotlib   # read 1: proc on /proc type proc (rw,relatime)
2015-09-26 04:54:21,484:INFO   :tbotlib   # read 1: sysfs on /sys type sysfs (rw,relatime)
2015-09-26 04:54:21,484:INFO   :tbotlib   # read 1: debugfs on /sys/kernel/debug type debugfs (rw,relatime)
2015-09-26 04:54:21,484:INFO   :tbotlib   # read 1: tmpfs on /run type tmpfs (rw,nosuid,nodev,mode=755)
2015-09-26 04:54:21,485:INFO   :tbotlib   # read 1: tmpfs on /var/volatile type tmpfs (rw,relatime)
2015-09-26 04:54:21,485:INFO   :tbotlib   # read 1: devpts on /dev/pts type devpts (rw,relatime,gid=5,mode=620)
2015-09-26 04:54:21,485:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:54:22,501:INFO   :tbotlib   # read no ret 1 
ttbott#
2015-09-26 04:54:22,502:INFO   :tbotlib   # write 1: mount -t ext4 /dev/sda1 /home/hs/mnt
2015-09-26 04:54:22,597:INFO   :tbotlib   # read 1: mount -t ext4 /dev/sda1 /home/hs/mnt
2015-09-26 04:54:22,597:INFO   :tbotlib   # read 1: 

2015-09-26 04:54:22,712:INFO   :tbotlib   # read 1: [  187.060544] EXT4-fs (sda1): mounted filesystem with ordered data mode. Opts: (null)
2015-09-26 04:54:22,712:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:54:22,712:INFO   :tbotlib   # End of TC: %s success
2015-09-26 04:54:22,712:INFO   :tbotlib   # -----------------------------------------
2015-09-26 04:54:23,713:INFO   :tbotlib   # read no ret 1 
ttbott#
2015-09-26 04:54:23,713:INFO   :tbotlib   # write 1: cmp /tmp/gnlmpf_partition /home/hs/mnt/gnlmpf_partition
2015-09-26 04:54:23,809:INFO   :tbotlib   # read 1: cmp /tmp/gnlmpf_partition /home/hs/mnt/gnlmpf_partition
2015-09-26 04:54:23,810:INFO   :tbotlib   # read 1: 

2015-09-26 04:54:24,025:INFO   :tbotlib   # read 1: ttbott#
2015-09-26 04:54:25,041:INFO   :tbotlib   # read no ret 1 
ttbott#
2015-09-26 04:54:25,041:INFO   :tbotlib   # End of TC: %s success
2015-09-26 04:54:25,042:INFO   :tbotlib   # -----------------------------------------
2015-09-26 04:54:25,042:INFO   :tbotlib   # End of TBOT: success
```
