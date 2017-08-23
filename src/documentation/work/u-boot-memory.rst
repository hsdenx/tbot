Memory Commands
---------------

base - print or set address offset
..................................


::

  
  => help base
  base - print or set address offset
  
  Usage:
  base 
      - print address offset for memory commands
  base off
      - set address offset for memory commands to 'off'
  => 

You can use the :redtext:`base` command (:redtext:`ba`) to print or set a "base address" that is used as the address offset for all subsequent memory commands; the default value of the base address is 0, so all addresses you enter are used unmodified. However, when you repeatedly have to access a certain memory region (like the internal memory of some embedded Power Architecture® processors) it can be very convenient to set the base address to the start of this area and then use only the offsets:

ToDo

crc32 - checksum calculation
............................

The :redtext:`crc32` command (:redtext:`crc`) can be used to calculate a CRC32 checksum over a range of memory: 


::

  => crc 0x80000004 0x3fc a6d53e40
  => 

When used with 3 arguments, the command stores the calculated checksum at the given address: 


::

  => crc 0x80000004 0x3fc 0x80000000 a6d53e40
  => md 0x80000000 4
  80000000: 403ed5a6 b9070000 38000000 38070000    ..>@.......8...8
  => 

As you can see, the CRC32 checksum was not only printed, but also stored at address passed in the 3th argument.

.. raw:: pdf

   PageBreak

cmp - memory compare
....................


::

  => help cmp
  cmp - memory compare
  
  Usage:
  cmp [.b, .w, .l] addr1 addr2 count
  => 

With the :redtext:`cmp` command you can test whether the contents of two memory areas are identical or not. The command will test either the whole area as specified by the 3rd (length) argument, or stop at the first difference. 


::

  => cmp 0x80000000 0x80100000 40000
  Total of 262144 word(s) were the same
  => md 0x80000000 0xc
  80000000: 1cec5b8c 381401ad 6778e393 01fbbcc3    .[.....8..xg....
  80000010: 89e9712a 0fb40e16 6f236743 3b46fbe6    *q......Cg#o..F;
  80000020: ea2356f6 6e7c540f e056e377 7bd28a9f    .V#..T|nw.V....{
  => md 0x80100000 0xc
  80100000: 1cec5b8c 381401ad 6778e393 01fbbcc3    .[.....8..xg....
  80100010: 89e9712a 0fb40e16 6f236743 3b46fbe6    *q......Cg#o..F;
  80100020: ea2356f6 6e7c540f e056e377 7bd28a9f    .V#..T|nw.V....{
  => 

Like most memory commands the :redtext:cmp` can access the memory in different sizes: as 32 bit (long word), 16 bit (word) or 8 bit (byte) data. If invoked just as cmp the default size (32 bit or long words) is used; the same can be selected explicitly by typing cmp.l instead. If you want to access memory as 16 bit or word data, you can use the variant cmp.w instead; and to access memory as 8 bit or byte data please use cmp.b.

|Warning| Please note that the count argument specifies the number of data items to process, i. e. the number of long words or words or bytes to compare. 


::

  => cmp.l 0x80000000 0x80100000 40000
  Total of 262144 word(s) were the same
  => cmp.w 0x80000000 0x80100000 80000
  Total of 524288 halfword(s) were the same
  => cmp.b 0x80000000 0x80100000 100000
  Total of 1048576 byte(s) were the same
  => 

.. raw:: pdf

   PageBreak

cp - memory copy
................


::

  => help cp
  cp - memory copy
  
  Usage:
  cp [.b, .w, .l] source target count
  => 

The :redtext:`cp` command is used to copy memory areas. 


::

  => cp 0x80000000 0x80100000 10000
  => 

The :redtext:`cp` command understands the type extensions :redtext:`.l`, :redtext:`.w` and :redtext:`.b` : 


::

  => cp.l 0x80000000 0x80100000 10000
  => cp.w 0x80000000 0x80100000 20000
  => cp.b 0x80000000 0x80100000 40000
  => 

.. raw:: pdf

   PageBreak

md - memory display
...................


::

  => help md
  md - memory display
  
  Usage:
  md [.b, .w, .l] address [# of objects]
  => 

The :redtext:`md` command can be used to display memory contents both as hexadecimal and ASCII data. 


::

  => md 0x80000000
  80000000: 1cec5b8c 381401ad 6778e393 01fbbcc3    .[.....8..xg....
  80000010: 89e9712a 0fb40e16 6f236743 3b46fbe6    *q......Cg#o..F;
  80000020: ea2356f6 6e7c540f e056e377 7bd28a9f    .V#..T|nw.V....{
  80000030: cfa9bcec b19ace51 b27f4dc5 8eeca28b    ....Q....M......
  80000040: ee9b1d07 09f8e81f 969e7603 6be76204    .........v...b.k
  80000050: b0de9f91 0b9a6062 825adf5e 6914b64e    ....b`..^.Z.N..i
  80000060: 31eb81cc ec1b3009 b7096df7 0546f59b    ...1.0...m....F.
  80000070: d94137a6 3d455f1d 01549ffb 4d7b0a2d    .7A.._E=..T.-.{M
  80000080: 8e8650b9 e2101ce1 d705d373 34455d16    .P......s....]E4
  80000090: b3776306 bb40cb3b 246c65e8 25587336    .cw.;.@..el$6sX%
  800000a0: 65f88ce1 33c09949 67ca3299 e88b24bf    ...eI..3.2.g.$..
  800000b0: 2057a219 45fe820a c5ae6da8 e9b39578    ..W ...E.m..x...
  800000c0: 0d27e891 5201230c da4c518d bfa2cc2b    ..'..#.R.QL.+...
  800000d0: 98386a41 803c36df 1b0d4c5d 09e31558    Aj8..6<.]L..X...
  800000e0: 58ae8bf1 681bc92b 752a350e 3f057db9    ...X+..h.5*u.}.?
  800000f0: a5e3bbbd c7c2239e ecf15559 e91c4375    .....#..YU..uC..
  => 

