=======
tbot2go
=======

tbot2go proides a setup, with which you can immediately start
with testing your hw. The setup is prepared to run on a raspberry
Pi and an attached LinkerKit plate. The raspberr pi works as HostPC and
LabPC. As compiling makes no sense on a raspberry pi, we connect
to a so called compilePC wheen we do CPU intensive tasks like
compiling. So you need to provide a compile PC for such tasks.

HW setup
========

Buy:

- Raspberry PI

  https://www.conrad.de/de/raspberry-pi-3-model-b-1-gb-ohne-betriebssystem-1419716.html

- Linker Kit

  https://www.conrad.de/de/raspberry-pi-erweiterungs-platine-lk-base-rb-raspberry-pi-a-b-b-1267835.html

- Relay

  https://www.conrad.de/de/linker-kit-erweiterungs-platine-relais-lk-relai-pcduino-raspberry-pi-a-b-b-arduino-1267859.html

  If you want to switch boot mode + 1

- cable to connect relay/LED with Linker Kit

  https://www.conrad.de/de/raspberry-pi-verbindungskabel-lk-cable-20-pcduino-raspberry-pi-a-b-b-arduino-1267839.html

- Power adapter for the raspberry pi

- SD card for the raspberry PI

- USB2serial adapter

optional:

- LED / Buttons

  https://www.conrad.de/de/linker-kit-erweiterungs-platine-relais-lk-relai-pcduino-raspberry-pi-a-b-b-arduino-1267859.html

  https://www.conrad.de/de/linker-kit-erweiterungs-platine-relais-lk-relai-pcduino-raspberry-pi-a-b-b-arduino-1267859.html
  

tbot setup
==========

If you are interested send me an EMail, I can deliver a ready to run
sd card image for the raspberry Pi, but you can prepare a sd card
image on your own, see steps `install steps raspberry pi`_.

bbb bootmmodes:
---------------

=======   =====  ======
medium    linux  U-Boot
=======   =====  ======
sd card   mmc0   MMC1
emmc      mmc1   MMC2
=======   =====  ======


To switch between botmodes we can use the PIN P8_43
attached to GND -> boot from sd, floating -> boot
from emmc.

So, we define here:

normal (off) : we boot from emmc

recovery (on): we boot from sd card

edit in config/lab_tbot2go
--------------------------

Adapt the following vars for your setup

::

  ip: set here the ip of your raspberry pi

::

  workdirpaths: defaults should work, only pay attention, that
                the tbot workdir defined in "tc_workfd_work_dir"
                must be the same for the labPC and the compilePC

Adapt this to your compile PC settings, also do not forget to adapt password.py
see later.

::

  compile_pc_ip = '192.168.3.XXX'
  compile_pc_user= 'hs'
  compile_pc_prompt = 'ttbott_compile> '
  connect_to_compilepc_ssh_opt = ''
  connect_to_compilepc_ssh_cmd_prompt = '$ '

src/tc/lab/tc_lab_prepare_tbot2go.py
------------------------------------

currently not used. You should instead setup the eth0
interface correctly.

board settings:
---------------

Adapt the toolchain to your setting on your compile PC

::

  tc_workfd_set_toolchain_t_p
  tc_workfd_set_toolchain_cr_co

edit (if not using beagleboneblack) in config/beagleboneblack.py
(best copy config/beagleboneblack.py into another file config/yourboard.py)

::

  linux_user = 'root' # linux board user
  uboot_prompt = '=> ' # uboot prompt of board
  linux_prompt = 'ttbott> '

If needed, add board specific U-Boot Envvariables

::

  ub_load_board_env_set

Adapt U-Boot / Linux settings

Here you may adapt a lot of board specific things

For example, where to get the u-boot tree:

::

  tc_lab_get_uboot_source_git_repo

or linux tree:

::

  tc_lab_get_linux_source_git_repo
  
How to boot linux from u-boot

set

::

  ub_boot_linux_cmd

to the U-Boot command you use for booting linux.

edit password.py:
-----------------

- compile PC setup

  search the line

::

  elif board == 'compilepc' or board =="

and set the ip for your compile PC, also
add the password or key for it if needed.

- raspberrypi password

  search the line

::

  if (board == '192.168.3.1'):

and change the ip to the ip your raspberry pi has.

- also add here the passwords you need for your board


limitations
-----------

raspberry pi connects to the world over WLAN
the ethernet port eth0 is for internal testing
purposes

This eth0 and wlan must be in different subnets

Default eth0 is assigned to 192.168.3.x

! This is not a must, but default. If you want
  to change this, you have to edit a little bit more.

So, you can connect the board direct to eth0 of the
raspberry PI.

This needs that the compilePC is reachable over WLAN

You can of course add a switch and connect the board,
raspberry PI and the compile PC to the switch.

prepare compile PC
------------------

- workdir

  create a workdir where tbot can work. Edit this path in _labtbot2go_workdir

  !! This must be the same path as th workdir on the labpc !!

  Please help me here to get rid of this !

- clone Code you compile

  May you clone u-boot and linux, so you can reference it when checking out
  U-Boot and/or linux for a board.

