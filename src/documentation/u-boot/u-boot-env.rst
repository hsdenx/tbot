Environment Variables Commands
------------------------------

printenv- print environment variables
.....................................

tbot_ref:help_printenv_tb_con_1_1.txt

The :redtext:`printenv` command prints one, several or all variables of the U-Boot environment. When arguments are given, these are interpreted as the names of environment variables which will be printed with their values: 

tbot_ref:printenv_ipaddr_hostname_netmask_tb_con_1_1.txt

Without arguments, :redtext:`printenv` prints all a list with all variables in the environment and their values, plus some statistics about the current usage and the total size of the memory available for the environment. 

tbot_ref:printenv_tb_con_1_1.txt

saveenv - save environment variables to persistent storage
..........................................................

tbot_ref:help_saveenv_tb_con_1_1.txt

All changes you make to the U-Boot environment are made in RAM only. They are lost as soon as you reboot the system. If you want to make your changes permanent you have to use the :redtext:`saveenv` command to write a copy of the environment settings to persistent storage, from where they are automatically loaded during startup: 

tbot_ref:saveenv_tb_con_1_1.txt

setenv - set environment variables
..................................

tbot_ref:help_setenv_tb_con_1_1.txt

To modify the U-Boot environment you have to use the :redtext:`setenv` command. When called with exactly one argument, it will delete any variable of that name from U-Boot's environment, if such a variable exists. Any storage occupied for such a variable will be automatically reclaimed: 

tbot_ref:setenv_example_1_tb_con_1_1.txt

When called with more arguments, the first one will again be the name of the variable, and all following arguments will (concatenated by single space characters) form the value that gets stored for this variable. New variables will be automatically created, existing ones overwritten. 

tbot_ref:setenv_example_2_tb_con_1_1.txt

Remember standard shell quoting rules when the value of a variable shall contain characters that have a special meaning to the command line parser (like the $ character that is used for variable substitution or the semicolon which separates commands). Use the backslash (\) character to escape such special characters, or enclose the whole phrase in apstrophes ('). Use "${name}" for variable expansion. 

tbot_ref:setenv_example_3_tb_con_1_1.txt

|Help| There is no restriction on the characters that can be used in a variable name except the restrictions imposed by the command line parser (like using backslash for quoting, space and tab characters to separate arguments, or semicolon and newline to separate commands). Even strange input like :redtext:`=-/|()+=` is a perfectly legal variable name in U-Boot. 

|Warning| A common mistake is to write 

::

  setenv name=value

instead of

::

  setenv name value

There will be no error message, which lets you believe everything went OK, but it didn't: instead of setting the variable name to the value value you tried to delete a variable with the name name=value - this is probably not what you intended! Always remember that name and value have to be separated by space and/or tab characters! 
