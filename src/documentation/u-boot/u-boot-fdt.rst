Flattened Device Tree support
-----------------------------

U-Boot is capable of quite comprehensive handling of the flattened device tree blob, implemented by the :redtext:`fdt` family of commands:

tbot_ref:help_fdt_tb_con_1_1.txt

fdt addr - select FDT to work on
................................

First, the blob that is to be operated on should be stored in memory, and U-Boot has to be informed about its location by the :redtext:`fdt addr` command. Once this command has been issued, all subsequent fdt handling commands will use the blob stored at the given address. This address can be changed later on by issuing :redtext:`fdt addr` or :redtext:`fdt move` command. Here's how to load the blob into memory and tell U-Boot its location: 

tbot_ref:fdt_addr_prepare_tb_con_1_1.txt
tbot_ref:fdt_addr_tb_con_1_1.txt

fdt list - print one level
..........................

Having selected the device tree stored in the blob just loaded, we can inspect its contents. As an FDT usually is quite extensive, it is easier to get information about the structure by looking at selected levels rather than full hierarchies. :redtext:`fdt list` allows us to do exactly this. Let's have a look at the hierarchy one level below the cpus node: 

tbot_ref:fdt_list_tb_con_1_1.txt

fdt print - recursive print
...........................

To print a complete subtree we use :redtext:`fdt print`. In comparison to the previous example it is obvious that the whole subtree is printed: 

tbot_ref:fdt_print_tb_con_1_1.txt

fdt mknode - create new nodes
.............................

:redtext:`fdt mknode` can be used to attach a new node to the tree. We will use the :redtext:`fdt list` command to verify that the new node has been created and that it is empty: 

tbot_ref:fdt_mknode_tb_con_1_1.txt

fdt set - set node properties
.............................

Now, let's create a property at the newly created node; again we'll use :redtext:`fdt list` for verification: 

tbot_ref:fdt_setnode_tb_con_1_1.txt

fdt rm - remove nodes or properties
...................................

The :redtext:`fdt rm` command is used to remove nodes and properties. Let's delete the test property created in the previous paragraph and verify the results: 

tbot_ref:fdt_rmnode_tb_con_1_1.txt

fdt move - move FDT blob to new address
.......................................

To move the blob from one memory location to another we will use the :redtext:`fdt move` command. Besides moving the blob, it makes the new address the "active" one - similar to :redtext:`fdt addr`: 

tbot_ref:fdt_move_node_tb_con_1_1.txt
tbot_ref:fdt_move_node_2_tb_con_1_1.txt
tbot_ref:fdt_move_node_3_tb_con_1_1.txt

fdt chosen - fixup dynamic info
...............................

One of the modifications made by U-Boot to the blob before passing it to the kernel is the addition of the :redtext:`/chosen` node. Linux 2.6 Documentation/powerpc/booting-without-of.txt says that this node is used to store "some variable environment information, like the arguments, or the default input/output devices." To force U-Boot to add the :redtext:`/chosen` node to the current blob, :redtext:`fdt chosen` command can be used. Let's now verify its operation: 

tbot_ref:fdt_chosen_tb_con_1_1.txt

Note: :redtext:`fdt boardsetup` performs board-specific blob updates, most commonly setting clock frequencies, etc. Discovering its operation is left as an excercise for the reader. 

