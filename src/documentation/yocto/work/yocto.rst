.. |Warning| image:: ./images/Warning-icon.png
   :height: 80
   :width: 80

.. |Help| image:: ./images/help.gif
   :height: 80
   :width: 80

.. |Tip| image:: ./images/tip.gif
   :height: 80
   :width: 80


Yocto
#####

Current Versions
================

Some infos from the yocto build system

bitbake version 1.34.0
yocto distro 2.3.2

Collect here some infos
yocto branch
yocto version

.. raw:: pdf

   PageBreak

Get yocto code for the beagleboneblack
======================================

Preparation
-----------

set shell variable :redtext:`TBOT_BASEDIR` to our work directory, and
if this directory does not exist, create it

Export our workdirectory:


::

  $ export TBOT_BASEDIR=/work/tbot2go/tbot/
  $ 

set shell variable :redtext:`TBOT_BASEDIR_YOCTO` to our yocto work directory,
and if this directory does not exist, create it


::

  $ export TBOT_BASEDIR_YOCTO=$TBOT_BASEDIR/yocto-am335x_evm
  $ 

.. raw:: pdf

   PageBreak

local patches
-------------

go to our work directory:


::

  $ "
  $ stty cols 200
  $ export TERM=vt200
  $ echo $COLUMNS
  200
  $ 

First, get the patches we need with:


.. raw:: pdf

   PageBreak

Yocto source
............

After this, checkout the yocto source:

go to our work directory:



and check out the yocto code:


and apply our local patches:


.. raw:: pdf

   PageBreak

Now get the needed layers:
--------------------------

meta-openembedded:
..................

go to the yocto work directory:

than get the layer:

.. raw:: pdf

   PageBreak

Setup Build Environment
-----------------------

now we have all layers, and can setup our build environment.


and set the correct path in bblayers.conf:


optional (but recommended), you can do the following 2 steps:

setup download directory
........................

All source files, bitbake needs, are stored in the directory
located through the config variable :redtext:`DL_DIR`
replace the marker :redtext:`TBOT_YOCTO_DLDIR` with the
settings you use, for example:


You can share this directory with other users, so source files
need to be downloaded only once.

.. raw:: pdf

   PageBreak

setup shared state cache
........................

Set up the directory for the shared state cache.

Add the correct path in the local.conf file, by replacing the
:redtext:`TBOT_YOCTO_SSTATEDIR` with the setting you need.


Rebuilding everything from scratch needs a lot of time and
resources. Therefore bitbake collects as much as possible
information about each task and stores this information
with a checksum. Poky now stores this information in the
so called :redtext:`shared state cache` and stores the output of
each task in the :redtext:`SSTATE_DIR`. Now, whenever bitbake
starts with a task, it checks if there is information about
this task in the :redtext:`shared state cache` and if the
checksum matches, it can use the stored output saved in the
:redtext:`SSTATE_DIR`.

Find more information:

https://wiki.yoctoproject.org/wiki/Enable_sstate_cache

.. raw:: pdf

   PageBreak

Generate Images
===============

Now we are ready to create the images with:


core-image-minimal
------------------

This generates the following images:



Install Images
==============

install rootfs for NFS boot
---------------------------

sd card image
-------------

copy the sd card image into the nfs:


Then we boot with NFS as rootfs and burn the sd card image
onto the sd card in the bbb:


boot the sd card rootfs image
-----------------------------

check if the version of the rootfs is the same as we expect.

links
=====

.. _tbot: https://github.com/hsdenx/tbot

.. _ELDK: http://www.denx.de/wiki/DULG/ELDK

.. _Ubuntu: http://www.ubuntu.com/

.. _Fedora: http://fedoraproject.org/

.. _OpenEmbedded: http://openembedded.org/wiki/Main_Page

.. _`Yocto Project`: https://www.yoctoproject.org/
