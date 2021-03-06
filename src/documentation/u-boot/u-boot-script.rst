U-Boot Scripting Capabilities
-----------------------------


U-Boot allows to store commands or command sequences in a plain text file. Using the :redtext:`mkimage` tool you can then convert this file into a script image which can be executed using U-Boot's :redtext:`source` command, see section `source - run script from memory`_.

|Tip| Hint: maximum flexibility can be achieved if you are using the Hush shell as command interpreter in U-Boot, see `How the Command Line Parsing Works`_

How the Command Line Parsing Works
----------------------------------

There are two different command line parsers available with U-Boot: the old "simple" one, and the much more powerful "hush" shell: 

Old, simple command line parser
...............................

- supports environment variables (through setenv / saveenv commands)
- several commands on one line, separated by ';'
- variable substitution using "... ${_variablename_} ..." syntax
    |Warning| NOTE: Older versions of U-Boot used "$(...)" for variable substitution. Support for this syntax is still present in current versions, but will be removed soon. Please use "${...}" instead, which has the additional benefit that your environment definitions are compatible with the Hush shell, too.
- special characters ('$', ';') can be escaped by prefixing with '\', for example:

::

            setenv bootcmd bootm \${address}


- You can also escape text by enclosing in single apostrophes, for example:

::

            setenv addip 'setenv bootargs ${bootargs} ip=${ipaddr}:${serverip}:${gatewayip}:${netmask}:${hostname}:${netdev}:off'


Hush shell
..........

- similar to Bourne shell, with control structures like if...then...else...fi, for...do...done, while...do...done, until...do...done, ...
- supports environment ("global") variables (through setenv / saveenv commands) and local shell variables (through standard shell syntax name=value ); only environment variables can be used with the run command, especially as the variable to run (i. e. the first argument).
- In the current implementation, the local variables space and global environment variables space are separated. Local variables are those you define by simply typing like name=value. To access a local variable later on, you have to write '$name' or '${name}'; to execute the contents of a variable directly you can type '$name' at the command prompt. Note that local variables can only be used for simple commands, not for compound commands etc.
- Global environment variables are those you can set and print using setenv and printenv. To run a command stored in such a variable, you need to use the run command, and you must not use the '$' sign to access them.
- To store commands and special characters in a variable, use single quotation marks surrounding the whole text of the variable, instead of the backslashes before semicolons and special symbols.
- Be careful when using the hash ('#') character - like with a "real" Bourne shell it is the comment character, so you have to escape it when you use it in the value of a variable.

Examples:

::

        setenv bootcmd bootm \$address
        setenv addip 'setenv bootargs $bootargs ip=$ipaddr:$serverip:$gatewayip:$netmask:$hostname:$netdev:off'


Hush shell scripts
..................

Here are a few examples for the use of the advanced capabilities of the hush shell in U-Boot environment variables or scripts: 

tbot_ref:hush_example_1_tb_con_1_1.txt
tbot_ref:hush_example_2_tb_con_1_1.txt

Instead of "echo Image OK" there could be a command (sequence) to boot or otherwise deal with the correct image; instead of the "echo Image corrupted!!" there could be a command (sequence) to (load and) boot an alternative image, etc. 

For Example:

tbot_ref:hush_example_3_tb_con_1_1.txt

This will check if the image at address "addr1" is ok and boot it; if the image is not ok, the alternative image at address "addr2" will be checked and booted if it is found to be OK. If both images are missing or corrupted, a new image will be loaded over TFTP and checked with imi.

General rules
.............

1. If a command line (or an environment variable executed by a run command) contains several commands separated by semicolons, and one of these commands fails, the remaining commands will still be executed.
2. If you execute several variables with one call to run (i. e. calling run with a list of variables as arguments), any failing command will cause run to terminate, i. e. the remaining variables are not executed.

