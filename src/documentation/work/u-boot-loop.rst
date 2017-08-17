loop - infinite loop on address range
.....................................


::

  => help loop
  loop - infinite loop on address range
  
  Usage:
  loop [.b, .w, .l] address number_of_objects
  => 

The :redtext:`loop` command reads in a tight loop from a range of memory. This is intended as a special form of a memory test, since this command tries to read the memory as fast as possible.

.. image:: ./images/Warning-icon.png

This command will never terminate. There is no way to stop it but to reset the board! 
