help - print online help
........................


::

  => help help
  help - print command description/usage
  
  Usage:
  help 
  	- print brief description of all commands
  help command ...
  	- print detailed usage of 'command'
  => 

The :redtext:`help` command (:redtext:`h` or :redtext:`?`) prints online help. Without any arguments, it prints a list of all U-Boot commands that are available in your configuration of U-Boot. You can get detailed information for a specific command by typing its name as argument to the help command: 


::

  => help printenv tftp
  printenv - print environment variables
  
  Usage:
  printenv [-a]
      - print [all] values of all environment variables
  printenv name ...
      - print value of environment variable 'name'
  tftpboot - boot image via network using TFTP protocol
  
  Usage:
  tftpboot [loadAddress] [[hostIPaddr:]bootfilename]
  => 
