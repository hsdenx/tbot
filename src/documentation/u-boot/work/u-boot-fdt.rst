Flattened Device Tree support
-----------------------------

U-Boot is capable of quite comprehensive handling of the flattened device tree blob, implemented by the :redtext:`fdt` family of commands:


::

  => help fdt
  fdt - flattened device tree utility commands
  
  Usage:
  fdt addr [-c]  <addr> [<length>]   - Set the [control] fdt location to <addr>
  fdt apply <addr>                    - Apply overlay to the DT
  fdt move   <fdt> <newaddr> <length> - Copy the fdt to <addr> and make it active
  fdt resize [<extrasize>]            - Resize fdt to size + padding to 4k addr + some optional <extrasize> if needed
  fdt print  <path> [<prop>]          - Recursive print starting at <path>
  fdt list   <path> [<prop>]          - Print one level starting at <path>
  fdt get value <var> <path> <prop>   - Get <property> and store in <var>
  fdt get name <var> <path> <index>   - Get name of node <index> and store in <var>
  fdt get addr <var> <path> <prop>    - Get start address of <property> and store in <var>
  fdt get size <var> <path> [<prop>]  - Get size of [<property>] or num nodes and store in <var>
  fdt set    <path> <prop> [<val>]    - Set <property> [to <val>]
  fdt mknode <path> <node>            - Create a new node after <path>
  fdt rm     <path> [<prop>]          - Delete the node or <property>
  fdt header                          - Display header info
  fdt bootcpu <id>                    - Set boot cpuid
  fdt memory <addr> <size>            - Add/Update memory node
  fdt rsvmem print                    - Show current mem reserves
  fdt rsvmem add <addr> <size>        - Add a mem reserve
  fdt rsvmem delete <index>           - Delete a mem reserves
  fdt chosen [<start> <end>]          - Add/update the /chosen branch in the tree
                                          <start>/<end> - initrd start/end addr
  NOTE: Dereference aliases by omitting the leading '/', e.g. fdt print ethernet0.
  => 

fdt addr - select FDT to work on
................................

First, the blob that is to be operated on should be stored in memory, and U-Boot has to be informed about its location by the :redtext:`fdt addr` command. Once this command has been issued, all subsequent fdt handling commands will use the blob stored at the given address. This address can be changed later on by issuing :redtext:`fdt addr` or :redtext:`fdt move` command. Here's how to load the blob into memory and tell U-Boot its location: 


::

  => setenv fdt_addr_r 0x80000000
  => tftpb ${fdt_addr_r} beagleboneblack/tbot/u-boot.dtb
  link up on port 0, speed 100, full duplex
  Using ethernet@4a100000 device
  TFTP from server 192.168.3.1; our IP address is 192.168.3.20
  Filename 'beagleboneblack/tbot/u-boot.dtb'.
  Load address: 0x80000000
  Loading: *#########
  	 862.3 KiB/s
  done
  Bytes transferred = 45056 (b000 hex)
  => 
  => fdt addr ${fdt_addr_r}
  => 

fdt list - print one level
..........................

Having selected the device tree stored in the blob just loaded, we can inspect its contents. As an FDT usually is quite extensive, it is easier to get information about the structure by looking at selected levels rather than full hierarchies. :redtext:`fdt list` allows us to do exactly this. Let's have a look at the hierarchy one level below the cpus node: 


::

  => fdt list /cpus
  cpus {
  	#address-cells = <0x00000001>;
  	#size-cells = <0x00000000>;
  	cpu@0 {
  	};
  };
  => 

fdt print - recursive print
...........................

To print a complete subtree we use :redtext:`fdt print`. In comparison to the previous example it is obvious that the whole subtree is printed: 


::

  => fdt print /cpus
  cpus {
  	#address-cells = <0x00000001>;
  	#size-cells = <0x00000000>;
  	cpu@0 {
  		compatible = "arm,cortex-a8";
  		device_type = "cpu";
  		reg = <0x00000000>;
  		operating-points = <0x000afc80 0x00139b88 0x000927c0 0x0012b128 0x0007a120 0x00112a88 0x00043238 0x00112a88>;
  		voltage-tolerance = <0x00000002>;
  		clocks = <0x00000002>;
  		clock-names = "cpu";
  		clock-latency = <0x000493e0>;
  		cpu0-supply = <0x00000003>;
  	};
  };
  => 

