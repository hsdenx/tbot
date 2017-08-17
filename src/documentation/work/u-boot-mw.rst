mw - memory write (fill)
........................


::

  => help mw
  mw - memory write (fill)
  
  Usage:
  mw [.b, .w, .l] address value [count]
  => 

The :redtext:`mw` command is a way to initialize (fill) memory with some value. When called without a count argument, the value will be written only to the specified address. When used with a count value, the entire memory area will be initialized with this value: 


::

  => md 0x80000000 0x10
  80000000: 6c6c6548 2020206f 01234567 27e177ee    Hello   gE#..w.'
  80000010: 85a9141f ea0e0d29 a3b83b60 9c5abf20    ....)...`;.. .Z.
  80000020: d5f90728 4863422c 3faaa83a 375dfa91    (...,BcH:..?..]7
  80000030: f708c998 a5e27535 2df72513 c2210796    ....5u...%.-..!.
  => mw 0x80000000 0xaabbccdd
  => md 0x80000000 0x10
  80000000: aabbccdd 2020206f 01234567 27e177ee    ....o   gE#..w.'
  80000010: 85a9141f ea0e0d29 a3b83b60 9c5abf20    ....)...`;.. .Z.
  80000020: d5f90728 4863422c 3faaa83a 375dfa91    (...,BcH:..?..]7
  80000030: f708c998 a5e27535 2df72513 c2210796    ....5u...%.-..!.
  => mw 0x80000000 0 6
  => md 0x80000000 0x10
  80000000: 00000000 00000000 00000000 00000000    ................
  80000010: 00000000 00000000 a3b83b60 9c5abf20    ........`;.. .Z.
  80000020: d5f90728 4863422c 3faaa83a 375dfa91    (...,BcH:..?..]7
  80000030: f708c998 a5e27535 2df72513 c2210796    ....5u...%.-..!.
  => 

This is another command that accepts the type extensions :redtext:`.l`, :redtext:`.w` and :redtext:`.b` :


::

  => mw.w 0x80000004 0x1155 6
  => md 0x80000000 0x10
  80000000: 00000000 11551155 11551155 11551155    ....U.U.U.U.U.U.
  80000010: 00000000 00000000 a3b83b60 9c5abf20    ........`;.. .Z.
  80000020: d5f90728 4863422c 3faaa83a 375dfa91    (...,BcH:..?..]7
  80000030: f708c998 a5e27535 2df72513 c2210796    ....5u...%.-..!.
  => mw.b 0x80000007 0xff 7
  => md 0x80000000 0x10
  80000000: 00000000 ff551155 ffffffff 1155ffff    ....U.U.......U.
  80000010: 00000000 00000000 a3b83b60 9c5abf20    ........`;.. .Z.
  80000020: d5f90728 4863422c 3faaa83a 375dfa91    (...,BcH:..?..]7
  80000030: f708c998 a5e27535 2df72513 c2210796    ....5u...%.-..!.
  => 

