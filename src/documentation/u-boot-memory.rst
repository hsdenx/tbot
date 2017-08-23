Memory Commands
---------------

base - print or set address offset
..................................

tbot_ref:tc_ub_memory.py_tb_con_1_1.txt

You can use the :redtext:`base` command (:redtext:`ba`) to print or set a "base address" that is used as the address offset for all subsequent memory commands; the default value of the base address is 0, so all addresses you enter are used unmodified. However, when you repeatedly have to access a certain memory region (like the internal memory of some embedded Power Architecture® processors) it can be very convenient to set the base address to the start of this area and then use only the offsets:

ToDo

crc32 - checksum calculation
............................

The :redtext:`crc32` command (:redtext:`crc`) can be used to calculate a CRC32 checksum over a range of memory: 

tbot_ref:crc_0x80000004_0x3fc_tb_con_1_1.txt

When used with 3 arguments, the command stores the calculated checksum at the given address: 

tbot_ref:crc_0x80000004_0x3fc_0x80000000_tb_con_1_1.txt

As you can see, the CRC32 checksum was not only printed, but also stored at address passed in the 3th argument.

.. raw:: pdf

   PageBreak

cmp - memory compare
....................

tbot_ref:help_cmp_tb_con_1_1.txt

With the :redtext:`cmp` command you can test whether the contents of two memory areas are identical or not. The command will test either the whole area as specified by the 3rd (length) argument, or stop at the first difference. 

tbot_ref:cmp_fail_tb_con_1_1.txt

Like most memory commands the :redtext:cmp` can access the memory in different sizes: as 32 bit (long word), 16 bit (word) or 8 bit (byte) data. If invoked just as cmp the default size (32 bit or long words) is used; the same can be selected explicitly by typing cmp.l instead. If you want to access memory as 16 bit or word data, you can use the variant cmp.w instead; and to access memory as 8 bit or byte data please use cmp.b.

|Warning| Please note that the count argument specifies the number of data items to process, i. e. the number of long words or words or bytes to compare. 

tbot_ref:cmp_long_tb_con_1_1.txt

.. raw:: pdf

   PageBreak

cp - memory copy
................

tbot_ref:help_cp_tb_con_1_1.txt

The :redtext:`cp` command is used to copy memory areas. 

tbot_ref:cp_basic_tb_con_1_1.txt

The :redtext:`cp` command understands the type extensions :redtext:`.l`, :redtext:`.w` and :redtext:`.b` : 

tbot_ref:cp_extensions_tb_con_1_1.txt

.. raw:: pdf

   PageBreak

md - memory display
...................

tbot_ref:help_md_tb_con_1_1.txt

The :redtext:`md` command can be used to display memory contents both as hexadecimal and ASCII data. 

tbot_ref:md_basic_tb_con_1_1.txt

This command can also be used with the type extensions :redtext:`.l`, :redtext:`.w` and :redtext:`.b` : 

tbot_ref:md_extensions_tb_con_1_1.txt

.. raw:: pdf

   PageBreak

The last displayed memory address and the value of the count argument are remembered, so when you enter md again without arguments it will automatically continue at the next address, and use the same count again. 

tbot_ref:md_remember_tb_con_1_1.txt

.. raw:: pdf

   PageBreak

mm - memory modify (auto-incrementing)
......................................

tbot_ref:help_mm_tb_con_1_1.txt

The :redtext:`mm` command is a method to interactively modify memory contents. It will display the address and current contents and then prompt for user input. If you enter a legal hexadecimal number, this new value will be written to the address. Then the next address will be prompted. If you don't enter any value and just press ENTER, then the contents of this address will remain unchanged. The command stops as soon as you enter any data that is not a hex number (like :redtext:`.`): 

tbot_ref:mm_first_tb_con_1_1.txt

Again this command can be used with the type extensions :redtext:`.l`, :redtext:`.w` and :redtext:`.b` :

tbot_ref:mm_second_tb_con_1_1.txt
tbot_ref:mm_third_tb_con_1_1.txt