fdt mknode - create new nodes
.............................

:redtext:`fdt mknode` can be used to attach a new node to the tree. We will use the :redtext:`fdt list` command to verify that the new node has been created and that it is empty: 


::

  => fdt list /
  / {
  	#address-cells = <0x00000001>;
  	#size-cells = <0x00000001>;
  	compatible = "ti,am335x-evm", "ti,am33xx";
  	interrupt-parent = <0x00000001>;
  	model = "TI AM335x EVM";
  	chosen {
  	};
  	aliases {
  	};
  	memory {
  	};
  	cpus {
  	};
  	pmu {
  	};
  	soc {
  	};
  	ocp {
  	};
  	fixedregulator@0 {
  	};
  	fixedregulator@1 {
  	};
  	fixedregulator@2 {
  	};
  	matrix_keypad@0 {
  	};
  	volume_keys@0 {
  	};
  	backlight {
  	};
  	panel {
  	};
  	sound {
  	};
  };
  => fdt mknode / testnode
  => fdt list /
  / {
  	#address-cells = <0x00000001>;
  	#size-cells = <0x00000001>;
  	compatible = "ti,am335x-evm", "ti,am33xx";
  	interrupt-parent = <0x00000001>;
  	model = "TI AM335x EVM";
  	testnode {
  	};
  	chosen {
  	};
  	aliases {
  	};
  	memory {
  	};
  	cpus {
  	};
  	pmu {
  	};
  	soc {
  	};
  	ocp {
  	};
  	fixedregulator@0 {
  	};
  	fixedregulator@1 {
  	};
  	fixedregulator@2 {
  	};
  	matrix_keypad@0 {
  	};
  	volume_keys@0 {
  	};
  	backlight {
  	};
  	panel {
  	};
  	sound {
  	};
  };
  => fdt list /testnode
  testnode {
  };
  => 

fdt set - set node properties
.............................

Now, let's create a property at the newly created node; again we'll use :redtext:`fdt list` for verification: 


::

  => fdt set /testnode testprop
  => fdt set /testnode testprop testvalue
  => fdt list /testnode
  testnode {
  	testprop = "testvalue";
  };
  => 

fdt rm - remove nodes or properties
...................................

The :redtext:`fdt rm` command is used to remove nodes and properties. Let's delete the test property created in the previous paragraph and verify the results: 


::

  => fdt rm /testnode testprop
  => fdt list /testnode
  testnode {
  };
  => fdt rm /testnode
  => fdt list /
  / {
  	#address-cells = <0x00000001>;
  	#size-cells = <0x00000001>;
  	compatible = "ti,am335x-evm", "ti,am33xx";
  	interrupt-parent = <0x00000001>;
  	model = "TI AM335x EVM";
  	chosen {
  	};
  	aliases {
  	};
  	memory {
  	};
  	cpus {
  	};
  	pmu {
  	};
  	soc {
  	};
  	ocp {
  	};
  	fixedregulator@0 {
  	};
  	fixedregulator@1 {
  	};
  	fixedregulator@2 {
  	};
  	matrix_keypad@0 {
  	};
  	volume_keys@0 {
  	};
  	backlight {
  	};
  	panel {
  	};
  	sound {
  	};
  };
  => 

fdt move - move FDT blob to new address
.......................................

To move the blob from one memory location to another we will use the :redtext:`fdt move` command. Besides moving the blob, it makes the new address the "active" one - similar to :redtext:`fdt addr`: 