- install a toolchain

  your choice. If you have no idea how, use the buildman tool in
  U-Boot code, see 

  http://git.denx.de/?p=u-boot.git;a=blob;f=tools/buildman/README;h=aaee58152b89dc94fd98d19edf83c7637af373c5;hb=HEAD

  and search for "--fetch-arch"

  buildman prints, to which place it installs the tolchain.

  adapt this in your board config settings variables:

::

  tc_workfd_set_toolchain_t_p
  tc_workfd_set_toolchain_cr_co


install steps raspberry pi
--------------------------

If you want to create the sd card image for the raspberry pi on your own.

- download a raspberry pi image from

  https://www.raspberrypi.org/downloads/raspbian/

- I prefer vim, so:

::

  sudo apt-get install vim

- kermit

::

  sudo apt-get install ckermit

- tftp server

::

  sudo apt-get install xinetd tftpd tftp

  setup file:



- dhcp server

::

  sudo apt-get install isc-dhcp-server

- nfs server

::

  sudo apt-get install nfs-kernel-server

-> /etc/exports get created, edit it.

we use the line:

::

  /work/tbot2go/tbot/nfs  192.168.3.0/255.255.255.0(rw,no_root_squash,sync)

restart NFS server

::

  sudo exportfs -ra
  sudo service nfs-kernel-server restart


check if NFS server runs

::

  sudo service nfs-kernel-server status

and

::

  sudo rpcinfo -p

Here you should see the entries (portmapper, mountd, nfs, nlockmgr)



- packages needed for tbot

::

  sudo apt-get install python-cffi
  sudo pip install paramiko
  sudo apt-get install u-boot-tools
  sudo apt-get install gnuplot

- install tbot, see Guide for using tbot with BBB

- gnuplot adaptions

  As we cannot pass a path to gnuplot you need to adapt the
  file "src/files/balkenplot.sem"

::

   pi@raspberrypitbot2go tbot (tbot2go) $ git diff
   diff --git a/src/files/balkenplot.sem b/src/files/balkenplot.sem
   index 839b3ea..a63be3c 100644
   --- a/src/files/balkenplot.sem
   +++ b/src/files/balkenplot.sem
   @@ -19,4 +19,4 @@ set termoption noenhanced
    set output "output.jpg"
    
    i = 2
   -plot 'stat.dat' using 2:xtic(1), for [i=3:3] '' using i
   +plot '/home/pi/tbot2go/tbot/stat.dat' using 2:xtic(1), for [i=3:3] '' using i


- graphviz

::

  sudo apt-get install graphviz

for documentation backend:

  * ansi2txt

    we use ansi2txt for cleaning a shell log file, find newest version:

    https://sourceforge.net/projects/ansi2txt/files/latest/download

    untar the tar.gz file, go into it and follow the README

  * rst2pdf

    sudo apt-get install rst2pdf 

for dashboard backend:

::

  sudo apt-get install mysql-server
  sudo apt-get install mysql-client
  sudo apt-get install python-mysqldb

login into new server

::

  sudo mysql -u root

set a new root passwd

::

  update mysql.user set password=password('tbot') where user='root';
  flush privileges;

Now you can login only with typing passwd:

::

  pi@raspberrypitbot2go tbot (tbot2go) $ sudo mysql -u root -p
  Enter password: 
  Welcome to the MariaDB monitor.  Commands end with ; or \g.
  Your MariaDB connection id is 9
  Server version: 10.1.23-MariaDB-9+deb9u1 Raspbian 9.0
  
  Copyright (c) 2000, 2017, Oracle, MariaDB Corporation Ab and others.
  
  Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
  
  MariaDB [(none)]> 


Create a database "tbot_root":

::

  CREATE SCHEMA tbot_root;
  CREATE TABLE tbot_root.tbot_results(
  tbot_id INT NOT NULL AUTO_INCREMENT,
  test_date DATETIME NULL,
  toolchain VARCHAR(45) NULL,
  binaryversion VARCHAR(45) NULL,
  defname VARCHAR(45) NULL,
  testcase VARCHAR(45) NULL,
  success VARCHAR(45) NULL,
  state VARCHAR(45) NULL,
  PRIMARY KEY (id));

Create user "tbot" with password "tbot" and grant all privileges on the created database:

::

  CREATE USER 'tbot'@'localhost' IDENTIFIED BY 'tbot';
  GRANT ALL PRIVILEGES ON tbot_root.tbot_results TO 'tbot'@'localhost';
  FLUSH PRIVILEGES;

Tips for the DB

complete reset

::

  truncate tbot_root.tbot_results;


delete the last XXX entries

::

  DELETE FROM tbot_root.tbot_results ORDER BY tbot_id DESC limit XXX;



- setting up webserver

::

  sudo apt-get install php
  sudo apt-get install apache2
  sudo apt-get install libapache2-mod-php7.0
  sudo apt-get install php5 libapache2-mod-php5
  sudo apt-get install apache2 mysql-server phpmyadmin php5-cli

change access rights for "/var/www/html"

::

  sudo chown -R pi /var/www/html/


- create "/var/www/html/tbot" and "/var/www/html/tests"
  and change access rights

- cp php scripts from tbot:src/dashboard to "/var/www/html/tests"

- check in your favorite browser if

::

  http://<ip_of_your_raspberrypi>/tests/read_db.php

