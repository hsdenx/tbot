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

  => cmp 0x80000000 0x80100000L 40000
  Total of 262144 word(s) were the same
  => md 0x80000000 0xc
  80000000: a555037f 7d9aebcf 1a1e2529 dfb0e082    ..U....})%......
  80000010: 0d838660 e04e09df 62a2cc8a def1601a    `.....N....b.`..
  80000020: 65b8b965 fb0fa81b c202c517 7fc93243    e..e........C2..
  => md 0x80100000L 0xc
  80100000: a555037f 7d9aebcf 1a1e2529 dfb0e082    ..U....})%......
  80100010: 0d838660 e04e09df 62a2cc8a def1601a    `.....N....b.`..
  80100020: 65b8b965 fb0fa81b c202c517 7fc93243    e..e........C2..
  => 

Like most memory commands the :redtext:cmp` can access the memory in different sizes: as 32 bit (long word), 16 bit (word) or 8 bit (byte) data. If invoked just as cmp the default size (32 bit or long words) is used; the same can be selected explicitly by typing cmp.l instead. If you want to access memory as 16 bit or word data, you can use the variant cmp.w instead; and to access memory as 8 bit or byte data please use cmp.b.

|Warning| Please note that the count argument specifies the number of data items to process, i. e. the number of long words or words or bytes to compare. 


::

  => cmp.l 0x80000000 0x80100000L 40000
  Total of 262144 word(s) were the same
  => cmp.w 0x80000000 0x80100000L 80000
  Total of 524288 halfword(s) were the same
  => cmp.b 0x80000000 0x80100000L 100000
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

  => cp 0x80000000 0x80100000L 10000
  => 

The :redtext:`cp` command understands the type extensions :redtext:`.l`, :redtext:`.w` and :redtext:`.b` : 


::

  => cp.l 0x80000000 0x80100000L 10000
  => cp.w 0x80000000 0x80100000L 20000
  => cp.b 0x80000000 0x80100000L 40000
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
  80000000: a555037f 7d9aebcf 1a1e2529 dfb0e082    ..U....})%......
  80000010: 0d838660 e04e09df 62a2cc8a def1601a    `.....N....b.`..
  80000020: 65b8b965 fb0fa81b c202c517 7fc93243    e..e........C2..
  80000030: d5246ead 92d57185 768d30c9 cecb8383    .n$..q...0.v....
  80000040: 4cc9e97b 852c5e63 9cf20e84 4f946122    {..Lc^,....."a.O
  80000050: 98649544 0a9a9788 526ca383 caa717c9    D.d.......lR....
  80000060: 40833929 97efd07d 93b179f9 faa3c3d2    )9.@}....y......
  80000070: d9aadf23 272e8f4c 8686240a 2230043a    #...L..'.$..:.0"
  80000080: 3939631e 3eb909cb 369e094f b2bb9795    .c99...>O..6....
  80000090: e64395c4 553b38e3 1e68ac97 ffdd5ff3    ..C..8;U..h.._..
  800000a0: 16c77f90 12bf8209 3b22f187 d922fba9    ..........";..".
  800000b0: 0f8a8ebc 3bee36c1 3d432085 04eb523f    .....6.;. C=?R..
  800000c0: 8525a54d bb52b1ea 1bd58cc6 210481d9    M.%...R........!
  800000d0: ef186528 dc261323 17e5f5bf d57f5029    (e..#.&.....)P..
  800000e0: 6bd14e6d f5289e33 07fcfa87 e9fef934    mN.k3.(.....4...
  800000f0: 1f4bdda6 2ef1e31d 2d7a05b2 2d21b481    ..K.......z-..!-
  => 

This command can also be used with the type extensions :redtext:`.l`, :redtext:`.w` and :redtext:`.b` : 


::

  => md.w 0x80000000
  80000000: 037f a555 ebcf 7d9a 2529 1a1e e082 dfb0    ..U....})%......
  80000010: 8660 0d83 09df e04e cc8a 62a2 601a def1    `.....N....b.`..
  80000020: b965 65b8 a81b fb0f c517 c202 3243 7fc9    e..e........C2..
  80000030: 6ead d524 7185 92d5 30c9 768d 8383 cecb    .n$..q...0.v....
  80000040: e97b 4cc9 5e63 852c 0e84 9cf2 6122 4f94    {..Lc^,....."a.O
  80000050: 9544 9864 9788 0a9a a383 526c 17c9 caa7    D.d.......lR....
  80000060: 3929 4083 d07d 97ef 79f9 93b1 c3d2 faa3    )9.@}....y......
  80000070: df23 d9aa 8f4c 272e 240a 8686 043a 2230    #...L..'.$..:.0"
  => md.b 0x80000000
  80000000: 7f 03 55 a5 cf eb 9a 7d 29 25 1e 1a 82 e0 b0 df    ..U....})%......
  80000010: 60 86 83 0d df 09 4e e0 8a cc a2 62 1a 60 f1 de    `.....N....b.`..
  80000020: 65 b9 b8 65 1b a8 0f fb 17 c5 02 c2 43 32 c9 7f    e..e........C2..
  80000030: ad 6e 24 d5 85 71 d5 92 c9 30 8d 76 83 83 cb ce    .n$..q...0.v....
  => 

.. raw:: pdf

   PageBreak

The last displayed memory address and the value of the count argument are remembered, so when you enter md again without arguments it will automatically continue at the next address, and use the same count again. 


::

  => md.b 0x80000000 0x20
  80000000: 7f 03 55 a5 cf eb 9a 7d 29 25 1e 1a 82 e0 b0 df    ..U....})%......
  80000010: 60 86 83 0d df 09 4e e0 8a cc a2 62 1a 60 f1 de    `.....N....b.`..
  => md.w 0x80000000
  80000000: 037f a555 ebcf 7d9a 2529 1a1e e082 dfb0    ..U....})%......
  80000010: 8660 0d83 09df e04e cc8a 62a2 601a def1    `.....N....b.`..
  80000020: b965 65b8 a81b fb0f c517 c202 3243 7fc9    e..e........C2..
  80000030: 6ead d524 7185 92d5 30c9 768d 8383 cecb    .n$..q...0.v....
  => md 0x80000000
  80000000: a555037f 7d9aebcf 1a1e2529 dfb0e082    ..U....})%......
  80000010: 0d838660 e04e09df 62a2cc8a def1601a    `.....N....b.`..
  80000020: 65b8b965 fb0fa81b c202c517 7fc93243    e..e........C2..
  80000030: d5246ead 92d57185 768d30c9 cecb8383    .n$..q...0.v....
  80000040: 4cc9e97b 852c5e63 9cf20e84 4f946122    {..Lc^,....."a.O
  80000050: 98649544 0a9a9788 526ca383 caa717c9    D.d.......lR....
  80000060: 40833929 97efd07d 93b179f9 faa3c3d2    )9.@}....y......
  80000070: d9aadf23 272e8f4c 8686240a 2230043a    #...L..'.$..:.0"
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
  80000000: a555037f ? 0
  80000004: 7d9aebcf ? 0xaabbccdd
  80000008: 1a1e2529 ? 0x01234567
  8000000c: dfb0e082 ? .
  => md 0x80000000 10
  80000000: 00000000 aabbccdd 01234567 dfb0e082    ........gE#.....
  80000010: 0d838660 e04e09df 62a2cc8a def1601a    `.....N....b.`..
  80000020: 65b8b965 fb0fa81b c202c517 7fc93243    e..e........C2..
  80000030: d5246ead 92d57185 768d30c9 cecb8383    .n$..q...0.v....
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
  80000000: 02020101 87654321 01234567 dfb0e082    ....!Ce.gE#.....
  80000010: 0d838660 e04e09df 62a2cc8a def1601a    `.....N....b.`..
  80000020: 65b8b965 fb0fa81b c202c517 7fc93243    e..e........C2..
  80000030: d5246ead 92d57185 768d30c9 cecb8383    .n$..q...0.v....
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
  80000000: 6c6c6548 2020206f 01234567 dfb0e082    Hello   gE#.....
  80000010: 0d838660 e04e09df 62a2cc8a def1601a    `.....N....b.`..
  80000020: 65b8b965 fb0fa81b c202c517 7fc93243    e..e........C2..
  80000030: d5246ead 92d57185 768d30c9 cecb8383    .n$..q...0.v....
  => 