::

  => fdt move ${fdt_addr_r} 0x8000b000L b000
  => 
  => fdt list /
  / {
  	#address-cells = <0x00000001>;
  	#size-cells = <0x00000001>;
  	compatible = "ti,am335x-evm", "ti,am33xx";
  	interrupt-parent = <0x00000001>;
  	model = "TI AM335x EVM";
  	chosen {
  	};
  	aliases {
  	};
  	memory {
  	};
  	cpus {
  	};
  	pmu {
  	};
  	soc {
  	};
  	ocp {
  	};
  	fixedregulator@0 {
  	};
  	fixedregulator@1 {
  	};
  	fixedregulator@2 {
  	};
  	matrix_keypad@0 {
  	};
  	volume_keys@0 {
  	};
  	backlight {
  	};
  	panel {
  	};
  	sound {
  	};
  };
  => fdt mknod / foobar
  => fdt list /
  / {
  	#address-cells = <0x00000001>;
  	#size-cells = <0x00000001>;
  	compatible = "ti,am335x-evm", "ti,am33xx";
  	interrupt-parent = <0x00000001>;
  	model = "TI AM335x EVM";
  	foobar {
  	};
  	chosen {
  	};
  	aliases {
  	};
  	memory {
  	};
  	cpus {
  	};
  	pmu {
  	};
  	soc {
  	};
  	ocp {
  	};
  	fixedregulator@0 {
  	};
  	fixedregulator@1 {
  	};
  	fixedregulator@2 {
  	};
  	matrix_keypad@0 {
  	};
  	volume_keys@0 {
  	};
  	backlight {
  	};
  	panel {
  	};
  	sound {
  	};
  };
  => 
  => fdt addr ${fdt_addr_r}
  => fdt list /
  / {
  	#address-cells = <0x00000001>;
  	#size-cells = <0x00000001>;
  	compatible = "ti,am335x-evm", "ti,am33xx";
  	interrupt-parent = <0x00000001>;
  	model = "TI AM335x EVM";
  	chosen {
  	};
  	aliases {
  	};
  	memory {
  	};
  	cpus {
  	};
  	pmu {
  	};
  	soc {
  	};
  	ocp {
  	};
  	fixedregulator@0 {
  	};
  	fixedregulator@1 {
  	};
  	fixedregulator@2 {
  	};
  	matrix_keypad@0 {
  	};
  	volume_keys@0 {
  	};
  	backlight {
  	};
  	panel {
  	};
  	sound {
  	};
  };
  => 

fdt chosen - fixup dynamic info
...............................

One of the modifications made by U-Boot to the blob before passing it to the kernel is the addition of the :redtext:`/chosen` node. Linux 2.6 Documentation/powerpc/booting-without-of.txt says that this node is used to store "some variable environment information, like the arguments, or the default input/output devices." To force U-Boot to add the :redtext:`/chosen` node to the current blob, :redtext:`fdt chosen` command can be used. Let's now verify its operation: 


::

  => fdt list /
  / {
  	#address-cells = <0x00000001>;
  	#size-cells = <0x00000001>;
  	compatible = "ti,am335x-evm", "ti,am33xx";
  	interrupt-parent = <0x00000001>;
  	model = "TI AM335x EVM";
  	chosen {
  	};
  	aliases {
  	};
  	memory {
  	};
  	cpus {
  	};
  	pmu {
  	};
  	soc {
  	};
  	ocp {
  	};
  	fixedregulator@0 {
  	};
  	fixedregulator@1 {
  	};
  	fixedregulator@2 {
  	};
  	matrix_keypad@0 {
  	};
  	volume_keys@0 {
  	};
  	backlight {
  	};
  	panel {
  	};
  	sound {
  	};
  };
  => fdt chosen
  => fdt list /
  / {
  	#address-cells = <0x00000001>;
  	#size-cells = <0x00000001>;
  	compatible = "ti,am335x-evm", "ti,am33xx";
  	interrupt-parent = <0x00000001>;
  	model = "TI AM335x EVM";
  	chosen {
  	};
  	aliases {
  	};
  	memory {
  	};
  	cpus {
  	};
  	pmu {
  	};
  	soc {
  	};
  	ocp {
  	};
  	fixedregulator@0 {
  	};
  	fixedregulator@1 {
  	};
  	fixedregulator@2 {
  	};
  	matrix_keypad@0 {
  	};
  	volume_keys@0 {
  	};
  	backlight {
  	};
  	panel {
  	};
  	sound {
  	};
  };
  => fdt list /chosen
  chosen {
  	stdout-path = "/ocp/serial@44e09000";
  	tick-timer = "/ocp/timer@48040000";
  };
  => 

Note: :redtext:`fdt boardsetup` performs board-specific blob updates, most commonly setting clock frequencies, etc. Discovering its operation is left as an excercise for the reader. 

