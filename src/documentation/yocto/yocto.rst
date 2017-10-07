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

bitbake version DUTS_BB_VERSION

yocto distro DUTS_DISTRO_VERSION

Collect here some infos
yocto branch
yocto version

.. raw:: pdf

   PageBreak

Get yocto code for the DUTS_BOARDNAME
======================================

Preparation
-----------

set shell variable :redtext:`TBOT_BASEDIR` to our work directory, and
if this directory does not exist, create it

Export our workdirectory:

tbot_ref:export_TBOT_BASEDIR=_work_tbot2go_tbot__tb_ctrl_1_1.txt

set shell variable :redtext:`TBOT_BASEDIR_YOCTO` to our yocto work directory.

tbot_ref:set_yocto_env_var_tb_ctrl_1_1.txt

.. raw:: pdf

   PageBreak

local patches
-------------

go to our work directory:

tbot_ref:cd_TBOT_BASEDIR_tb_ctrl_1_1.txt

First, get the patches we need with:

tbot_ref:tc_workfd_git_clone_source.py_tb_ctrl_1_1.txt


.. raw:: pdf

   PageBreak

Yocto source
............

After this, checkout the yocto source:

go to our work directory:

tbot_ref:cd_TBOT_BASEDIR_tb_ctrl_1_1.txt

and check out the yocto code:

tbot_ref:tc_workfd_git_clone_source.py_tb_ctrl_2_1.txt

and apply our local patches:

tbot_ref:tc_workfd_apply_local_patches.py_tb_ctrl_2_2.txt

.. raw:: pdf

   PageBreak

Now get the needed layers:
--------------------------

meta-openembedded:
..................

go to the yocto work directory:

tbot_ref:tc_workfd_goto_yocto_code.py_tb_ctrl_2_1.txt

than get the layer:

tbot_ref:tc_workfd_git_clone_source.py_tb_ctrl_3_1.txt

.. raw:: pdf

   PageBreak

Setup Build Environment
-----------------------

now we have all layers, and can setup our build environment.


First we have to customize some configurations files

edit bblayers.conf
..................

go to the yocto work directory:

tbot_ref:tc_workfd_goto_yocto_code.py_tb_ctrl_2_1.txt

and create a build directory.
We make it here in our yocto work dir and name it :dirtext:`build`

While at it, copy our default :filetext:`bblayers.conf` and :filetext:`local.conf` from our patchest
into it.

tbot_ref:tc_workfd_goto_lab_source_dir.py_tb_ctrl_3_1.txt

Now edit the :filetext:`bblayers.conf` file. Replace the TBOT_YOCTO_PATH placeholder
with the :shellvar:`$TBOT_BASEDIR_YOCTO` shell variable, to set the correct path in bblayers.conf:

tbot_ref:tc_workfd_goto_lab_source_dir.py_tb_ctrl_4_2.txt

Variables you may want to customize (recommended):

setup download directory
........................

variable :redtext:`TMP`

This is where temporary build files and the final build binaries will end up. Expect to use at least 35GB. You probably want at least 50GB available.
The default location is in the build directory. We do not change it for this documentation.

variable :redtext:`DL_DIR`

This is where the downloaded source files will be stored. You can share this among configurations and build files so I created a general location for this outside the project directory. Make sure the build user has write permission to the directory you decide on.

replace the marker :redtext:`TBOT_YOCTO_DLDIR` with the
settings you want to use, for example:

tbot_ref:tc_workfd_goto_lab_source_dir.py_tb_ctrl_4_3.txt

setup shared state cache
........................
variable :redtext:`SSTATE_DIR`

This is another Yocto build directory that can get pretty big, greater then 5GB.
You can share this directory with other users, so source files need to be downloaded only once.
So it makes sense to place this directory to a place where other can use it too.

Set up the directory for the shared state cache.

tbot_ref:tc_workfd_goto_lab_source_dir.py_tb_ctrl_4_4.txt

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

first we clean our sstate cache, so we get a new image

tbot_ref:tc_workfd_bitbake.py_tb_ctrl_1_1.txt

and bitbake it:

tbot_ref:tc_workfd_bitbake.py_tb_ctrl_2_1.txt

For the records, our build config:

tbot_ref:get_build_info_tb_ctrl_1_1.txt

This generates the following images:

# list all files
# may describe them for what they are

U-Boot images:

tbot_ref:tc_workfd_check_if_file_exist.py_tb_ctrl_1_1.txt
tbot_ref:tc_workfd_check_if_file_exist.py_tb_ctrl_2_1.txt

kernel Image:

tbot_ref:tc_workfd_check_if_file_exist.py_tb_ctrl_3_1.txt

and the DTB
tbot_ref:tc_workfd_check_if_file_exist.py_tb_ctrl_4_1.txt

rootfs:

tbot_ref:tc_workfd_check_if_file_exist.py_tb_ctrl_5_1.txt

and sd card image:

tbot_ref:tc_workfd_check_if_file_exist.py_tb_ctrl_6_1.txt

.. raw:: pdf

   PageBreak

Install Images
==============

First we extract from the rootfs tar file the yocto rootfs version.

tbot_ref:tc_yocto_get_rootfs_from_tarball.py_tb_ctrl_1_1.txt

So we can later, when we booted it, check if we really use the new created
rootfsversion!


install rootfs for NFS boot
---------------------------

For installing the new rootfs in the NFS directory, we do the following 3 steps:

- remove all files in our nfs directory
- go into the nfs directory
- extract the new files into it

tbot_ref:tc_yocto_install_rootfs_as_nfs.py_tb_ctrl_1_1.txt cut 10

sd card image
-------------

copy the sd card image into the nfs:

tbot_ref:tc_board_yocto_install_nfs.py_tb_ctrl_1_1.txt

Then we boot with NFS as rootfs and burn the sd card image
onto the sd card in the bbb:

tbot_ref:tc_ub_boot_linux.py_tb_con_1_2.txt cut 10

now we can write the sd card image onto the sd card.

tbot_ref:tc_board_yocto_install_sdcard.py_tb_con_1_1.txt


boot the sd card rootfs image
-----------------------------

Now we reboot the board and boot with the rootfs on the sd card:

tbot_ref:tc_ub_boot_linux.py_tb_con_2_2.txt

check if the version of the rootfs is the same as we expect.

tbot_ref:tc_workfd_yocto_check_rootfs_version.py_tb_con_1_1.txt

It must be the same as described in `Install Images`_

Or DUTS_YOCTO_VERSION

.. raw:: pdf

   PageBreak

Settings
========

U-Boot Environment
------------------

tbot_ref:tc_ub_load_board_env.py_tb_con_1_1.txt

links
=====

tbot_

.. _tbot: https://github.com/hsdenx/tbot

ELDK_

.. _ELDK: http://www.denx.de/wiki/DULG/ELDK

Ubuntu_

.. _Ubuntu: http://www.ubuntu.com/

Fedora_

.. _Fedora: http://fedoraproject.org/

OpenEmbedded_

.. _OpenEmbedded: http://openembedded.org/wiki/Main_Page

`Yocto Project`_

.. _`Yocto Project`: https://www.yoctoproject.org/
