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

  => crc 0x80000004 0x3fc 76a37280
  => 

When used with 3 arguments, the command stores the calculated checksum at the given address: 


::

  => crc 0x80000004 0x3fc 0x80000000 76a37280
  => md 0x80000000 4
  80000000: 8072a376 ff551155 ffffffff 1155ffff    v.r.U.U.......U.
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
  80000000: f5b5afec a76e1eb6 c2c2868a 27e177ee    ......n......w.'
  80000010: 85a9141f ea0e0d29 a3b83b60 9c5abf20    ....)...`;.. .Z.
  80000020: d5f90728 4863422c 3faaa83a 375dfa91    (...,BcH:..?..]7
  => md 0x80100000 0xc
  80100000: f5b5afec a76e1eb6 c2c2868a 27e177ee    ......n......w.'
  80100010: 85a9141f ea0e0d29 a3b83b60 9c5abf20    ....)...`;.. .Z.
  80100020: d5f90728 4863422c 3faaa83a 375dfa91    (...,BcH:..?..]7
  => 

Like most memory commands the :redtext:cmp` can access the memory in different sizes: as 32 bit (long word), 16 bit (word) or 8 bit (byte) data. If invoked just as cmp the default size (32 bit or long words) is used; the same can be selected explicitly by typing cmp.l instead. If you want to access memory as 16 bit or word data, you can use the variant cmp.w instead; and to access memory as 8 bit or byte data please use cmp.b.

.. image:: ./images/Warning-icon.png

Please note that the count argument specifies the number of data items to process, i. e. the number of long words or words or bytes to compare. 


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
  80000000: f5b5afec a76e1eb6 c2c2868a 27e177ee    ......n......w.'
  80000010: 85a9141f ea0e0d29 a3b83b60 9c5abf20    ....)...`;.. .Z.
  80000020: d5f90728 4863422c 3faaa83a 375dfa91    (...,BcH:..?..]7
  80000030: f708c998 a5e27535 2df72513 c2210796    ....5u...%.-..!.
  80000040: 3be665d4 f934ed72 77f30cfe ff7d4927    .e.;r.4....w'I}.
  80000050: 01938b0f 67670a77 a03e2f27 a3cddfa8    ....w.gg'/>.....
  80000060: 7db4427d a8720cdc a00adede db2afc3e    }B.}..r.....>.*.
  80000070: 8b68e416 5fb506a9 8a3d89e7 9155cdc2    ..h...._..=...U.
  80000080: 897baab0 2df979d2 04789346 6d0794e1    ..{..y.-F.x....m
  80000090: 4cf78ec4 7ef5efa3 d2079c53 56a97ebc    ...L...~S....~.V
  800000a0: 1d592a82 12942c92 04204dc4 51a92c67    .*Y..,...M .g,.Q
  800000b0: 8c0a5f41 9eae1126 426a3d45 efb1cdb0    A_..&...E=jB....
  800000c0: 495f405b 228f37a0 558bbf15 6170078a    [@_I.7."...U..pa
  800000d0: f3dd9b6f 992af779 d7a51967 cb0c7480    o...y.*.g....t..
  800000e0: 0d9a0971 b232aaf7 682e70c7 8001b172    q.....2..p.hr...
  800000f0: fd79317c a172ac42 46685500 b25977a8    |1y.B.r..UhF.wY.
  => 

This command can also be used with the type extensions :redtext:`.l`, :redtext:`.w` and :redtext:`.b` : 


::

  => md.w 0x80000000
  80000000: afec f5b5 1eb6 a76e 868a c2c2 77ee 27e1    ......n......w.'
  80000010: 141f 85a9 0d29 ea0e 3b60 a3b8 bf20 9c5a    ....)...`;.. .Z.
  80000020: 0728 d5f9 422c 4863 a83a 3faa fa91 375d    (...,BcH:..?..]7
  80000030: c998 f708 7535 a5e2 2513 2df7 0796 c221    ....5u...%.-..!.
  80000040: 65d4 3be6 ed72 f934 0cfe 77f3 4927 ff7d    .e.;r.4....w'I}.
  80000050: 8b0f 0193 0a77 6767 2f27 a03e dfa8 a3cd    ....w.gg'/>.....
  80000060: 427d 7db4 0cdc a872 dede a00a fc3e db2a    }B.}..r.....>.*.
  80000070: e416 8b68 06a9 5fb5 89e7 8a3d cdc2 9155    ..h...._..=...U.
  => md.b 0x80000000
  80000000: ec af b5 f5 b6 1e 6e a7 8a 86 c2 c2 ee 77 e1 27    ......n......w.'
  80000010: 1f 14 a9 85 29 0d 0e ea 60 3b b8 a3 20 bf 5a 9c    ....)...`;.. .Z.
  80000020: 28 07 f9 d5 2c 42 63 48 3a a8 aa 3f 91 fa 5d 37    (...,BcH:..?..]7
  80000030: 98 c9 08 f7 35 75 e2 a5 13 25 f7 2d 96 07 21 c2    ....5u...%.-..!.
  => 

.. raw:: pdf

   PageBreak

The last displayed memory address and the value of the count argument are remembered, so when you enter md again without arguments it will automatically continue at the next address, and use the same count again. 


::

  => md.b 0x80000000 0x20
  80000000: ec af b5 f5 b6 1e 6e a7 8a 86 c2 c2 ee 77 e1 27    ......n......w.'
  80000010: 1f 14 a9 85 29 0d 0e ea 60 3b b8 a3 20 bf 5a 9c    ....)...`;.. .Z.
  => md.w 0x80000000
  80000000: afec f5b5 1eb6 a76e 868a c2c2 77ee 27e1    ......n......w.'
  80000010: 141f 85a9 0d29 ea0e 3b60 a3b8 bf20 9c5a    ....)...`;.. .Z.
  80000020: 0728 d5f9 422c 4863 a83a 3faa fa91 375d    (...,BcH:..?..]7
  80000030: c998 f708 7535 a5e2 2513 2df7 0796 c221    ....5u...%.-..!.
  => md 0x80000000
  80000000: f5b5afec a76e1eb6 c2c2868a 27e177ee    ......n......w.'
  80000010: 85a9141f ea0e0d29 a3b83b60 9c5abf20    ....)...`;.. .Z.
  80000020: d5f90728 4863422c 3faaa83a 375dfa91    (...,BcH:..?..]7
  80000030: f708c998 a5e27535 2df72513 c2210796    ....5u...%.-..!.
  80000040: 3be665d4 f934ed72 77f30cfe ff7d4927    .e.;r.4....w'I}.
  80000050: 01938b0f 67670a77 a03e2f27 a3cddfa8    ....w.gg'/>.....
  80000060: 7db4427d a8720cdc a00adede db2afc3e    }B.}..r.....>.*.
  80000070: 8b68e416 5fb506a9 8a3d89e7 9155cdc2    ..h...._..=...U.
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
  80000000: f5b5afec ? 0
  80000004: a76e1eb6 ? 0xaabbccdd
  80000008: c2c2868a ? 0x01234567
  8000000c: 27e177ee ? .
  => md 0x80000000 10
  80000000: 00000000 aabbccdd 01234567 27e177ee    ........gE#..w.'
  80000010: 85a9141f ea0e0d29 a3b83b60 9c5abf20    ....)...`;.. .Z.
  80000020: d5f90728 4863422c 3faaa83a 375dfa91    (...,BcH:..?..]7
  80000030: f708c998 a5e27535 2df72513 c2210796    ....5u...%.-..!.
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
  80000000: 02020101 87654321 01234567 27e177ee    ....!Ce.gE#..w.'
  80000010: 85a9141f ea0e0d29 a3b83b60 9c5abf20    ....)...`;.. .Z.
  80000020: d5f90728 4863422c 3faaa83a 375dfa91    (...,BcH:..?..]7
  80000030: f708c998 a5e27535 2df72513 c2210796    ....5u...%.-..!.
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
  80000000: 6c6c6548 2020206f 01234567 27e177ee    Hello   gE#..w.'
  80000010: 85a9141f ea0e0d29 a3b83b60 9c5abf20    ....)...`;.. .Z.
  80000020: d5f90728 4863422c 3faaa83a 375dfa91    (...,BcH:..?..]7
  80000030: f708c998 a5e27535 2df72513 c2210796    ....5u...%.-..!.
  => 

