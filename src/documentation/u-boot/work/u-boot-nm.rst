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
  80000010: 00000000 00000000 62a2cc8a def1601a    ...........b.`..
  80000020: 65b8b965 fb0fa81b c202c517 7fc93243    e..e........C2..
  80000030: d5246ead 92d57185 768d30c9 cecb8383    .n$..q...0.v....
  => 

The :redtext:`nm` command also accepts the type :redtext:`.l`, :redtext:`.w` and :redtext:`.b`
