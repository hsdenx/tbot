mtest - simple RAM test
.......................

tbot_ref:help_mtest_tb_con_1_1.txt

The :redtext:`mtest` provides a simple memory test. 

.. image:: ./images/Warning-icon.png

This tests writes to memory, thus modifying the memory contents. It will fail when applied to ROM or flash memory.

tbot_ref:mtest_run_tb_con_1_1.txt

This command may crash the system when the tested memory range includes areas that are needed for the operation of the U-Boot firmware (like exception vector code, or U-Boot's internal program code, stack or heap memory areas).
