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
  80000010: 00000000 00000000 6f236743 3b46fbe6    ........Cg#o..F;
  80000020: ea2356f6 6e7c540f e056e377 7bd28a9f    .V#..T|nw.V....{
  80000030: cfa9bcec b19ace51 b27f4dc5 8eeca28b    ....Q....M......
  => 

The :redtext:`nm` command also accepts the type :redtext:`.l`, :redtext:`.w` and :redtext:`.b`
