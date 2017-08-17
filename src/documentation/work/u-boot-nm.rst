nm - memory modify (constant address)
.....................................


::

  => help nm
  nm - memory modify (constant address)
  
  Usage:
  nm [.b, .w, .l] address
  => 

The :redtext:`nm` command (non-incrementing memory modify) can be used to interactively write different data several times to the same address. This can be useful for instance to access and modify device registers: 


::

  => nm 0x80000000
  80000000: 00000000 ? 0x48
  80000000: 00000048 ? 0x65
  80000000: 00000065 ? 0x6c
  80000000: 0000006c ? 0x6c
  80000000: 0000006c ? 0x6f
  80000000: 0000006f ? .
  => md 0x80000000 10
  80000000: 0000006f ff551155 ffffffff 1155ffff    o...U.U.......U.
  80000010: 00000000 00000000 a3b83b60 9c5abf20    ........`;.. .Z.
  80000020: d5f90728 4863422c 3faaa83a 375dfa91    (...,BcH:..?..]7
  80000030: f708c998 a5e27535 2df72513 c2210796    ....5u...%.-..!.
  => 

The :redtext:`nm` command also accepts the type :redtext:`.l`, :redtext:`.w` and :redtext:`.b`
