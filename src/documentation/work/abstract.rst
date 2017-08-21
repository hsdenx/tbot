.. role:: redtext
.. role:: bluetext

Abstract
########

About this Document
===================

The documentation is written in reStructuredText_ and converted into a pdf document.
Some parts of this document are created automatically out of the log files from the tbot build process.

.. _reStructuredText: https://de.wikipedia.org/wiki/ReStructuredText

This document is generated for the beagleboneblack with U-Boot version

U-Boot 2017.07-rc2-00090-g08546df (Aug 16 2017 - 10:50:22 +0200)

Introduction
============

This document describes how to use the firmware U-Boot and the operating system Linux in Embedded Power Architecture®, ARM and MIPS Systems.

There are many steps along the way, and it is nearly impossible to cover them all in depth, but we will try to provide all necessary information to get an embedded system running from scratch. This includes all the tools you will probably need to configure, build and run U-Boot and Linux.

First, we describe how to install the Cross Development Tools Embedded Linux Development Kit which you probably need - at least when you use a standard x86 PC running Linux or a Sun Solaris 2.6 system as build environment.

Then we describe what needs to be done to connect to the serial console port of your target: you will have to configure a terminal emulation program like cu or kermit.

In most cases you will want to load images into your target using ethernet; for this purpose you need TFTP and DHCP / BOOTP servers. A short description of their configuration is given.

A description follows of what needs to be done to configure and build the U-Boot for a specific board, and how to install it and get it working on that board.

The configuration, building and installing of Linux in an embedded configuration is the next step. We use SELF, our Simple Embedded Linux Framework, to demonstrate how to set up both a development system (with the root filesystem mounted over NFS) and an embedded target configuration (running from a ramdisk image based on busybox).

This document does not describe what needs to be done to port U-Boot or Linux to a new hardware platform. Instead, it is silently assumed that your board is already supported by U-Boot and Linux.

.. raw:: pdf

   PageBreak

Disclaimer
==========

Use the information in this document at your own risk. DENX disavows any potential liability for the contents of this document. Use of the concepts, examples, and/or other content of this document is entirely at your own risk. All copyrights are owned by their owners, unless specifically noted otherwise. Use of a term in this document should not be regarded as affecting the validity of any trademark or service mark. Naming of particular products or brands should not be seen as endorsements. 