This command can also be used with the type extensions :redtext:`.l`, :redtext:`.w` and :redtext:`.b` : 


::

  => md.w 0x80000000
  80000000: 5b8c 1cec 01ad 3814 e393 6778 bcc3 01fb    .[.....8..xg....
  80000010: 712a 89e9 0e16 0fb4 6743 6f23 fbe6 3b46    *q......Cg#o..F;
  80000020: 56f6 ea23 540f 6e7c e377 e056 8a9f 7bd2    .V#..T|nw.V....{
  80000030: bcec cfa9 ce51 b19a 4dc5 b27f a28b 8eec    ....Q....M......
  80000040: 1d07 ee9b e81f 09f8 7603 969e 6204 6be7    .........v...b.k
  80000050: 9f91 b0de 6062 0b9a df5e 825a b64e 6914    ....b`..^.Z.N..i
  80000060: 81cc 31eb 3009 ec1b 6df7 b709 f59b 0546    ...1.0...m....F.
  80000070: 37a6 d941 5f1d 3d45 9ffb 0154 0a2d 4d7b    .7A.._E=..T.-.{M
  => md.b 0x80000000
  80000000: 8c 5b ec 1c ad 01 14 38 93 e3 78 67 c3 bc fb 01    .[.....8..xg....
  80000010: 2a 71 e9 89 16 0e b4 0f 43 67 23 6f e6 fb 46 3b    *q......Cg#o..F;
  80000020: f6 56 23 ea 0f 54 7c 6e 77 e3 56 e0 9f 8a d2 7b    .V#..T|nw.V....{
  80000030: ec bc a9 cf 51 ce 9a b1 c5 4d 7f b2 8b a2 ec 8e    ....Q....M......
  => 

.. raw:: pdf

   PageBreak

The last displayed memory address and the value of the count argument are remembered, so when you enter md again without arguments it will automatically continue at the next address, and use the same count again. 


::

  => md.b 0x80000000 0x20
  80000000: 8c 5b ec 1c ad 01 14 38 93 e3 78 67 c3 bc fb 01    .[.....8..xg....
  80000010: 2a 71 e9 89 16 0e b4 0f 43 67 23 6f e6 fb 46 3b    *q......Cg#o..F;
  => md.w 0x80000000
  80000000: 5b8c 1cec 01ad 3814 e393 6778 bcc3 01fb    .[.....8..xg....
  80000010: 712a 89e9 0e16 0fb4 6743 6f23 fbe6 3b46    *q......Cg#o..F;
  80000020: 56f6 ea23 540f 6e7c e377 e056 8a9f 7bd2    .V#..T|nw.V....{
  80000030: bcec cfa9 ce51 b19a 4dc5 b27f a28b 8eec    ....Q....M......
  => md 0x80000000
  80000000: 1cec5b8c 381401ad 6778e393 01fbbcc3    .[.....8..xg....
  80000010: 89e9712a 0fb40e16 6f236743 3b46fbe6    *q......Cg#o..F;
  80000020: ea2356f6 6e7c540f e056e377 7bd28a9f    .V#..T|nw.V....{
  80000030: cfa9bcec b19ace51 b27f4dc5 8eeca28b    ....Q....M......
  80000040: ee9b1d07 09f8e81f 969e7603 6be76204    .........v...b.k
  80000050: b0de9f91 0b9a6062 825adf5e 6914b64e    ....b`..^.Z.N..i
  80000060: 31eb81cc ec1b3009 b7096df7 0546f59b    ...1.0...m....F.
  80000070: d94137a6 3d455f1d 01549ffb 4d7b0a2d    .7A.._E=..T.-.{M
  => 

.. raw:: pdf

   PageBreak

mm - memory modify (auto-incrementing)
......................................


::

  => help mm
  mm - memory modify (auto-incrementing address)
  
  Usage:
  mm [.b, .w, .l] address
  => 

The :redtext:`mm` command is a method to interactively modify memory contents. It will display the address and current contents and then prompt for user input. If you enter a legal hexadecimal number, this new value will be written to the address. Then the next address will be prompted. If you don't enter any value and just press ENTER, then the contents of this address will remain unchanged. The command stops as soon as you enter any data that is not a hex number (like :redtext:`.`): 


::

  => mm 0x80000000
  80000000: 1cec5b8c ? 0
  80000004: 381401ad ? 0xaabbccdd
  80000008: 6778e393 ? 0x01234567
  8000000c: 01fbbcc3 ? .
  => md 0x80000000 10
  80000000: 00000000 aabbccdd 01234567 01fbbcc3    ........gE#.....
  80000010: 89e9712a 0fb40e16 6f236743 3b46fbe6    *q......Cg#o..F;
  80000020: ea2356f6 6e7c540f e056e377 7bd28a9f    .V#..T|nw.V....{
  80000030: cfa9bcec b19ace51 b27f4dc5 8eeca28b    ....Q....M......
  => 

Again this command can be used with the type extensions :redtext:`.l`, :redtext:`.w` and :redtext:`.b` :


::

  => mm.w 0x80000000
  80000000: 0000 ? 0x0101
  80000002: 0000 ? 0x0202
  80000004: ccdd ? 0x4321
  80000006: aabb ? 0x8765
  80000008: 4567 ? .
  => md 0x80000000 10
  80000000: 02020101 87654321 01234567 01fbbcc3    ....!Ce.gE#.....
  80000010: 89e9712a 0fb40e16 6f236743 3b46fbe6    *q......Cg#o..F;
  80000020: ea2356f6 6e7c540f e056e377 7bd28a9f    .V#..T|nw.V....{
  80000030: cfa9bcec b19ace51 b27f4dc5 8eeca28b    ....Q....M......
  => 
  => mm.b 0x80000000
  80000000: 01 ? 0x48
  80000001: 01 ? 0x65
  80000002: 02 ? 0x6c
  80000003: 02 ? 0x6c
  80000004: 21 ? 0x6f
  80000005: 43 ? 0x20
  80000006: 65 ? 0x20
  80000007: 87 ? 0x20
  80000008: 67 ? .
  => md 0x80000000 10
  80000000: 6c6c6548 2020206f 01234567 01fbbcc3    Hello   gE#.....
  80000010: 89e9712a 0fb40e16 6f236743 3b46fbe6    *q......Cg#o..F;
  80000020: ea2356f6 6e7c540f e056e377 7bd28a9f    .V#..T|nw.V....{
  80000030: cfa9bcec b19ace51 b27f4dc5 8eeca28b    ....Q....M......
  => 

