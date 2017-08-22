Download Commands
-----------------

bootp - boot image via network using BOOTP/TFTP protocol
........................................................

tbot_ref:help_bootp_tb_con_1_1.txt

dhcp - invoke DHCP client to obtain IP/boot params
..................................................

tbot_ref:help_dhcp_tb_con_1_1.txt

.. raw:: pdf

   PageBreak

loadb - load binary file over serial line (kermit mode)
.......................................................

tbot_ref:help_loadb_tb_con_1_1.txt

With kermit you can download binary data via the serial line.

Make sure you use the following settings in kermit.

tbot_ref:loadb_kermit_settings_tb_con_1_1.txt

If you have problems with downloading, may you set the values

::

  set rec pack
  set send pack

to smaller values.

Now for example download u-boot.img.

tbot_ref:loadb_run_tb_con_1_1.txt
tbot_ref:loadb_send_file_tb_con_1_1.txt
tbot_ref:imi_80000000_tb_con_1_1.txt


.. raw:: pdf

   PageBreak

loads - load S-Record file over serial line
...........................................

tbot_ref:help_loads_tb_con_1_1.txt

rarpboot- boot image via network using RARP/TFTP protocol
.........................................................

tbot_ref:help_rarp_tb_con_1_1.txt

tftpboot- boot image via network using TFTP protocol
....................................................

tbot_ref:help_tftp_tb_con_1_1.txt
